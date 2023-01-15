import sys
import threading
import time


def func_2():
    f_name = sys._getframe().f_code.co_name
    print(f'-- {f_name} begin')
    time.sleep(2)
    t_10.join()  # wait
    print(f'-- {f_name} end')


def func_10():
    f_name = sys._getframe().f_code.co_name
    print(f'-- {f_name} begin')
    time.sleep(10)
    print(f'-- {f_name} end')


if __name__ == '__main__':
    t_2 = threading.Thread(target=func_2)
    t_10 = threading.Thread(target=func_10)
    t_10.start()
    t_2.start()
