import json
import pickle
import requests
from cryptography.fernet import Fernet
messages = []
YOUR_RESOURCE_NAME = "apim-aoai-eas-dev02"
YOUR_DEPLOYMENT_NAME = "cs5483-2024"
API_VERSION = "2023-08-01-preview"
MY_GP = "cs-gpt4-0314"
fernet = None
key = None
with open("key.pickle","rb") as f1:
    fernet = pickle.load(f1)
with open("haha.dit","rb") as f2:
    key = fernet.decrypt(f2.read()).decode()
url = f"https://{YOUR_RESOURCE_NAME}.azure-api.net/{YOUR_DEPLOYMENT_NAME}/openai/deployments/{MY_GP}/chat/completions?api-version={API_VERSION}"
headers = {
    "Content-Type":"application/json",
    "Cache-Control": "no-cache",
    "api-key":key
}
def getByMessages():
    data = {
        "messages": messages
    }
    data = json.dumps(data)
    res = requests.post(url,data=data,headers=headers)
    res = res.json()
    if 'choices' in res and len(res['choices']) > 0:
        messages.append({"role":"assistant","content": res["choices"][0]["message"]["content"]})
        return res["choices"][0]["message"]["content"]
    else:
        return None
def getGpt4Img(quest,image_url):
    content = [{"type":"text","text": quest},
     { "type": "image_url", "image_url": { "url": image_url } }]
    messages.append({"role":"user","content":content})
    return getByMessages()
def getGpt4Text(quest):
    messages.append({"role": "user", "content": quest})
    return getByMessages()
context = []
# r = getGpt4Img("描述一下","https://ssl.gstatic.com/support/content/images/static/homepage_header_background_v2.svg")
# print(r)niha
while True:
    q = input("Me: ")
    if q == "q":
        break
    ans = getGpt4Text(q)
    print(ans)