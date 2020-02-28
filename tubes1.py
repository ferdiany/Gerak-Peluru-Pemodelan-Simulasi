# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:26:30 2020

@author: ASUS
"""
import numpy as np
import matplotlib.pyplot as plt

t = 0
x = 0
y = 0
m = 0.15
v0 = 50
print(v0)
g = -9.8
sudut = 35
sudut = (sudut/180)*3.14
D = 0.0013
timestep = 0.01

#inisiasi array
t_array = [t]
x_array = [x]
y_array = [y]

vx = v0 * np.cos(sudut)
vy = v0 * np.sin(sudut)
 
#mmempertimbangkan hambatan udara
#v = np.sqrt(np.power(vx,2)+np.power(vy,2))
#print(v)
#ax = -(D/m)*v*vx
#ay = -g-(D/m)*v*vy

def hambatanudara(t,vx,x,vy,y):
    while y >= 0:
        print(y)
        t = t + timestep
        v = np.sqrt(np.power(vx,2)+np.power(vy,2))
        ax = -(D/m)*v*vx
        ay = g-(D/m)*v*vy
        vx = vx + (ax * timestep)
        x = x + (vx * timestep)
        vy = vy + (ay * timestep)
        y = y + (vy * timestep)
        if y> 0 and x > 0:
            t_array.append(t)
            x_array.append(x)
            y_array.append(y)
        
t_array_2 = [t]
x_array_2 = [x]
y_array_2 = [y]

def tanpaudara(t,x,vy,y):
    while y >=0:
        t = t + timestep
        x = x + (vx * timestep)
        vy = vy + (g * timestep)
        y = y + (vy * timestep)
        if y > 0:
            t_array_2.append(t)
            x_array_2.append(x)
            y_array_2.append(y)

x_a = []
y_a = []

def analitik(v0,g):
    for t in t_array_2:
        x_analitik = x_array_2[0] + (vx * t)
        y_analitik = y_array_2[0] + (vy * t) + (0.5*g*t**2)
        x_a.append(x_analitik)
        y_a.append(y_analitik)
        
def validasi():
    t_total_a = (-2*v0*np.sin(sudut))/g
    t_total_n = t_array_2[-1]
    range_a = v0 * np.cos(sudut) * t_total_a
    range_n = x_array_2[-1]
    persen = (range_a / range_n)*100
    print("Waktu Total Analitik : ",t_total_a)
    print("Waktu Total Numerik",t_total_n)
    print("Jarak Analitik : ",range_a)
    print("Jarak Numerik",range_n)
    print("Persentase : ",persen,"%")
    
hambatanudara(t,vx,x,vy,y)
tanpaudara(t,x,vy,y)
analitik(v0,g)
validasi()

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, figsize=(6,10))
#plt.plot(x_array, y_array, color="blue")
plt.xlabel("x")
plt.ylabel("y")
ax1.plot(x_array,y_array, color="blue")
ax1.set(title="Hambatan Udara")
ax2.plot(x_array_2,y_array_2, color="blue")
ax2.set(title="Tanpa Hambatan Udara")
ax3.set(title="validasi")
ax3.plot(x_array_2, y_array_2, color="red")
ax3.plot(x_a, y_a, color="green")

