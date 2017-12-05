import json
from data_preprocessing import img2vec

def diff_value(char_vector,key):
    ans = 0
    for i in range(120):
        if char_vector[i] != key[i]:
            ans = ans + 1
    return ans
'''
char_vector is an array of 120 characters which is either '0' or '1'
key is a key of one json object in injson
calculate the numbers of differences between char_vector and key
'''

def char2index(ch):
    if ch >= '0' && ch <= '9':
        return ch - '0'
    else:
        return ch - 'A' + 10

def index2char(ind):
    if ind <= 9:
        return ind + '0'
    else:
        return ind - 10 + 'A'
'''
establish a map between a char and an index
'0'-'9' to 0-9
'A'-'Z' to 10-35
'''

def knn (file_path):
    with open('test.txt','r') as fr:
        injson = json.load(fr)
    '''
    input test.txt as known data
    injson is json format
    '''
    for i in injson.keys():
        print(i,injson[i])

    char_vectors = img2vec.captcha2char_vectors(file_path,False)
    '''
    assume char_vectors has four elements
    every element is an array with 120 characters which is either '0' or '1'
    '''

    k = 20
    '''
    k represents we will get the top k records that have the least differences
    '''
    answer = list()
    for i in range(4):
        pair_diff_chara = list()
        for j in injson.keys():
            diff = diff_value(char_vectors[i],j)
            pair_diff_chara.append(diff,char2index(injson[j]))
        list.sort(pair_diff_chara)
        rec = list()
        for p in range(36):
            rec.append(0)
        for p in range(0,k,1):
            rec[pair_diff_chara[p][1]] = rec[pair_diff_chara[p][1]] + 1
        Max, maxi = 0, 0
        for p in range(36):
            if rec[p] > Max :
                Max = rec[p]
                maxi = p
        answer.append(index2char(maxi))
    print(answer)
    '''
    answer reserves the answer of knn algorithm
    answer has four elements
    '''
