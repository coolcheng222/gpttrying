import time
import random
import h5py
class Message:
    def __init__(self):
        self.messages = []
    def append(self,text):
        self.messages.append(text)
    def getMessages(self):
        return list(self.messages[:])
    def setMessages(self,messages):
        self.messages = messages
    def rollback(self):
        if len(self.message) > 0:
            self.messages = self.messages[:len(self.messages) - 1]
class Session:
    def __init__(self):
        self.timestamp = int(time.time() * 1000)
        random_number = random.randint(0, 9999)
        self.session_id = f"{self.timestamp}-{random_number}"
        self.message = Message()

    def addMessage(self,text,transfermation):
        self.message.append(transfermation(text))
    def getMessages(self):
        return self.message.getMessages()
    def rollback(self):
        self.message.rollback()


    
# # 创建一个Session对象
# session = Session(60)

# # 将Session对象存储到HDF5文件
# with h5py.File('session.h5', 'a') as f:
#     session_data = session.to_dict()
#     group = f.create_group('sessions')
#     for key, value in session_data.items():
#         group.create_dataset(key, data=value)

# # 从HDF5文件中读取指定session_id的Session对象
# def load_session_from_hdf5(session_id):
#     with h5py.File('session.h5', 'r') as f:
#         group = f['sessions']
#         session_data = {}
#         for key in group.keys():
#             session_data[key] = group[key][()]
        
#         session_data['session_id'] = session_id
#         restored_session = Session.from_dict(session_data)
    
#     return restored_session

# # 指定session_id来加载Session对象
# loaded_session = load_session_from_hdf5(session.session_id)

# # 检查加载的Session对象
# print("Loaded Session:")
# print("Timestamp:", loaded_session.timestamp)
# print("Session ID:", loaded_session.session_id)
# print("TTL:", loaded_session.ttl)
# print("TTL Base:", loaded_session.ttl_base)
# print("Activated:", loaded_session.activated)