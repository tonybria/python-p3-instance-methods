#!/usr/bin/env python3

from person import Person

import io
import sys
import types

class Person:
    def walk(self):
        print("The person is walking.")

def test_prints_the_person_is_walking():
    '''prints "The person is walking."'''
    guido = Person()
    captured_out = io.StringIO()
    sys.stdout = captured_out
    guido.walk()
    sys.stdout = sys.__stdout__  # Reset the standard output
    assert captured_out.getvalue().strip() == "The person is walking."

class TestTalk:
    '''Person.talk() in person.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person()
        assert(type(guido.talk) == types.MethodType)

    def test_prints_hello_world(self):
        '''prints "Hello World!"'''
        guido = Person()
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.talk()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello World!\n")

class Person:
    def walk(self):
        print("The person is walking.")
    
    def talk(self):
        print("Hello World!")

def test_prints_hello_world():
    '''prints "Hello World!"'''
    guido = Person()
    captured_out = io.StringIO()
    sys.stdout = captured_out
    guido.talk()
    sys.stdout = sys.__stdout__  # Reset the standard output
    assert captured_out.getvalue().strip() == "Hello World!"

