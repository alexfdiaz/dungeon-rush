from math import *

def in_sine(x, scale = 1, shift = 0):
	return (1 - cos((x * pi) / 2)) * scale + shift

def out_sine(x, scale = 1, shift = 0):
	return (sin(x * pi) / 2) * scale + shift

def in_out_sine(x, scale = 1, shift = 0):
	return (- (cos(pi * x) - 1) / 2) * scale + shift

def in_quad(x, scale = 1, shift = 0):
	return (x ** 2) * scale + shift

def out_quad(x, scale = 1, shift = 0):
	return (1 - (1 - x) * (1 - x)) * scale + shift

def in_out_quad(x, scale = 1, shift = 0):
	if x < 0.5: return (2 * x ** 2) * scale + shift
	else: return (1 - pow(-2 * x + 2, 2) / 2) * scale + shift

def in_cubic(x, scale = 1, shift = 0): 
	return (x ** 3) * scale + shift

def out_cubic(x, scale = 1, shift = 0):
	return (1 - pow(1 - x, 3)) * scale + shift

def in_out_cubic(x, scale = 1, shift = 0):
	if x < 0.5: return (4 * x ** 3)
	else: return (1 - pow(-2 * x + 2, 3) / 2) * scale + shift

def in_quart(x, scale = 1, shift = 0): 
	return (x ** 4) * scale + shift

def out_quart(x, scale = 1, shift = 0):
	return (1 - pow(1 - x, 4)) * scale + shift

def in_out_quart(x, scale = 1, shift = 0):
	if x < 0.5: return (8 * x ** 4) * scale + shift
	else: return (1 - pow(-2 * x + 2, 4) / 2) * scale + shift

def in_quint(x, scale = 1, shift = 0):
	return (x ** 5) * scale + shift

def out_quint(x, scale = 1, shift = 0):
	return (1 - pow(1 - x, 5)) * scale + shift

def in_out_quint(x, scale = 1, shift = 0):
	if x < 0.5: return (16 * x ** 5) * scale + shift
	else: return (1 - pow(-2 * x + 2, 5) / 2) * scale + shift

def in_expo(x, scale = 1, shift = 0):
	if x == 0: return shift
	else: return (pow(2, 10 * x - 10)) * scale + shift

def out_expo(x, scale = 1, shift = 0):
	if x == 1: return scale + shift
	else: return (1 - pow(2, -10 * x)) * scale + shift

def in_out_expo(x, scale = 1, shift = 0):
	if x == 0: return shift
	elif x == 1: return scale + shift
	elif x < 0.5: return (pow(2, 20 * x - 10) / 2) * scale + shift
	else: return ((2 - pow(2, -20 * x + 10)) / 2) * scale + shift

def in_circ(x, scale = 1, shift = 0):
	return (1 - sqrt(1 - pow(x, 2))) * scale + shift

def out_circ(x, scale = 1, shift = 0):
	return (sqrt(1 - pow(x - 1, 2))) * scale + shift

def in_out_circ(x, scale = 1, shift = 0):
	if x < 0.5: return ((1 - sqrt(1 - pow(2 * x, 2))) / 2) * scale + shift
	else: return ((sqrt(1 - pow(-2 * x + 2, 2)) + 1) / 2) * scale + shift

def in_back(x, scale = 1, shift = 0):
	c1 = 1.70158
	c2 = c1 + 1
	return (c2 * x ** 3 - c1 * x ** 2) * scale + shift

def out_back(x, scale = 1, shift = 0):
	c1 = 1.70158
	c2 = c1 + 1
	return (1 + c2 * pow(x - 1, 3) + c1 * pow(x - 1, 2)) * scale + shift

def in_out_back(x, scale = 1, shift = 0):
	c1 = 1.70158
	c2 = c1 * 1.525
	if x < 0.5: return ((pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2) * scale + shift
	else: return ((pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2) * scale + shift

def in_elastic(x, scale = 1, shift = 0):
	c = (2 * pi) / 3
	if x == 0: return shift
	elif x == 1: return scale + shift
	else: return (-pow(2, 10 * x - 10) * sin((x * 10 - 10.75) * c)) * scale + shift

def out_elastic(x, scale = 1, shift = 0):
	c = (2 * pi) / 3
	if x == 0: return shift
	elif x == 1: return scale + shift
	else: return (pow(2, -10 * x) * sin((x * 10 - 0.75) * c) + 1) * scale + shift

def in_out_elastic(x, scale = 1, shift = 0):
	c = (2 * pi) / 4.5
	if x == 0: return shift
	elif x == 1: return scale + shift
	elif x < 0.5: return(-(pow(2, 20 * x - 10) * sin((20 * x - 11.125) * c)) / 2) * scale + shift
	else: return ((pow(2, -20 * x + 10) * sin((20 * x - 11.125) * c)) / 2 + 1) * scale + shift

def in_bounce(x, scale = 1, shift = 0):
	return (1 - out_bounce(1 - x)) * scale + shift

def out_bounce(x, scale = 1, shift = 0):
	n = 7.5625
	d = 2.75
	if x < 1 / d: return (n * x ** 2) * scale + shift
	elif x < 2 / d: return (n * ((x - 1.5) / d) * x + 0.75) * scale + shift
	elif x < 2.5 / d: return (n * ((x - 2.25) / d) * x + 0.9375) * scale + shift
	else: return (n * ((x - 2.625) / d) * x + 0.984375) * scale + shift

def in_out_bounce(x, scale = 1, shift = 0):
	if x < 0.5: return ((1 - out_bounce(1 - 2 * x)) / 2) * scale + shift
	else: return ((1 + out_bounce(2 * x - 1)) / 2) * scale + shift