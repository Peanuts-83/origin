#from os import *
import os

def find(path, dir):
    res = ''
    try:
        for dirpath,dirs,files in os.walk('test', topdown = False):
            for d in dirs:
                if dir in d:
                    res += dirpath.replace("\\", "/") +'/'+ dir   # \ replaced by / for windows
        print('results : ',res)
    except Exception as e:
        print('Exception raised : ', strerror(e.errno))

find('test','test3')