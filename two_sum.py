import time

def log_time(function):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print('function: {}, time : {}'.format(function.__name__, end_time-start_time))
        return result
    return wrapper_fn

@log_time
def hash_table(num_arr, pair_sum):
    hash_table = {}
    for _, num in enumerate(num_arr):
        complement = pair_sum - num
        if complement in hash_table:
            print(num, complement)
        hash_table[num] = num

@log_time
def bruce_force(num_arr, pair_sum):
    for i, num in enumerate(num_arr):
        for j, n_num in enumerate(num_arr):
            if num + n_num == pair_sum:
                print(num, n_num)
                break
        



num_arr = [9,4,5,1,8,2,6,7,3,0]
pair_sum = 9

hash_table(num_arr, pair_sum)
bruce_force(num_arr, pair_sum)
