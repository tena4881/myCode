"""
This problem is a python practice problem found on HackerRank.com 
This is my solution.


THE PROBLEM (From HackerRank)
    ABC is a right triangle, 90 deg at B.
    Therefore, Angle ABC = 90 deg

    Point M is the midpoint of hypotenuse AC

    You are given the lengths AB and BC.
    The task is to find angle MBC in degrees.


INPUT FORMAT
    The first line contains the length of side AB
    The second line contains the length of side BC


CONSTRINTS
    0 < AB <= 100
    0< BC <= 100
    Lengths AB and BC are natural numbers


OUTPUT FORMAT
    Angle MBC in degrees. 


"""

import math

def main():
    done = False
    while not done:
        aB = int(input("Length of AB: "))
        bC = int(input("Length of BC: "))
        if validateInput(aB) and validateInput(bC):
            res = getAngle(aB,bC)
            formatOutput(res)
            done = True
        else:
            print("Please enter values <= 100")
    

#Calculates angle MBC give sides AB and BC
def getAngle(aB,bC):
    leftSide = (aB**2) + (bC**2)
    h = math.sqrt(leftSide)
    return round(math.degrees(math.acos(bC/h))) #uses arc coside to find angle MBC

#Checks if user input is within the defined constraints
def validateInput(x):
    try:
        return int(x) <= 100
    except ValueError:
        return False

#Formats and prints the answer to console
def formatOutput(res):
    degree=chr(176)
    print("Angle MBC is: ", end = " ")                               
    print(res,degree, sep='')

if __name__ == "__main__":
    main()
