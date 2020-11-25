import signal, time

count = 1

def my_custom_handler(signum, stack_frame):
	print('I have encountered the signal KILL.')
	print('CTRL+C was pressed.  Do anything here before the process exists')
	exit()

signal.signal(signal.SIGINT, my_custom_handler)

while True:
	print('Running ', count)
	count += 1
	time.sleep(1)