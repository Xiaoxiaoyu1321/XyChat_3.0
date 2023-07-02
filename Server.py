#导入模块
import socket
import time
import select
import os
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

SP = "|||"

host = "0.0.0.0" #服务器地址
port = 18679 #端口
print("[Server]服务器：",host)
print("[Server]端口:",port)
StartNewServer = False #设定主线程启动新服务器为禁用

#启动服务器监听
def StartServerListen(): 
    serversocket.bind((host,port)) #绑定端口
    serversocket.listen(100) #设置监听数量
    print("[Server]已开启监听，最多100个用户连接")
    


StartServerListen()
#主循环
while True:
    print("[Server]等待用户连接")
    
    clientsocket,addr = serversocket.accept() #同意所有用户连接
    print("[Server]新用户连接" ,str(addr))
    
    try:
        
        pass
    except Exception as q:
        print("[Error]错误信息:" , q)
        
    
    
    
