
# for port in range(8088)

from myfile import back_up_and_write


out_str=""
for ip_end in  range(101,202):
    out_str+=f"192.168.0.{ip_end}|8080\n"
    # print(f"192.168.0.{ip_end}")
    
# back_ 

# with open("telnet_list.txt",)

list_path="telnet_list.txt"
back_up_and_write(list_path,out_str)
