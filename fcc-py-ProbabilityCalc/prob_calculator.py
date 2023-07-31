import random, copy
from collections import Counter


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.contents.extend(k for i in range(v))
    self.drawn = []

  def draw(self, nDraw):
    if nDraw > len(self.contents):
      return self.contents
    for i in range(nDraw):
      self.drawn.append(self.contents.pop(
        random.randrange(len(self.contents))))
    return self.drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # transform target into list
  exball = []
  for k, v in expected_balls.items():
    exball.extend(k for i in range(v))
  # use deepcopy to draw and reset
  winCount = 0
  for i in range(num_experiments):
    hatCopy = copy.deepcopy(hat)
    if Counter(hatCopy.draw(num_balls_drawn)) >= Counter(exball):
      winCount += 1
  return winCount / num_experiments
