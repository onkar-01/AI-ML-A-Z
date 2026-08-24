price_dict = {
    "laptop":45000,
    "mobile":15000,
    "tablet":10000,
    "desktop":25000,
    "headphone":5000,
    "smart-watch":2500,
    "tablet":1500,
}

def func(product_name,action,price=0):
    if(action == "remove"):
        price_dict.pop(product_name)
        print(f"{product_name} removed")
    elif(action == "add"):
        price_dict[product_name] = price
        print(f"{product_name} added")
    elif(action == "update"):
        price_dict[product_name] = price
        print(f"{product_name} updated")
    else:
        print("Invalid action")

func("laptop", "remove")
func("keyboard","add",3500)
func("tablet","update",20000)

print(price_dict)
print(f"Average price : {int(sum(price_dict.values()) / len(price_dict))}")
print(f"Max price : {max(price_dict.values())}") 
print(f"Min price : {min(price_dict.values())}") 

