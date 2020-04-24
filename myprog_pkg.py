#!/usr/bin/python3

import my_pkg

def print_menu():
	print("1.conversion")
	print("2.union/intersection")
	print("3.exit")
	menu = input("메뉴선택: ")
	return int(menu)

if __name__== '__main__':
	while True:
		menu=print_menu()
		if menu == 1:
			num=input("input binary number:")
			my_pkg.binary(num)
		elif menu == 2:
			list_string1=input("input 1st list:")
			list_num1=list_string1.split(',')
			list_string2 = input("input 2nd list:")
			list_num2=list_string2.split(',')
			print("intersection : ")
			my_pkg.intersect(list_num1,list_num2)
			print("union:")
			my_pkg.union(list_num1,list_num2)
		elif menu == 3:
			break	

