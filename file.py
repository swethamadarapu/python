temp =" "
with open("class.py","r+")as fs:
    temp =fs.read()
    if("Sai" in temp):
        print("it is in the file")
    else:
        with open("class.py","a")as fs:
            fs.write("sai")
