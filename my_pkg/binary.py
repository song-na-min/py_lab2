#!/usr/bin/python3

def binary(num):
	d_num=0
	b_str=str(num)
	for i,digit in enumerate(b_str):
		d_num+=int(digit)*pow(2,len(b_str)-1-i)
	o_num=oct(d_num)
	h_num=hex(d_num)
	print("oct>",o_num)
	print("dec>",d_num)
	print("hex>",h_num)

if __name__== '__main__':
	print(" :")
