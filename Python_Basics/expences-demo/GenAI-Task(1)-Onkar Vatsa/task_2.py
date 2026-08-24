categories = ["electronics", "electronics", "electronics", "electronics",
              "accessories", "wearables", "electronics", "gaming", "gaming"]

# 1. create a set of categories
categories_set = set(categories)
print("Categories Set:", categories_set)

# 2. 
categories_set.add("software")
print("After adding 'software':", categories_set)

categories_set.add("electronics")   
print("After adding duplicate 'electronics':", categories_set)

# 3. 
print("Is 'gaming' in set?", "gaming" in categories_set)
print("Is 'furniture' in set?", "furniture" in categories_set)
print("Total unique categories:", len(categories_set))
