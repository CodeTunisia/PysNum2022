#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 01:21:05 2022
Fresnel
@author: ahmed
"""
#a)
# Importation
import numpy as np

def ff1(x):
    S = 0
    for i in range(12):
        fn = (8 / np.pi)**(i + 0.5) * dn[i]
        S += fn * x**(-2 * i - 1)
    return S

def gg1(x):
    S = 0
    for i in range(12):
        gn = (8 / np.pi)**(i + 0.5) * cn[i]
        S += gn * x**(-2 * i - 1)
    return S

def ff2(x):
    S = 0
    for i in range(12):
        fn = (np.pi / 8)**(i + 0.5) * bn[i]
        S += fn * x**(2 * i + 1)
    return S

def gg2(x):

    S = 0
    for i in range(12):
        gn = (np.pi/8)**(i + 0.5) * an[i]
        S +=  gn * x**(2 * i + 1)
    return S
# b)
def C(x):
    CF=[]
    for i in range(len(x)):
        if x[i] >= np.sqrt(8/np.pi):
            cf=0.5 + np.cos((np.pi*x[i]**2)/2)*gg1(x[i]) + np.sin((np.pi*x[i]**2)/2)*ff1(x[i])
            CF.append(cf)
        elif 0 <= x[i] < np.sqrt(8/np.pi):
            cf = np.cos((np.pi*x[i]**2)/2)*gg2(x[i]) + np.sin((np.pi*x[i]**2)/2)*ff2(x[i])
            CF.append(cf)
    return CF
def S(x):
    SF=[]
    for i in range(len(x)):
        if x[i] >= np.sqrt(8/np.pi):
            sf = 0.5 - np.cos((np.pi*x[i]**2)/2)*ff1(x[i]) + np.sin((np.pi*x[i]**2)/2)*gg1(x[i])
            SF.append(sf)
        elif 0 <= x[i] < np.sqrt(8/np.pi):
            sf = -np.cos((np.pi*x[i]**2)/2)*ff2(x[i]) + np.sin((np.pi*x[i]**2)/2)*gg2(x[i])
            SF.append(sf)
    return SF
#c)
an, bn, cn, dn = np.loadtxt('coef.dat', comments='#', usecols=(0, 1, 2, 3), unpack=True)
#d)
x = np.linspace(0,10, 500)
#e)
CF = np.array(C(x)); SF = np.array(S(x))
#f)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(x, CF,'b', x, SF,'r', linewidth=2)
plt.xlabel("x", fontweight='bold'); plt.ylabel("C(x) / S(x)", fontweight='bold')
plt.title(u"Intégrales de Fresnel", fontsize=14, fontweight='bold')
plt.legend(["C(x)","S(x)"])
plt.subplot(1,2,2)
plt.plot(CF, SF, linewidth = 2, color = 'k')
plt.xlabel("C(x)", fontweight='bold'); plt.ylabel("S(x)", fontweight='bold')
plt.title("Spirale de Cornu", fontsize=14, fontweight='bold')

plt.savefig("fresnel.png")
plt.show()