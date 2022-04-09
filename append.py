import random
import timeit
import matplotlib.pyplot as plt

mylist = []

x = random.randint(0,100)

start = timeit.default_timer()
mylist.append(x)
end = timeit.default_timer()
print("time to add a single element", end - start)

test = []
rt =[]
n = range(1000000)
for _ in n:
    x = random.randint(0,100)
    start = timeit.default_timer()
    test.append(x)
    end = timeit.default_timer()
    rt.append(end - start)
    
plt.plot(n, rt, '.', label='append running time')
plt.xlabel("index (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of append")
plt.legend(loc = "upper left")
plt.show()