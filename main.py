# from bs4 import BeautifulSoup
# with open("lesson parsing 28.08.html") as fp:
#     text = BeautifulSoup(fp, "html.parser")
#     find_text = text.find('div', {'id': 'GodenMorgen'}).get_text()
#     b = text.body.div
#     print(b)



import numpy as np
import random
# arr = np.array([[1,2,3],[4,5,6]])
# arr
#
# array = ([[1,2,3],[4,5,6]])
#
# arr * arr
#
# arr - arr

# r = [
#         [1,2,3,4,5,7],
#         [1,2,3,4,5,6],
#         [1,2,3,4,5,7],
#         [1,2,3,4,5,6],
#         [1,2,3,4,5,7]
# ]
#
# a = np.array(r)
#
# num_columns = a.shape[1]
# first_column = a[0]
# last_column = a[-1]

# s = [s[0] for s in a]
# g = [g[4] for g in a]
#
# for i in range (len(a)):
#     if i % 2 == 0:
#         print(a[i])

# a = np.array([[random.randint(1, 9) for _ in range(1, 11)] for _ in range(10)]).reshape(10, 10)
#
# example = [a[:, 1::2][:, x] for x in range(len(a[:, 1::2][0]))]
# result = [x for x in example if x[0] > x[-1]]
# print(*example)
# print(*result)

# print(s,g)
# print(a[:,0])
# print(a[:,4])
# print(first_column)
# print(last_column)

