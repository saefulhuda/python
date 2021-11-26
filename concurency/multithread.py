# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import signal
import time


on = True
def print_cube(num):
    """
    function to print cube of given num
    """
    while on:
        print("Cube: {}".format(num * num * num))
        time.sleep(1)

def print_square(num):
    """
    function to print square of given num
    """
    while on:
        print("Square: {}".format(num * num))
        time.sleep(1)

def stoping(signum, stack_frame):
    global on
    on = False
    print('Stoping ..')

signal.signal(signal.SIGINT, stoping)

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
