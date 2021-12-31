from sys import stderr, stdin, stdout
from computer import add2,guess
import sys
import io

def testAdd():
    assert add2(2) == 3
    assert add2(4) == 5
    
def testGuess(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('1'))
    guess(1)
    stdout , stderr = capsys.readouterr()
    assert stdout == 'Guess a number between 1 and 1: WINNER WINNER CHICKEN DINNER! You have guessed the number 1.\n'