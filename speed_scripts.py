import time
import matplotlib as plt
import numpy as np
import random

#do nothing n times, returns time taken in ns
def loop_test(n : int) -> int:
    start_time_ns : int = time.perf_counter_ns()
    for i in range(n):
        pass
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)

#build a list of length n, returns time taken in ns
def list_build_test(n : int) -> int:
    our_list : list[int] = []
    start_time_ns : int = time.perf_counter_ns()
    for i in range(n):
        our_list.append(i)
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)

#build a set of size n, return time taken in ns
def set_build_test(n : int) -> int:
    our_set : set[int] = set()
    start_time_ns : int = time.perf_counter_ns()
    for i in range(n):
        our_set.add(i)
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)

#build a dict of size n, return time taken in ns
def dict_build_test(n : int) -> int:
    our_dict : set[int] = {}
    start_time_ns : int = time.perf_counter_ns()
    for i in range(n):
        our_dict[i] = None
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)

#test to see how quickly we can generate k random integers in range n, return time taken in ns
def random_gen_test(n : int, k : int) -> int:
    start_time_ns : int = time.perf_counter_ns()
    for i in range(k):
        random_num = random.randrange(n)
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)

#test to see how quickly we can lookup k random integers in a list of length n, return time taken in ns
def list_access_test(n : int, k : int) -> int:
    #create the list
    our_list : list[int] = []
    for i in range(n):
        our_list.append(i)
    start_time_ns : int = time.perf_counter_ns()
    for i in range(k):
        random_num = random.randrange(n)
        _ = our_list.index(random_num)
    end_time_ns : int = time.perf_counter_ns()
    return (end_time_ns-start_time_ns)