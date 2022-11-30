#implement linear congruential generators
# x_{n+1} = (a*x_n + c) mod m
x_0 = 1000
a = 7 ** 1000

c = 0
m = 2**31 - 1
Xtarray = [x_0]
UtArray = [x_0/m]
for i in range(0,1000):
    x_0 = (a*Xtarray[i] + c) % m
    Xtarray.append(x_0)
    UtArray.append(x_0/m)

print("xt array:",Xtarray)
print("Ut array:",UtArray)

#plot Ut array
import matplotlib.pyplot as plt
# plt.plot(UtArray)
# plt.show()

#plot histogram
plt.hist(UtArray)
plt.show()

