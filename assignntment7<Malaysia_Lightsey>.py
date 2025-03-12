pizza_orders = ["Pepperoni", "Cheese", ""Chicken", "Sausage", "Hawaiian"]
finished_pizzas = []

while pizza_orders:
    current_pizza = pizza_orders.pop(0)  # Take the first pizza from the list
    print(f"Your {current_pizza} pizza pie is finished!")  # Notify the customer
    finished_pizzas.append(current_pizza)  # Move it to the finished list

print("\nAll pizzas have been made!\n")
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.") 
