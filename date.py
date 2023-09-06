from datetime import date
import webbrowser


today = date.today()
str_today = str(today)
print(today)


password = input("Enter password")
count = 0
for i in range(len(str_today)):
    if (str_today[i]== password[i]):
        count = count+1
    
if(len(password)==count):
    print("you entered correct password")
    url="https://www.youtube.com/"
   # url="https://mail.google.com/mail/u/0/#inbox"
    webbrowser.open_new_tab(url)  
else:
   print("u have entered wrong password")
