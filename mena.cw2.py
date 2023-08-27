my_name =input("my_name")
my_age = int(input("my_age"))
print(f"my name is {my_name} and iam {my_age}")

first_number = int (input(" first_numer"))
second_number =int (input("second_number"))
operation =input(" what is the operation(+-*/)")

if operation == "+" :
     print( first_number + second_number)
elif operation == "-" :
       print(first_number - second_number)
elif operation == "*" :
      print(first_number * second_number)
elif operation == "/" :
      print(first_number / second_number)
else : 
      print("the operation is not avalib")

bus_capacity = (40)

people_inbus = int(input(" how many people in bus"))

empty_sets = bus_capacity - people_inbus

if bus_capacity >= people_inbus :
       print (f" there is {empty_sets} sets avalib") 
elif bus_capacity< people_inbus :
       print(" sorry the bus is full") 