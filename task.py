import logging


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