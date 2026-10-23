items=[
    ("Laptop",50000),
    ("Mouse",500),
    ("Keyboard",1500)
]
products,price=zip(*items)
print(list(products))
print(list(price))