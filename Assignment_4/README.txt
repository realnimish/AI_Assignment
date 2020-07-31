Task: The game of sticks using Min/Max tree with Alfa-beta pruning. Last person to remove stick loses!

Run environment: Program runs on python2

Command: python nim-game.py

Further optimisation: 
The time complexity is still exponential after Alfa-Beta pruning but we can optimise it further down to polynomial time with the help of memoization with linear space cost. Following two lines(line 12&27) needs to be updated as follows:

(Line 12) if payoff.get(n):  (convert to) if payoff.get(n)!=None:
(Line 27) if payoff.get(-n): (convert to) if payoff.get(-n)!=None: