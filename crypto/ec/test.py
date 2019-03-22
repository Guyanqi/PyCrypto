# -*- coding: utf-8 -*-
# @Author: Yanqi Gu
# @Date:   2019-03-22 11:11:25
# @Last Modified by:   Yanqi Gu
# @Last Modified time: 2019-03-22 11:12:53

import ecdh
from curve import Curve, Point

def test_ecdh():
	curve = Curve(65, -65, 3077783)
	G = Point(1, 1, curve)

	alice = ECDH(curve, G)
	bob = ECDH(curve, G)

	alice.setSecretMultiplicand(13)
	bob.setSecretMultiplicand(79)

	# Alice -> Bob
	bob.receiveECDHMessage(
	    alice.getECDHMessage()
	)
	print("Alice -> Bob", alice.getECDHMessage())

	# Bob -> Alice
	alice.receiveECDHMessage(
	    bob.getECDHMessage()
	)
	print("Bob -> Alice", bob.getECDHMessage())

	print("Alice: K=",alice.getCommonKey())
	print("Bob: K=", bob.getCommonKey())