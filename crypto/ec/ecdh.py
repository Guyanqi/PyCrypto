# -*- coding: utf-8 -*-
# @Author: Yanqi Gu
# @Date:   2019-03-18 16:45:49
# @Last Modified by:   Yanqi Gu
# @Last Modified time: 2019-03-22 11:09:41
# This is the implementation of Elliptic Curve Diffie Hellman

from curve import Curve, Point


class ECDH:
    def __init__(self, curve, generatorPoint):
        self.curve = curve
        self.generatorPoint = generatorPoint
        self.secret = None
        self.ecdhmessage = None

    def setSecretMultiplicand(self, multiplicand : int):
        self.secret = multiplicand

    def receiveECDHMessage(self, ecdhmessage : Point):
        self.ecdhmessage = ecdhmessage

    def getECDHMessage(self) -> Point:
        return self.secret*self.generatorPoint

    def getCommonKey(self) -> Point:
        return self.secret*self.ecdhmessage

# Usage Example
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