#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 06:33:03 2017

@author: ubuntu

ref:https://stackoverflow.com/questions/12357732/hsv-color-ranges-table
    https://en.wikipedia.org/wiki/Web_colors#HTML_color_names
"""

import math
import cv2

def EqualizeHist(img,
                 returntype=cv2.COLOR_YCR_CB2RGB):
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
    img2[:, :, 0] = cv2.equalizeHist(img2[:, :, 0]) 
    img = cv2.cvtColor(img2,returntype)
    return img    

def hsv2rgb((h, s, v)):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b
    
def rgb2hsv((r, g, b)):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

def checkBlue(hsv):
    if hsv[0]>180 and hsv[0] <250 and \
        hsv[1] > 0.2 and hsv[1] <= 1 and \
        hsv[2] > 0.2 and hsv[2] <= 1:
        return True
    return False

def checkYellow(hsv):
    if hsv[0]>20 and hsv[0] <60 and \
        hsv[1] > 0.2 and hsv[1] <= 1 and \
        hsv[2] > 0.2 and hsv[2] <= 1:
        return True
    return False

def skimage2opencv(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

def opencv2skimage(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)