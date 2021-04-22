import copy
import random


class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.contents.extend([k]*v)

  def draw(self, n):
    if n > len(self.contents):
      return self.contents
    else:
      drawn = []
      for times in range(n):
        rand_idx = random.randrange(len(self.contents))
        drawn.append(self.contents.pop(rand_idx))

      return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for experiment in range(num_experiments):
    exp_copy = copy.deepcopy(hat)
    repeat = exp_copy.draw(num_balls_drawn)
    #print (repeat)
    for k, v in expected_balls.items():
      if repeat.count(k) >= v:
        f = True
      else:
        f = False
        break
    if f is True:
      success = success + 1


  probability = success/num_experiments
  return probability
