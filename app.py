from flask import Flask, jsonify, request
from flask_cors import *
from Msg import Msg

from sessionManager.SessionManager import SessionManager
from sessionManager.SessionMessager import SessionMessager
app = Flask(__name__)
CORS(app, supports_credentials=True)
sessionManager = SessionManager()
SessionMessager = SessionMessager()
# res = SessionMessager().sendMessage(session,"nihao")
# print(res)
# print(session.getMessages())


@app.route("/chat/start",methods=["POST"])
def sessionStart():
    session = sessionManager.createSession()
    if session == None:
        return jsonify(Msg.FAIL("unknown error creating session"))
    else:
        return Msg.SUCCESS(session.session_id)

@app.route("/chat",methods=["POST"])
def chat():
    data = request.get_json()
    if "session_id" in data and "text" in data:
        session_id = data["session_id"]
        text = data["text"]
        session = sessionManager.getSession(session_id)
        if session == None:
            return Msg.FAIL("error session id")
        res = SessionMessager.sendMessage(session,text, True if "system" in data and data["system"] else False)
        if res == None:
            return Msg.FAIL("error response")
        else:
            return Msg.SUCCESS(res)
    else:
        return Msg.FAIL("error json")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)