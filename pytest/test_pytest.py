from sys import stderr, stdin, stdout
from computer_and_user import guess
import sys
import io

    
def testGuess(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('1'))
    guess(1)
    stdout , stderr = capsys.readouterr()
    assert stdout == 'Guess a number between 1 and 1: WINNER WINNER CHICKEN DINNER! You have guessed the number 1.\n'