import re
email="Contact us at adarshgouda02@gmail.com or support@yahoo.com"
result=re.findall(r"\w+",email)
print(result)