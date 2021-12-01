import matplotlib.pyplot as plt
import numpy as np
import math
import scipy 

Y = []
v0 = []
v1 = []
v2 = []
v3 = []
v4 = []
v5 = []
v6 = []
v7 = []

c=[]
n = 0
f = open(r'C:\Users\edupc\Desktop\laba2-main\00.txt')
for i in f:
    n += int(i)
    c.append(int(i))
    if int(i) > 811:
        a = math.sqrt(2*(int(i) - 811)*0.14/1.2)
        if a < 4:
            a=3
        v0.append(a)

Y.append(n/100)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\10.txt')
for i in f:
    n += int(i)
    if int(i) > 811:
        a = math.sqrt(2*(int(i) - 811)*0.14/1.2)
        if a < 4:
            a=3
        v1.append(a)

Y.append(n/100)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\20.txt')
for i in f:
    n += int(i)
    if int(i) > 811:
        a = math.sqrt(2*(int(i) - 811)*0.14/1.2)
        if a < 4:
            a=3
        v2.append(a)

Y.append(n/100)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\30.txt')
for i in f:
    n += int(i)
    if int(i) > 811:
        a = math.sqrt(2*(int(i) - 811)*0.14/1.2)
        if a < 4:
            a=3
        v3.append(a)

Y.append(n/100)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\40.txt')
for i in f:
    n += int(i)
    if int(i) > 811:
        a = math.sqrt(2*(int(i) - 811)*0.14/1.2)
        if a < 4:
            a=3
        v4.append(a)

Y.append(n/100)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\50.txt')
for i in f:
    n += int(i)
    if int(i) > 811:
        a = math.sqrt(2*(int(i) - 811)*0.14/1.2)
        if a < 4:
            a=3
        v5.append(a)

Y.append(n/100)
f.close

n=0

f = open(r'C:\Users\edupc\Desktop\laba2-main\60.txt')
for i in f:
    n += int(i)
    if int(i) > 811:
        a = math.sqrt(2*(int(i) - 811)*0.14/1.2)
        if a < 4:
            a=3
        v6.append(a)

Y.append(n/100)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\70.txt')
for i in f:
    n += int(i)
    if int(i) > 811:
        a = math.sqrt(2*(int(i) - 811)*0.14/1.2)
        if a < 4:
            a=3
        v7.append(a)

f.close

q0 = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0
q6 = 0
q7 = 0

X = []
c = open(r'C:\Users\edupc\Desktop\laba2-main\x.txt')
for i in c:
    X.append(float(i))

for i in range (len(v0)):
    if v0[i] > 3:
        q0 += (v0[i]) * abs(X[i])* 0.6 * 1.2 * math.pi / 1000
for i in range (len(v1)):
    if v1[i] > 3:
        q1 += (v1[i]) * abs(X[i])* 0.6 * 1.2 * math.pi / 1000
for i in range (len(v2)):
    if v2[i] > 3:
        q2 += (v2[i]) * abs(X[i])* 0.6 * 1.2 * math.pi / 1000
for i in range (len(v3)):
    if v3[i] > 3:
        q3 += (v3[i]) * abs(X[i]-1)* 0.6 * 1.2 * math.pi / 1000
for i in range (len(v4)):
    if v4[i] > 3:
        q4 += (v4[i]-1) * abs(X[i]-0.8)* 0.6 * 1.2 * math.pi / 1000
for i in range (len(v5)):
    if v5[i] > 3:
        q5 += (v5[i]) * abs(X[i])* 0.6 * 1.2 * math.pi / 1000
for i in range (len(v6)):
    if v6[i] > 3:
        q6 += (v6[i]) * abs(X[i]-0.2)* 0.6 * 1.2 * math.pi / 1000
for i in range (len(v7)):
    if v7[i] > 3:
        q7 += (v7[i]) * abs(X[i]-2)* 0.6 * 1.2 * math.pi / 1000


fig, ax = plt.subplots(figsize=(16, 10), dpi = 100)
ax.plot(np.linspace(-30,30,len(v0)), v0, lw = 1,c = "black", label = "Q (00mm) = {:.3f} [г/с]".format(q0))
ax.plot(np.linspace(-30,30,len(v1)), v1, lw = 1, c = "green",  label = "Q (10mm) = {:.3f} [г/с]".format(q1))
ax.plot(np.linspace(-30,30,len(v2)), v2, lw = 1, c = "red", label = "Q (20mm) = {:.3f} [г/с]".format(q2))
ax.plot(np.linspace(-30,30,len(v3)), v3, lw = 1, c = "brown", label = "Q (30mm) = {:.3f} [г/с]".format(q3))
ax.plot(np.linspace(-30,30,len(v4)), v4, lw = 1, c = "orange", label = "Q (40mm) = {:.3f} [г/с]".format(q4))
ax.plot(np.linspace(-30,30,len(v5)), v5, lw = 1, c = "cyan", label = "Q (50mm) = {:.3f} [г/с]".format(q5))
ax.plot(np.linspace(-30,30,len(v6)), v6, lw = 1, c = "purple",  label = "Q (60mm) = {:.3f} [г/с]".format(q6))
ax.plot(np.linspace(-30,30,len(v7)), v7, lw = 1, c = "lime", label = "Q (70mm) = {:.3f} [г/с]".format(q7))
legend = ax.legend(loc='upper right', fontsize='medium')
plt.grid(True, which = "minor", linestyle = "--", alpha = 1)
plt.grid(True, which = "major", linestyle = "-")
plt.minorticks_on()
plt.grid(True, which = "minor", linestyle = "--", alpha = 1)
plt.xlabel("Положение трубки Пито относительно центра струи [мм]")
plt.ylabel("Скорость воздуха [м/с]")
plt.title('График скоростей')
plt.show()

A = [q0,q1,q2,q3,q4,q5,q6,q7]
B = [0,10,20,30,40,50,60,70]

plt.plot(B,A)
plt.title('График зависимости расхода от расстояния до сопла')
plt.grid(True, which = "major", linestyle = "-")
plt.ylabel("Расход Q [г/с]")
plt.xlabel("Положение трубки Пито относительно центра струи [мм]")
plt.minorticks_on()
plt.grid(True, which = "minor", linestyle = "--", alpha = 1)
plt.show()