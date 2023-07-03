#导入模块
import socket
import time
import select
import os
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
onlineUser = []
onlineUserIP = []


SP = "|$|"

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
    
def recvMessage():
    while True:
        back = serversocket.recv(9999).decode('gbk')
        try:
            aback = back.split(SP)



            def GetLoginUserName():
                
                try:
                    with open(r'./Users/' + aback[2] , "r") as f: #阅读账户文件
                    userAccount = f.read()
                    userAccount1 = userAccount.split(SP)
                    userName = userAccount1[0]
                    userPassword = userAccount1[1]
                except Exception as w:
                    print("无效登录请求,", w)
            





            
            if len(aback) >= 2:
                if aback[0] == "Login"and len(aback) =5: #当收到登录请求时
                    
                    GetLoginUserName()

                    if aback[2] == userName and aback[3] == userPassword:#如果密码符合则
                        onlineUser.append(aback[1] + SP +aback[4])
                elif aback[0] == "newMessage" and len(aback)>=5:
                    
                    

StartServerListen()
#主循环
while True:
    print("[Server]等待用户连接")
    
    clientsocket,addr = serversocket.accept() #同意所有用户连接
    print("[Server]新用户连接" ,str(addr))

        
    
    try:
        #添加连接用户到列表
        onlineUserIP.append(str(addr))
        
        
    except Exception as q:
        print("[Error]错误信息:" , q)
        
    
    

