from sessionManager.Session import Session


class SessionManager:
    def __init__(self):
        self.sessions = {}
    def createSession(self):
        session = Session()
        self.sessions[session.session_id] = session
        return session
    def deleteSession(self,session_id):
        if not session_id in self.sessions:
            return None
        else:
            return self.sessions.pop(session_id);
    def updateSession(self,session_id,session):
        if not session_id in self.sessions:
            return False
        elif session == None:
            return False
        self.sessions[session_id] = session
        return True
    def getSession(self,session_id):
        if not session_id in self.sessions:
            return None
        else:
            return self.sessions[session_id]
    def getSessionList(self):
        return self.sessions