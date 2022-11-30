#implement multiple recursive generators
# x_{n+1} = (a_1*x_n + a_2*x_{n-1} + ... + a_k*x_{n-k+1} + c) mod m
# Using Linear method to generate the first 10 values of the sequence
x_0 = 1000
a = 7 ** 5
c = 0
m = 2**31 - 1
Xtarray = [x_0]
UtArray = [x_0/m]
for i in range(0,999):
    x_0 = (a*x_0 + c) % m
    Xtarray.append(x_0)
    UtArray.append(x_0/m)

# Using the first 10 values to generate the next 1000 values
# define a array with 1000 elements as 7 **5
a = [7 ** 5] * 1000
m = 2**31 - 1

for t in range(1001,2001):
    sum = 0
    for i in range(0,1000):
        sum = sum + a[i] * Xtarray[t-i-2]
    x_0 = (sum) % m
    Xtarray.append(x_0)
    UtArray.append(x_0/m)

print("xt array:",Xtarray)
print("Ut array:",UtArray)


#plot histogram
import matplotlib.pyplot as plt
plt.hist(UtArray)
plt.show()