
import random
import timeit
import matplotlib.pyplot as plt

def copylist(test):
    list1 = test.copy()

test1 = [1,2,3,4,5,6,7,8,9,10]
test2 = []
test3 = ['cat','bat','rat','sat','hat','mat','fat','kat','pat','tat']
test4 = [1.1424,3.5829,283.2972,29.92,9374.223,90.2837,82.27252,8.8383,2.424,98.4736]

def avgtime(test):
    time = 0
    for _ in range(100):
        start = timeit.default_timer()
        copylist(test)
        end = timeit.default_timer()
        time += (end - start)
    return time/100

print("the average running time of test 1 is: ", avgtime(test1), ' s.')

print("the average running time of test 2 is: ", avgtime(test2), ' s.')

print("the average running time of test 3 is: ", avgtime(test3), ' s.')

print("the average running time of test 4 is: ", avgtime(test4), ' s.')


# some function definition
def create_random_list(n, upper):
    # range(n) returns [0, 1, ..., n-1]
    # the function returns [rint0, rint1, ..., rint(n-1)]
    return [random.randint(0, upper) for _ in range(n)]


# plot 
ns = [10 * _ for _ in range(100)] 
# range(100) returns [0, 1, 2, ..., 99]
# ns returns [0, 10, 20, ..., 9900]
ts = []
# run 100 times to calculate average time
runs = 100
for n in ns:
    # n = 10
    arr = create_random_list(n, 100)
    total = 0
    for _ in range(runs):
      start = timeit.default_timer()
      arr.copy()
      end = timeit.default_timer()
      total += end - start
    ts.append(total / runs)

plt.plot(ns, ts, '.', label='copylist() running time')
plt.xlabel("input length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of copylist()")
plt.legend(loc = "upper left")
plt.show()