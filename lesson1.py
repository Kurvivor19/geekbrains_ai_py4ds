__author__ = 'Ivan Truskov'

# Numpy part
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
    print "Covariance correct"
else:
    print "Convariance incorrect"

# pandas part
# 1.
import pandas as pd
authors = pd.DataFrame(data={'author_id': [1, 2, 3],
                             'author_name': ['Тургенев', 'Чехов', 'Островский']})
book = pd.DataFrame(data={'author_id': [1, 1, 1, 2, 2, 3, 3],
                          'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                          'price': [450, 300, 350, 500, 450, 370, 290]})
# 2.
authors_price = authors.join(book.set_index('author_id'), on='author_id')
# 3.
top5 = authors_price.sort_values('price', ascending=False).head(5)
# 4.
author_stat = authors_price.groupby('author_name').agg({'price': [np.min, np.max, np.mean]})
author_stat.columns = ['min_price', 'max_price', 'mean_price']
author_stat.reset_index()
# 5.
authors_price = authors_price.assign(cover=['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'])
# 6.
book_info = pd.pivot_table(authors_price, index='author_name', values='price', columns=['cover'], aggfunc=np.sum, fill_value=0)
# 7.
book_info.to_pickle('book_info.pkl')
book_info2 = pd.read_pickle('book_info.pkl')
if book_info.equals(book_info2):
    print "Data frames are same"
else:
    print "Data frames are not same"
