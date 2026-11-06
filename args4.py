def employee_details(*args):
    for value in args:
        print("Positional Arguments:\n",value)
employee_details(
    "Adarsh","Python","Developer","Bengaluru"
)
def employee_details(**kwargs):
    for key,value in kwargs.items():
        print("Keyword Arguments:\n",key,":",value)
employee_details(age=21,experience="Fresher")