#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, turtle

class pendu(object):
    def __iter__(self):
        yield turtle.forward(50); turtle.backward(25); turtle.left(90)
        yield turtle.forward(200); turtle.left(90)
        yield turtle.forward(100); turtle.left(90)
        yield turtle.forward(20)
        yield for _ in range(18): turtle.forward(5); turtle.left(360/18)






os.system("pause")