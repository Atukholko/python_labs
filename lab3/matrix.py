import numpy as np


# 10000x10000: 149.65234375
# 1000x1000: 10013.45703125 with sleep 1
# 100x100: 10004.6875 with sleep 1
def decorate_matrix_1v(n: int):
    result_array = np.ones((n, n), int)
    result_array[1:-1, 1:-1] = 0
    return result_array


# 10000x10000: 129.654296875
# 1000x1000: 10023.599609375 with sleep 1
# 100x100: 10005.12890625 with sleep 1
def decorate_matrix_2v(n: int):
    result_array = np.zeros((n, n), int)
    result_array[:1] = 1
    result_array[-1:] = 1
    result_array[1:-1, :1] = 1
    result_array[1:-1, -1:] = 1
    return result_array


# for n >= 10000 2v is more effective
print(decorate_matrix_2v(10000))
