__author__ = 'Ivan Truskov'

# 1.
import numpy as np
a = np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])
mean_a = a.mean(0)
# 2.
a_centered = a - mean_a
# 3.
a_centered_sp = np.dot(a_centered[:, 0], a_centered[:, 1])
a_centered_sp /= a.shape[0] - 1
# 4.
cov_matrix = np.cov(a.transpose())
if cov_matrix[0, 1] == a_centered_sp:
    print "correct"
else:
    print "incorrect"
