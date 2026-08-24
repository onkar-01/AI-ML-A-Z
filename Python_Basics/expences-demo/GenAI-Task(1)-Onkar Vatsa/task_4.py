from task_1 import products
from task_2 import categories
from task_3 import price_dict

tuple_list = []
# 1.
for i, product in enumerate(products):
    if product in price_dict:
        tuple_list.append((product, price_dict[product], categories[i]))

print(tuple_list)

# 2. 

category_to_products = {}

for product in tuple_list:
    if product[2] not in category_to_products:
        category_to_products[product[2]] = []
    category_to_products[product[2]].append(product[0])

print(category_to_products)

# 3.

print(max(category_to_products.values(),key=len))