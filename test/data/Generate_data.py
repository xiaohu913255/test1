# File and Code Templates
import numpy as np
from functools import wraps
import time

def generate_data(h,w):
    _vs = (-1,2,-1)
    _i = -1 #偏移量基数
    example_data = np.zeros([h,w],dtype=np.int32)
    for i in range(3):
        example_data_mask = np.eye(h,w,_i+i,dtype=np.bool_)
        example_data[example_data_mask ==True] = _vs[i]
    return example_data

a = generate_data(5,5)
print(a)