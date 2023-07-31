import random, copy
from collections import Counter


class Hat:
  def __init__(self, **kwargs):
    self.contents = list(Counter(kwargs).elements())
    self.drawn = []

  def draw(self, nDraw):
    if nDraw > len(self.contents):
      return self.contents
    for i in range(nDraw):
      self.drawn.append(self.contents.pop(
        random.randrange(len(self.contents))))
    return self.drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # convert target to list obj
  target = list(Counter(expected_balls).elements())
  winCount = 0
  for i in range(num_experiments):
    hatCopy = copy.deepcopy(hat)
    if Counter(hatCopy.draw(num_balls_drawn)) >= Counter(target):
      winCount += 1
  return winCount / num_experiments
