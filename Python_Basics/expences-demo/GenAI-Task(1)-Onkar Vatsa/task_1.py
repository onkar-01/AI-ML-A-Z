# 1.
products = ["laptop","mobile","tablet","desktop","headphone"]
# 2.
sample_product = ("laptop", 50000, "electronics")  # (product_name, price, category)
# 3.
print(products[1],products[-1])
# 4.
# one by one 
products.append("smart-watch") 
products.append("tabet")
# multiple at a time 
products.extend(["play-station","controller"])
print(products)

# 5. extra (optional)
sample_product_list = list(sample_product)
sample_product_list[1] = 45000
sample_product = tuple(sample_product_list)
print(sample_product)
