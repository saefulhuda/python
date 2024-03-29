# importing the multiprocessing module
import multiprocessing
import time
import signal


on = True
def print_cube(num):
    """
    function to print cube of given num
    """
    while on:
        print("Process: {} cube".format(num))
        time.sleep(1)

def print_square(num):
    """
    function to print square of given num
    """
    while on:
        print("Process: {} square".format(num))
        time.sleep(1)

def stoping(signum, stack_frame):
    global on
    on = False

signal.signal(signal.SIGINT, stoping)

if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(1, ))
    p2 = multiprocessing.Process(target=print_cube, args=(2, ))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done!")