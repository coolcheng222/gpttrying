from sessionManager.MessageGenerator import MessageGenerator


def func(session_id,text):
    # 获取session
    session = getSession(session_id)
    messages = session.message

    # 更改message
    session.addMessage(text,MessageGenerator.getQuest)
    res = send(messages)
    session.addMessage(text,MessageGenerator.getAns)
    
    session.setMessage(messages)