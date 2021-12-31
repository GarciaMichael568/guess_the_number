from sys import stderr, stdin
from computer import add2,guess
import sys

def testAdd():
    assert add2(2) == 3
    assert add2(4) == 5
    
#def testGuess(capsys):
    