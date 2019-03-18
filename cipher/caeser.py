# -*- coding: utf-8 -*-
# @Author: Yanqi Gu
# @Date:   2019-03-18 16:30:15
# @Last Modified by:   Yanqi Gu
# @Last Modified time: 2019-03-18 16:41:17

def caeser(msg, key, flag):
	# key limitation: 1<= key <= m, m = 26.
	# The shift operation should only shift between 1-26.
	# flag: encrypt(0) or decrypt(1)
	if flag == 1:
		key = -key
	encrypted = ''
	for symbol in msg:
		if symbol.isalpha():
			num = ord(symbol)
			num += key
			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
				encrypted += chr(num)
			else:
				encrypted += symbol
	return encrypted

if __name__ == '__main__':
	msg = "I love you"
	key = 14
	flag = 1
	print(caeser(msg, key, flag))


	