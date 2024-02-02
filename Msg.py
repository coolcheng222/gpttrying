class Msg:
    @classmethod
    def SUCCESS(self,text):
        return {
            "code": 0,
            "message": text
        }
    @classmethod
    def FAIL(self,text):
        return {
            "code": 1,
            "message": text
        }
    def __init__(self,code,text):
        return {
            "code": code,
            "message": text
        }