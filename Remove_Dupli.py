with open("E:\Documents\IP_LOG.txt", 'r+') as fd:
    lines = fd.readlines()
    res = [*set(lines)]
    with open("E:/Documents/IP_LOG2.txt", "a") as external_file:
        add_text = res
        print(add_text, file=external_file)
        external_file.close()
    print (res)