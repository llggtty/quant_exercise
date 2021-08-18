#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 20:56:43 2018

@author: annhuang

Given a square matrix MxM, which contains only entries of either 0 or 1, 
find out whether the entries of 1 form a circle or an unrecognizable shape. 
It is up to you to decide where exactly the boundary between “circles” and “unrecognizable shapes” is. 
If it’s a circle also calculate the coordinates of the center and its radius. 
Otherwise calculate only the center of mass of all ones.

"""
import numpy as np
n=10
np.zeros((n,n),dtype = int)

def make_circle(n):
     """
     :param n:
     :return:
     """