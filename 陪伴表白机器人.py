import itchat
# https://mp.weixin.qq.com/s?__biz=MzUxNDY5NTYzMg==&mid=2247483750&idx=1&sn=b894b91ff8c7ad2c6b7c996d1b0ed5f9&chksm=f94349d9ce34c0cf1423f23a7e155be15626fefbcf74c82d497cf02113bf0cad20873aff21cd&scene=21#wechat_redirect
@itchat.msg_register('Text') #注册文本消息
def text(msg):
    message =  msg['Text'] #接收文本消息
    fromName =msg['FromUserName'] #发送方
    toName = msg['ToUserName'] #接收方
    if toName == "filehelper":
        print(message)#打印输入的消息

itchat.auto_login()
itchat.send("登录成功！开始发消息吧！","filehelper")
itchat.run()