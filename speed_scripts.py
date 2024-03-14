import time
import matplotlib.pyplot as plt
import numpy as np
import random

def get_lookup_times(n : int, k : int) -> tuple[np.ndarray,np.ndarray,np.ndarray,np.ndarray]:
    random_times_ns = np.zeros(n,dtype=float)
    list_times_ns = np.zeros(n,dtype=float)
    set_times_ns = np.zeros(n,dtype=float)
    dict_times_ns = np.zeros(n,dtype=float)
    our_list : list[int] = []
    our_set : set[int] = set()
    our_dict : dict[int,bool] = {}
    for i in range(n):
        our_list.append(i)
        our_set.add(i)
        our_dict[i] = False
        random_time = random_find_time_per_call(our_list,k)
        list_time = list_find_time_per_call(our_list,k)
        set_time = set_find_time_per_call(our_set,k)
        dict_time = dict_find_time_per_call(our_dict,k)
        random_times_ns[i] = random_time
        list_times_ns[i] = list_time
        set_times_ns[i] = set_time
        dict_times_ns[i] = dict_time

    return random_times_ns,list_times_ns,set_times_ns,dict_times_ns

def plot_lookup_times(n : int, k : int) -> None:
    random_times_ns,list_times_ns,set_times_ns,dict_times_ns = get_lookup_times(n,k)
    x_data = np.arange(n)
    #plot the data
    fig = plt.figure()
    plt.plot(x_data,random_times_ns,'r',label="random")
    plt.plot(x_data,list_times_ns,'b',label="list")
    plt.plot(x_data,set_times_ns,'g',label="set")
    plt.plot(x_data,dict_times_ns,'y',label="dict")
    plt.legend(loc="upper right")
    plt.xlabel("size ")
    plt.ylabel("lookup time (ns)")
    plt.show(block=False)

#determine average time taken (in ns) to generate a random integer in a list, using k samples to get the average
def random_find_time_per_call(test_list : list[int],k : int) -> float:
    list_length = len(test_list)
    start_time_ns : int = time.perf_counter_ns()
    for i in range(k):
        random_num = random.randrange(list_length)
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)/k

#determine average time taken (in ns) to find a random integer in a list, using k samples to get the average
def list_find_time_per_call(test_list : list[int],k : int) -> float:
    list_length = len(test_list)
    start_time_ns : int = time.perf_counter_ns()
    for i in range(k):
        random_num = random.randrange(list_length)
        _ = test_list.index(random_num)
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)/k

#determine average time taken (in ns) to find a random integer in a set, using k samples to get the average
def set_find_time_per_call(test_set : set[int],k : int) -> float:
    set_size = len(test_set)
    start_time_ns : int = time.perf_counter_ns()
    for i in range(k):
        random_num = random.randrange(set_size)
        _ = random_num in test_set
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)/k

#determine average time taken (in ns) to find a random integer in a set, using k samples to get the average
def dict_find_time_per_call(test_dict : dict[int],k : int) -> float:
    set_size = len(test_dict)
    start_time_ns : int = time.perf_counter_ns()
    for i in range(k):
        random_num = random.randrange(set_size)
        _ = test_dict[random_num]
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)/k        


