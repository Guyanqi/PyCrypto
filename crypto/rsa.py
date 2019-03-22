# -*- coding: utf-8 -*-
# @Author: Yanqi Gu
# @Date:   2019-03-18 16:45:49
# @Last Modified by:   Yanqi Gu
# @Last Modified time: 2019-03-22 10:55:45

import sys
sys.path.append('../tool')
import math_tool as tool

# Key Generation
# Use 2 prime factors to form the composite, and use phi_easy() to find the totient
# To break RSA, you would only have the composite, 
# thus would have to use phi_hard() to derive totient -> privkey.

# pubkeys are a coprime of the composite modulus
def find_pubkeys(p1, p2):
    pubkeys = []
    totient = tool.phi_easy(p1, p2)
    # start from 3, smallest prime. in practice, starts at bigger prime (65537)
    for pub in range(4, totient):
        if tool.is_prime(pub):
            pubkeys.append(pub)
    return pubkeys

# Extended Euclidean Algorithm
# privkey is modular multiplicative inverse of pubkey
def find_privkey(pubkey, p1, p2):
    composite = p1 * p2
    totient = tool.phi_easy(p1, p2)
    for priv in range(1, composite):
        if ((pubkey * priv) - 1) % totient is 0:
            return priv

def gen_keypair(p1, p2):
    keys = []
    pubkeys = find_pubkeys(p1, p2)
    for pub in pubkeys:
        priv = find_privkey(pub, p1, p2)
        if priv is not None:
            keys.append({"pub": pub, "priv": priv})
    return keys

def encrypt_char(num, pubkey, modulus):
    # multiply num by itself, pubkey times
    r = num ** pubkey
    return r % modulus

def decrypt_char(num, privkey, modulus):
    # multiply encrypted num by itself, modulus times
    r = num ** privkey
    return r % modulus

def encrypt_word(word, pubkey, modulus):
    encwd = ''
    for char in word:
        n = ord(char)
        enc = encrypt_char(n, pubkey, modulus)
        encwd += chr(enc)
    return encwd

def decrypt_word(word, privkey, modulus):
    decwd = ''
    for char in word:
        n = ord(char)
        dec = decrypt_char(n, privkey, modulus)
        decwd += chr(dec)
    return decwd


