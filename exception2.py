# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:45:32 2020

@author: Sudarshan
"""

try:
    x='Hi'
    print(x)
except NameError:
    print('The variable x is not defined')
except:
    print('Some other error')
else:
    print('Everything went fine')
finally:
    print('This is the finally block')
    
x=-1
if x<0:
    raise Exception('OOPS')