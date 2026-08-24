import numpy as np

amounts_list = [250,1200,90,500]
amount = np.array(amounts_list)

print("array", amount)
print("dtype:", amount.dtype)
print("shape:", amount.shape)

with_tax = amount * 1.18 # vectorized no loop
print("with tax:",with_tax)

table = np.array([
    [250, 0.18],
    [1200, 0.05],
    [90, 0.18],
])

taxes = table[:,0] * table[:,1];

print("taxes:",taxes)