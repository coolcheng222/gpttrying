from flask import Flask, jsonify, request
from flask_cors import *

from sessionManager.SessionManager import SessionManager
from sessionManager.SessionMessager import SessionMessager
app = Flask(__name__)
CORS(app, supports_credentials=True)

session = SessionManager().createSession()
res = SessionMessager().sendMessage(session,"nihao")
print(res)
print(session.getMessages())


# @app.route("/chat/<session_id>",methods=["POST"])
# def chat():

    


# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000)