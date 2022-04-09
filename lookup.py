import random
import timeit
import matplotlib.pyplot as plt

test = [random.randint(0,100) for _ in range(1000000)]

start = timeit.default_timer()
value = test[10380]
end = timeit.default_timer()
print("time to look up a single index", end - start)

rt =[]
n = range(1000000)
for i in n:
    start = timeit.default_timer()
    value = test[i]
    end = timeit.default_timer()
    rt.append(end - start)
    
plt.plot(n, rt, '.', label='lookup running time')
plt.xlabel("index (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of lookup")
plt.legend(loc = "upper left")
plt.show()