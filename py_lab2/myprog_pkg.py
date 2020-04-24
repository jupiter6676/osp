#!/usr/bin/python

import my_pkg

while True:

	print("Select menu: 1) conversion  2) union/intersection  3) exit ?")

	menu = int(input())

	if (menu == 1):

		binNum = input("inpput binary number: ")	# 10101110 (string)
		
		"""
		#decNum = int(binNum, 2)

		
		print(oct(decNum))		# 256
		print(decNum)			# 174
		print(hex(decNum))		# ae (AE)
		"""
		
		decNum = my_pkg.dec_(binNum)
		
		print("=> OCT> ", end="")
		print(my_pkg.oct_(decNum)[2:])	# [2:] - 0o

		print("=> DEC> ", end="")
		print(decNum)

		print("=> HEX> ", end="")
		print(my_pkg.hex_(decNum)[2:].upper())	# [2:] - 0x


	elif (menu == 2):
		
		set1_element = []
		set2_element = []

		set1_str = input("1st list: ")	# [ 2, 3, 5, 7, 8 ]
		set2_str = input("2nd list: ")	# [ 1,3, 5,7, 9 ]

		set1_str_list = list(set1_str)
		set2_str_list = list(set2_str)

		#print(set1_str_list)
		#print(set2_str_list)


		for i in range(0, len(set1_str_list)):

			if (set1_str_list[i] != '[') and (set1_str_list[i] != ' ') and (set1_str_list[i] != ',') and (set1_str_list[i] != ']'):

				set1_element.append(set1_str_list[i])	# str list


		for j in range(0, len(set2_str_list)):

			if (set2_str_list[j] != '[') and (set2_str_list[j] != ' ') and (set2_str_list[j] != ',') and (set2_str_list[j] != ']'):

				set2_element.append(set2_str_list[j])	# str list


		set1_element = list(map(int, set1_element))	# int list
		set2_element = list(map(int, set2_element))	# int list

		#print(set1_element)
		#print(set2_element)

		set1 = set(set1_element)
		set2 = set(set2_element)

		#print(set1)
		#print(set2)
		print("=> union: ", end="")
		print(my_pkg.union_(set1, set2))

		print("=> intersection: ", end="")
		print(my_pkg.intersection_(set1, set2))


	elif (menu == 3):

		print("Exit the program...")
		break
