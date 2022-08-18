def change_mac(mac, num, offset=1 ):
    li = list()
    for i in range(num):
    #  使用format格式化字符串，int函数，按照16进制算法，将输入的mac地址转换成十进制，然后加上偏移量
    # {:012X}将十进制数字，按照16进制输出。其中12表示只取12位，0表示不足的位数在左侧补0
        mac.sp
        mac_address = "{:012X}".format(int(mac, 16) + offset * i)
        print(mac_address)
        li.append(mac_address)
    print(li)

start_mac = '0102030405AF'
change_mac(start_mac,10)
