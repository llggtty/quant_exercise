#!/usr/bin/env python3
"""
Three players A, B, C play the following game. First, A picks a real number between 0 and 1 (both inclusive),
then B picks a number in the same range (different from A’s choice) and finally C picks a number,
also in the same range, (different from the two chosen numbers). We then pick a number in the range uniformly randomly.
Whoever’s number is closest to this random number wins the game. Assume that A, B and C all play optimally and
their sole goal is to maximise their chances of winning. Also assume that if one of them has several optimal choices,
then that player will randomly pick one of the optimal choices.

If A chooses 0, then what is the best choice for B?
What is the best choice for A?
Can you write a program to figure out the best choice for the first player when the game is played among four players?
"""
import numpy as np


