# -*- coding: utf-8 -*-
# @Author: Yanqi Gu
# @Date:   2019-03-18 17:00:10
# @Last Modified by:   Yanqi Gu
# @Last Modified time: 2019-03-18 17:00:20


# Greatest Common Denominator
def gcd(a, b):
	if isinstance(a,int) != True or isinstance(b,int) != True:
		alert("Error: Input Format should be Integer")
	if a == 0:
		return b
	return gcd(b%a, a)

def is_prime(x):
	# TODO: need a more efficient implementation
	if x == 1:
		return False
	else:
		for a in range(2,x):
			if x % a == 0:
				return False
	return True

# Euler's Totient Function
# Count of numbers up to n which are relatively prime to n
# Finding phi from composite for large numbers is hard
def phi_hard(composite):
    count = 1
    for num in range(2, composite):
        if gcd(num, composite) == 1:
            count += 1
    return count

# If you know prime factors of composite, finding phi becomes easy
def phi_easy(p1, p2):
    return (p1 - 1) * (p2 - 1)