#!/usr/bin/env python3

from dog import Dog

import io
import sys
import types

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog"'''
        fido = Dog()
        assert(type(fido) == Dog)

class Dog:
    def bark(self):
        print("Woof!")

def test_is_method():
    '''is an instance method'''
    fido = Dog()
    assert type(fido.bark) == types.MethodType

class Dog:
    def sit(self):
        print("The dog is sitting.")

def test_prints_the_dog_is_sitting():
    '''prints "The dog is sitting."'''
    fido = Dog()
    captured_out = io.StringIO()
    sys.stdout = captured_out
    fido.sit()
    sys.stdout = sys.__stdout__  # Reset the standard output
    assert captured_out.getvalue().strip() == "The dog is sitting."