# External libraries
import sqlite3
#
from ..data_preprocessing import img2vec

for i in range(0, 2, 1):
    print(i)
    print(captcha2char_vectors("example_captchas/0000"+str(i)+".gif"))
