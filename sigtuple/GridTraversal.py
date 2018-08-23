
# coding: utf-8

# In[5]:

import numpy as np


# In[83]:

m, n = map(int, input().strip().split())


# In[7]:

grid = []
for i in range(m):
    row = list(map(int, input().strip().split()))
    assert(len(row) == n)
    grid.append(row)
grid = np.array(grid)


# In[75]:

def count_factor(num):
    count = [0, 0]
    factor = [2, 5]
    for i in range(len(factor)):
        while num % factor[i] == 0:
            count[i] += 1
            num = int(num / factor[i])
    return count


# In[76]:

def min_zero_path(tuple_1, tuple_2):
    zeros_1 = min(tuple_1)
    zeros_2 = min(tuple_2)
    if zeros_1 < zeros_2:
        return tuple_1
    else:
        return tuple_2


# In[77]:

def sum_tuples(tuple1, tuple2):
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


# In[78]:

# def min_grid_zeros(grid, i, j, twos, fives):
#     if i >= grid.shape[0] and j >= grid.shape[1]:
#         return twos, fives
#     else:
#         twos, fives = twos + count_factor(grid[i, j], 2), fives + count_factor(grid[i, j], 5)
#         print(twos, fives, i, j)
#         twos_r, fives_r = min_grid_zeros(grid, i, j+1, twos, fives)
#         zeros_r = min(twos_r, fives_r)
#         twos_d, fives_d = min_grid_zeros(grid, i+1, j, twos, fives)
#         zeros_d = min(twos_d, fives_d)
#         if zeros_d < zeros_r:
#             return twos_d, fives_d
#         else:
#             return twos_r, fives_r


# In[79]:

def min_grid_zeros(grid, i, j, m, n, twos, fives):
    if i == m - 1 and j == n - 1:
        return count_factor(grid[i, j])
    elif i == m - 1:
        return sum_tuples(count_factor(grid[i, j]), min_grid_zeros(grid, i, j + 1, m, n, twos, fives))
    elif j == n - 1:
        return sum_tuples(count_factor(grid[i, j]), min_grid_zeros(grid, i + 1, j, m, n, twos, fives))
    else:
        return min_zero_path(
            sum_tuples(count_factor(grid[i, j]), min_grid_zeros(
                grid, i + 1, j, m, n, twos, fives)),
            sum_tuples(count_factor(grid[i, j]), min_grid_zeros(
                grid, i, j + 1, m, n, twos, fives))
        )


# In[80]:

def res_min_grid_zeros(grid):
    return min(min_grid_zeros(grid, 0, 0, grid.shape[0], grid.shape[1], 0, 0))


# In[81]:

res_min_grid_zeros(grid)


# In[ ]:
