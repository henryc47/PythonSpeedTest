import time
import matplotlib.pyplot as plt
import numpy as np
import random

#calculate the time taken to lookup random values in different data structures
def get_lookup_times(n : int, k : int) -> tuple[np.ndarray,np.ndarray,np.ndarray]:
    list_times_ns = np.zeros(n,dtype=float)
    set_times_ns = np.zeros(n,dtype=float)
    dict_times_ns = np.zeros(n,dtype=float)
    our_list : list[int] = []
    our_set : set[int] = set()
    our_dict : dict[int,bool] = {}
    for i in range(n):
        random_list = []
        for j in range(k):
            random_list.append(random.randrange(i+1))
        our_list.append(i)
        our_set.add(i)
        our_dict[i] = False
        list_time = list_find_time_per_call(our_list,k,random_list)
        set_time = set_find_time_per_call(our_set,k,random_list)
        dict_time = dict_find_time_per_call(our_dict,k,random_list)
        list_times_ns[i] = list_time
        set_times_ns[i] = set_time
        dict_times_ns[i] = dict_time

    return list_times_ns,set_times_ns,dict_times_ns

#plot the output from get_lookup times
def plot_lookup_times(n : int, k : int) -> None:
    list_times_ns,set_times_ns,dict_times_ns = get_lookup_times(n,k)
    x_data = np.arange(n)
    #plot the data
    fig = plt.figure()
    plt.plot(x_data,list_times_ns,'b',label="list")
    plt.plot(x_data,set_times_ns,'g',label="set")
    plt.plot(x_data,dict_times_ns,'y',label="dict")
    plt.legend(loc="upper left")
    plt.xlabel("size ")
    plt.ylabel("lookup time (ns)")
    plt.show(block=False)

#determine average time taken (in ns) to find a random integer in a list, using k samples to get the average
def list_find_time_per_call(test_list : list[int],k : int,random_list : list[int]) -> float:
    start_time_ns : int = time.perf_counter_ns()
    for i in range(k):
        _ = test_list.index(random_list[i])
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)/k

#determine average time taken (in ns) to find a random integer in a set, using k samples to get the average
def set_find_time_per_call(test_set : set[int],k : int,random_list : list[int]) -> float:
    start_time_ns : int = time.perf_counter_ns()
    for i in range(k):
        _ = random_list[i] in test_set
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)/k

#determine average time taken (in ns) to find a random integer in a set, using k samples to get the average
def dict_find_time_per_call(test_dict : dict[int],k : int,random_list : list[int]) -> float:
    start_time_ns : int = time.perf_counter_ns()
    for i in range(k):
        _ = test_dict[random_list[i]]
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)/k        


