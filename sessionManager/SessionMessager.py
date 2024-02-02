from sessionManager.MessageGenerator import MessageGenerator
import pickle
import json
import requests
YOUR_RESOURCE_NAME = "apim-aoai-eas-dev02"
YOUR_DEPLOYMENT_NAME = "cs5483-2024"
API_VERSION = "2023-08-01-preview"
MY_GP = "cs-gpt4-0314"
fernet = None
key = None
url = f"https://{YOUR_RESOURCE_NAME}.azure-api.net/{YOUR_DEPLOYMENT_NAME}/openai/deployments/{MY_GP}/chat/completions?api-version={API_VERSION}"


with open("key.pickle","rb") as f1:
    fernet = pickle.load(f1)
with open("haha.dit","rb") as f2:
    key = fernet.decrypt(f2.read()).decode()
headers = {
    "Content-Type":"application/json",
    "Cache-Control": "no-cache",
    "api-key":key
}
class SessionMessager:
    def sendMessage(self,session,text,system = False):
        func = MessageGenerator.getQuest if not system else MessageGenerator.getSys
        session.addMessage(text,func)
        return self._getByMessages(session)
    def _getByMessages(self,session):
        data = {
            "messages": session.getMessages()
        }
        data = json.dumps(data)
        res = requests.post(url,data=data,headers=headers)
        res = res.json()
        if 'choices' in res and len(res['choices']) > 0:
            session.addMessage(res["choices"][0]["message"]["content"], MessageGenerator.getAns)
            return res["choices"][0]["message"]["content"]
        else:
            session.rollback()
            return None