import matplotlib.pyplot as plt
import numpy as np

Y = []


n = 0
f = open(r'C:\Users\edupc\Desktop\laba2-main\00.txt')
for i in f:
    n += int(i)

Y.append(n/500)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\10.txt')
for i in f:
    n += int(i)

Y.append(n/500)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\20.txt')
for i in f:
    n += int(i)

Y.append(n/500)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\30.txt')
for i in f:
    n += int(i)

Y.append(n/500)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\40.txt')
for i in f:
    n += int(i)

Y.append(n/500)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\50.txt')
for i in f:
    n += int(i)

Y.append(n/500)
f.close

n=0

f = open(r'C:\Users\edupc\Desktop\laba2-main\60.txt')
for i in f:
    n += int(i)

Y.append(n/500)
f.close

n=0
f = open(r'C:\Users\edupc\Desktop\laba2-main\70.txt')
for i in f:
    n += int(i)

Y.append(n/500)
f.close


X = np.array([0,10,20,30,40,50,60,70])
a = np.polyfit(X,Y,5)
n = np.linspace(0, 70, 1000, True)
yn = a[0]*n**5 + a[1]*n**4 + a[2]*n**3 + a[3]*n**2 + a[4]*n + a[5]

plt.plot(n,yn)
plt.scatter(X,Y)
plt.set_title('График каллибровки по расстоянию', style='italic')
plt.ylabel('Показания АЦП')
plt.xlabel('Длина [мм]')
plt.show()
