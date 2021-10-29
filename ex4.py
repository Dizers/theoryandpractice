import random
import numpy as np

lst = np.random.uniform(-100, 100, 10)
res = sorted(lst, key = lambda x: abs(x-int(x)))
print(res)
