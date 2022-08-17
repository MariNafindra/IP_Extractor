import re
import sys

with open('E:/Documents/log.txt', 'r') as file:
    fi = file.readlines()
re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
# re_port = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$\/(\d+)")

# print("This text will be added to the file")

for line in fi:
    ip = re.findall(re_ip,line)
    # port = re.findall(re_port,line)
    # 
    with open("E:/Documents/IP_LOG.txt", "a") as external_file:
        add_text = ip
        print(add_text, file=external_file)
        external_file.close()
    print (ip)
    