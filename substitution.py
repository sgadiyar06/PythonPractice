# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:33:47 2020

@author: Sudarshan
"""


import string
dict={}
data=""
file=open("newcypher.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-4]
print('The cypher code is: ',dict)
with open("cypher.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print(data)
        print(c)
file.close()