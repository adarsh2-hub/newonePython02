from collections import OrderedDict
fruits=OrderedDict()
fruits["Apple"]=50
fruits["Banana"]=30
fruits["Mango"]=60
fruits.move_to_end("Apple")
print(fruits)