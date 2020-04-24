#!/usr/bin/python3

def intersect(a,b):
	inter = list(set(a)&set(b))
	print(inter)
def union(a,b):
	uni = list(set(a)|set(b))
	print(uni)
if __name__== '__main__':
	print("union and intersection")
