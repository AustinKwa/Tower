#  File: Tower.py

#  Description: This program manipulates the puzzle Tower of Hanoi.

#  Student's Name: Austin Kwa

#  Student's UT EID: ak38754

#  Partner's Name: N/A

#  Partner's UT EID: N/A

#  Course Name: CS 313E 

#  Unique Number: 51125

#  Date Created: 3/5/2022

#  Date Last Modified: 3/5/2022

from re import X
import sys, math

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
    if n <= 1:  # n should always return 1 because n should only be 1 when it passes the if statement
        return n
    else:
        k = round(n - math.sqrt(2 * n + 1) + 1) # calculating k value
        return num_moves(k) + three_pegs(n - k) + num_moves(k)

def three_pegs (n): #number of moves with three pegs given number of stacked disks
    if n <= 1:
        return n
    else:
        return 2*three_pegs(n - 1) + 1

def main():
  # read number of disks and print number of moves
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))

if __name__ == "__main__":
  main()

'''
def towers (n, source, spare, dest):
    if (n == 1):
        print('Move disk from', source, 'to', dest)
    else:
        towers(n - 1, source, dest, spare)
        print('Move disk from', source, 'to', dest)
        towers(n - 1, spare, source, dest)
    
def main():
    towers(5, 'A', 'B', 'C')

main()
'''