import time
import matplotlib as plt
import numpy as np

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

