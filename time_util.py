import time


def get_now_time_str():
    now_time_str = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    return now_time_str