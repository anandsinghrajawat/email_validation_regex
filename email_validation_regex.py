#a-z
#0-9
#one dot or one underscore one @
#dot must be at secone or third position from the end 
import re
email_condition="^[a-z]+[\._]?[a_z 0_9]+[@]\w+[.]\w{2,3}$"
user_email=input("enter your email : ")

if re.search(email_condition,user_email):
    print("right email")
else:
    print("wrong email")    
