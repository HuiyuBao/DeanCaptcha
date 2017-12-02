# External libraries
import sqlite3
import base64
#
from data_preprocessing import img2vec
import show_char

def array2string(array):
    string = ""
    for char in array:
        string += str(char)
    return string

def array2b64(array):
    string = ""
    for char in array:
        string += str(char)
    int_rep = int(string,2)
    bytes_rep = int_rep.to_bytes(15, byteorder='big', signed=False)
    b64 = str(base64.b64encode(bytes_rep))
    return b64[2:-1]
def b642array(b64):
    byte_rep = base64.b64decode(b64)
    int_rep = int.from_bytes(byte_rep, byteorder='big', signed=False)
    string_rep = bin(int_rep)
    real_string_rep = string_rep[2:].zfill(120)
    array = list()
    for char in real_string_rep:
        if char == "1":
            array.append(1)
        elif char == "0":
            array.append(0)
    return array

def show_captcha(id):
    conn = sqlite3.connect(database="training_data.db")
    cursor = conn.cursor()
    id = int(id)
    if id < 0 or id > 10000:
        return
    Id = id,

    cursor.execute('SELECT vec1,vec2,vec3,vec4 FROM captchas WHERE id=?', Id)
    infos = cursor.fetchone()
    conn.close()
    captcha_img = list()
    for i in range(0,4,1):
        captcha_img.append(b642array(infos[i]))
    show_char.show_char(captcha_img)

#ALTER TABLE table_name ADD column_name datatype --add column
conn = sqlite3.connect(database="training_data.db")
cursor = conn.cursor()
for i in range(0, 10, 1):
    print(i)
    array_list = img2vec.captcha2char_vectors("example_captchas/"+str(i).zfill(5)+".gif", False)
    info = (i,array2b64(array_list[0]),array2b64(array_list[1]),array2b64(array_list[2]),array2b64(array_list[3]), 0)
    cursor.execute('INSERT INTO captchas (id, vec1, vec2, vec3, vec4,is_verified) VALUES (?,?,?,?,?,?)',info)
conn.commit()
conn.close()
