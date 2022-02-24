def getmsg(self):
        inject_dll.readMapping.restype = c_wchar_p
        buff = create_unicode_buffer(5000)
        # https://zhuanlan.zhihu.com/p/419821472
        msg = inject_dll.readMapping("NewMessageLog",buff,5000)
        if not msg:
            return False
        buff = create_unicode_buffer(50)
        inject_dll.writeMapping("NewMessageLog",buff,50)
        for i in range(-1, -20, -1):

                if msg[i] == '}':
                    j = i
                if msg[i] == '{':
                    k = i
                    break

        msgtype = ''
        try:
            for i in range(k + 1, j):
                msgtype = msgtype + msg[i]
        except UnboundLocalError:
            msgtype = '长链接'
            return {"text":msg,"wxid":None,"type":msgtype}
        msgwxid = msgtype.split('[')[1].replace(']','')
        msgtype = msgtype.split('[')[0]
        msg = msg[::-1].replace(msgtype[::-1],'')[::-1]
        msg = msg[::-1].replace(msgwxid[::-1], '')[::-1].replace('{[]}','')
        if msgwxid=='filehelper':
            self.runcommand(msg)
        return {"text":msg,"wxid":msgwxid,"type":msgtype}