

def live(program, on = 'TV', time = '00.00 WIB'): # on = set argument and keyword argument
	print('This is program:', program, 'on:', on, 'that live at:', time)

live('Talkshow', time = '12.00 WIB')
live('Pramboss', 'Radio', time = '11.00 WIB')


def stream(program, *args, **kwargs): # set all input argument and keyword argument
	print('Currently we on live streaming on program:', program)
	for arg in args:
		print('-', arg)

	for kwarg in kwargs:
		print(kwarg, ':' , kwargs[kwarg])

stream('Roadshow NET 7.0', 'Please watching now ..', 'Dont miss it ..', on = 'NET TV', at = '12.00 WIB', live_in = 'Jakarta, Indonesia', gate = 'Coldplay, Marshmello, Justin Bieber')


def concat(*string, set = '-'):
	print(set.join(string))

concat('Live', 'on', 'NET TV', 'Exclusive')
concat('Live', 'on', 'NET TV', 'Exclusive', set = '-|-')