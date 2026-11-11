import re
email="adarshgouda02@gmail.com"
result=re.search("@",email)
if result:
    print("Valid Email!")
else:
    print("Invalid Email!")