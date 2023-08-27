#!/usr/bin/env python3

class Dog:
    def bark(self):
        print("Woof!")

def test_is_method():
    '''is an instance method'''
    fido = Dog()
    assert type(fido.bark) == types.MethodType

import types


