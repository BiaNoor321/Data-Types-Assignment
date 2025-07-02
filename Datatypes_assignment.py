# Integer :
age = 14
print("In 5 years, you will be", age + 5)

# String :
name = "Bia"
greeting = "Hello" +" "+ name + "!"
print (greeting)

# Float :
height = 5.1
print("My_height_is" , height , "meters")

# Combined Use
item = "book"  # String
quantity = 4  # Integar
price_per_item = 12.99  # Float
total_cost = price_per_item * quantity
print("You_bought" , quantity , item + "s" , "for a total of" , total_cost , "dollars")

# Challenge
name = str(input("Enter your name :"))
item = str(input("What do you want :"))
price = float(input("price per item :"))
quantity = int(input("quantity of your item :"))
total = price * quantity
print(total)
print(f"Hello {name}! You bought {quantity} {item}s. Total: {total} dollars.")