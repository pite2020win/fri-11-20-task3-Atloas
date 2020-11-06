import logging

#Matrix. 


#Write a class that can represent any 4𝑥4 real matrix. 
#Include two functions to calculate the sum and dot product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
#Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction 
# - inversion
# - string representation 
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.

class Matrix:
  size = 4
  length = 2
  def __init__(self, contents):
    if len(contents) != 4:
      raise Exception
    self.contents = contents

  def __add__(self, other):
    returnMatrix = Matrix([0, 0, 0, 0])
    if isinstance(other, Matrix):
      for i in range(self.size):
        returnMatrix.contents[i] += self.contents[i] + other.contents[i]
    else:
      for i in range(self.size):
        returnMatrix.contents[i] += self.contents[i] + other
    return returnMatrix 

  def __str__(self):
    returnString = "\n["
    for i in range(self.length):
      for j in range(self.length):
        returnString += str(self.contents[i*self.length + j])
        if j != self.length - 1:
          returnString += ", "
        else:
          returnString += "]"
      if i != self.length - 1:
        returnString += "\n["
    return returnString


if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)
  m1 = Matrix([1, 2, 3, 4])
  m2 = Matrix([1, 2, 3, 5])
  m3 = m1 + m2
  logging.info(str(m3))