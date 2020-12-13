import math
import os
import random
import re
import sys
import unittest

'''
THE PROBLEM

Given a square chess board with one queen (who can move in any direction), determine how many square the queen can attack (move to).
The cols of the board start at 1 on the bottom left most side and increment as you go to the left
The row of the board start at 1 on the bottom left most side and increment as you go to the up

INPUT TYPE
n k 
r c
k k
. .
. .
. .

The first line: two space separated intergers. n = lenght of board k = the number of obstacles 
The second line: the initial locaiton of the queen (r,c) (row, col)

OUTPUT
This alogrithm will output the max amount of places the queen can move to (attack) with out encountering obstacles
'''

def queensAttack(n, k, r_q, c_q, obstacles):
    #define the max distance the queen can move (up, down, left, right, right/up, right/own, left/up, left/down)
    #bounded by the size fo the given board
    up = n - r_q
    down = r_q-1
    right = n - c_q
    left = c_q-1
    rightUp = min(up, right)
    rightDown = min(right,down)
    leftUp = min(left,up)
    leftDown = min(left,down)

    # Traverse through the given obstacles
    # the loop will check for obsticles in all directions of the queen
    # if there is an obstacle the distance the queen can travel in that respective direction becomes limited to the 
    # the distance from the queen to the located obstacle. 
    # The max amount that can be travled in that direction is then updated.

    for o in obstacles:
        #checks up and down if there is an obstacle in the same column as the queen
        if o[1] == c_q:
            #once obstacle is found (up or down) update the max distance that the queen can travel up or down
            if o[0] < r_q:
                down = min(down, r_q-1-o[0])
            else:
                up = min(up, o[0]-r_q-1)
        #checks left and right if there is an obsticle in the same row as the queen 
        elif o[0] == r_q:
            #once obstacle is found to the left or right update the max distance that the queen can travel left or right
            if o[1] < c_q: 
                left = min(left, c_q-1-o[1])
            else: 
                right = min(right, o[1]-c_q-1)
        #checks all the diagonals if there is an obsticle in the same row as the queen 
        elif abs(o[0]-r_q) == abs(o[1]-c_q): 
            #once obstacle is found on the disgonal paths update the max distance that the queen can travel accordingly
            if o[1]>c_q:
                if o[0]>r_q: 
                    rightUp = min(rightUp, o[1]-c_q-1)
                else: 
                    rightDown = min(rightDown, o[1]-c_q-1)
            else:
                if o[0]>r_q: 
                    leftUp = min(leftUp, c_q-1-o[1])
                else: 
                    leftDown = min(leftDown, c_q-1-o[1])

    #returns the remaining sum of the max distances that be travel by the queen in any given direction            
    return up + down + right + left + rightUp + rightDown + leftUp + leftDown


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    #the row the queen starts on
    r_q = int(r_qC_q[0]) 

    #the col the queen starts on
    c_q = int(r_qC_q[1])

    # to hold the location of the obsticles
    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    #get result
    result = queensAttack(n, k, r_q, c_q, obstacles)

    #print result
    print(result)
