class MessageGenerator:
    @classmethod
    def getQuest(self,quest):
        return {"role": "user", "content": quest}
    @classmethod
    def getAns(self,ans):
        return {"role":"assistant","content": ans}
    @classmethod
    def getSys(self,mes):
        return {"role": "system","content": mes}