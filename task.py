import logging
import math
import itertools


class Matrix:
  def __init__(self, contents):
    attemptedSize = len(contents)
    attemptedLength = round(math.sqrt(attemptedSize))
    if math.pow(attemptedLength, 2) != attemptedSize:
      raise Exception("Not a square matrix!")
    self.contents = contents.copy()
    self.size = attemptedSize
    self.length = attemptedLength


  @staticmethod
  def from_matrix(argument):
    return Matrix(argument.contents)


  @staticmethod
  def from_list_of_lists(argument):
    lengthsList = [len(x) for x in argument]
    lengthsSet = set(lengthsList)
    if len(lengthsSet) != 1:
      raise Exception("Not a square matrix!")
    return Matrix(list(itertools.chain.from_iterable(argument)))


  @staticmethod
  def from_list(argument):
    return Matrix(argument)


  @staticmethod
  def from_arguments(*arguments):
    return Matrix(list(arguments))


  @staticmethod
  def empty_for_size(size):
    return Matrix([0 for x in range(size)])


  def add_matrix(self, other):
    if self.size != other.size:
      raise Exception("Matrix size mismatch!")
    returnMatrix = Matrix.from_matrix(self)
    for i in range(self.size):
        returnMatrix[i] += other[i]
    return returnMatrix


  def add_number(self, other):
    returnMatrix = Matrix.from_matrix(self)
    for i in range(self.size):
        returnMatrix[i] += other
    return returnMatrix


  def __add__(self, other):
    if type(other) == Matrix:
      return self.add_matrix(other)
    elif type(other) in [int, float]:
      return self.add_number(other)
    else:
      raise Exception("Unsupported operand types!")


  def __radd__(self, other):
    return self + other


  def sub_matrix(self, other):
    if self.size != other.size:
      raise Exception("Matrix size mismatch!")
    returnMatrix = Matrix.from_matrix(self)
    for i in range(self.size):
        returnMatrix[i] -= other[i]
    return returnMatrix


  def sub_number(self, other):
    returnMatrix = Matrix.from_matrix(self)
    for i in range(self.size):
        returnMatrix[i] -= other
    return returnMatrix


  def __sub__(self, other):
    if type(other) == Matrix:
      return self.sub_matrix(other)
    elif type(other) in [int, float]:
      return self.sub_number(other)
    else:
      raise Exception("Unsupported operand types!")


  def __mul__(self, other):
    if type(other) == Matrix:
      raise Exception("Unsupported operand types!")
    returnMatrix = Matrix.from_matrix(self)
    for i in range(self.size):
        returnMatrix[i] *= other
    return returnMatrix


  def __rmul__(self, other):
    return self * other


  def __truediv__(self, other):
    returnMatrix = Matrix.from_matrix(self)
    for i in range(self.size):
        returnMatrix[i] /= other
    return returnMatrix


  def __floordiv__(self, other):
    returnMatrix = Matrix.from_matrix(self)
    for i in range(self.size):
        returnMatrix[i] //= other
    return returnMatrix


  def __matmul__(self, other):
    returnMatrix = Matrix.empty_for_size(self.size)
    for i in range(self.length):
      for j in range(self.length):
        for k in range(self.length):
          returnMatrix[i*self.length + j] += self[i*self.length + k] * other[k*self.length + j]
    return returnMatrix


  def __str__(self):
    returnString = "\n["
    for i in range(self.length):
      for j in range(self.length):
        returnString += str(self[i*self.length + j])
        if j != self.length - 1:
          returnString += ", "
        else:
          returnString += "]"
      if i != self.length - 1:
        returnString += "\n["
    return returnString


  def __getitem__(self, index):
    if not 0 <= index < self.size:
      raise IndexError
    return self.contents[index]


  def __setitem__(self, index, value):
    if not 0 <= index < self.size:
      raise IndexError
    self.contents[index] = value


  def __iter__(self):
    self.index = 0
    return self


  def __next__(self):
    if self.index < self.size:
      toReturn = self[self.index]
      self.index += 1
      return toReturn
    else:
      raise StopIteration


#TODO: Better showcase
if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)
  m1 = Matrix.from_list_of_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  m2 = Matrix.from_arguments(5, 6, 7, 8, 9, 10, 11, 12, 13)
  m3 = Matrix.empty_for_size(4)
  logging.info("m1:{}".format(str(m1)))
  logging.info("m2:{}".format(str(m2)))
  logging.info("m3:{}".format(str(m3)))
  logging.info("m1 + m2:{}".format(str(m1 + m2)))
  logging.info("5 + m3:{}".format(str(5 + m3)))
  logging.info("m1 // 3:{}".format(str(m1 // 3)))
  logging.info("m1 @ m2:{}".format(str(m1 @ m2)))
  logging.info("m1 iterated:")
  for i in m1:
    logging.info(str(i))
    
