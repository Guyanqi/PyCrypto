# -*- coding: utf-8 -*-
# @Author: Yanqi Gu
# @Date:   2019-03-18 17:08:59
# @Last Modified by:   Yanqi Gu
# @Last Modified time: 2019-03-18 17:19:25

import sys
sys.path.append('../crypto')

import rsa

def test_rsa():
	prime1 = 13
	prime2 = 7
	# Their product is your modulus number
	modulus = prime1 * prime2
	print("Take prime numbers %d, %d make composite number to use as modulus: %d" % (prime1, prime2, modulus))
	print("RSA security depends on the difficulty of determining the prime factors of a composite number.")

	# Key generation is the most complicated part of RSA. See rsaKeyGen.py for algorithms
	print("\n*~*~*~ Key Generation *~*~*~")
	keys = rsa.gen_keypair(prime1, prime2)
	print("All possible keys:", keys)
	# We'll go with the first keypair: pub 5, priv 29
	pubkey = keys[0]['pub']
	privkey = keys[0]['priv']
	print("\nYour pubkey is %d, your privkey is %d\n" % (pubkey, privkey))

	encwd = rsa.encrypt_word('CLOUD', pubkey, modulus)
	print("Encrypted word: ", encwd)
	decwd = rsa.decrypt_word(encwd, privkey, modulus)
	print("Decrypted word: ", decwd)

def main():
	test_rsa()

if __name__ == '__main__':
	main()