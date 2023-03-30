import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    self.balls = balls
    self.contents = []
    for color, count in balls.items():
      for i in range(count):
        self.contents.append(color)

  def draw(self, num_balls):
    if len(self.contents) < num_balls:
      return self.contents
    else:
      li = []
      for i in range(num_balls):
        random_ball = random.choice(self.contents)
        li.append(random_ball)
        self.contents.remove(random_ball)
      return li

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  occurences = 0

  for i in range(num_experiments):
    my_hat = copy.deepcopy(hat)
    random_balls = my_hat.draw(num_balls_drawn)
    di = {}
    for color in (random_balls):
      if color in di:
        di[color] += 1
      else:
        di[color] = 1

    match = True
    for key in expected_balls.keys():
      if random_balls.count(key) < expected_balls[key]:
        match = False
        break
    if match:
      occurences += 1

  return occurences/num_experiments #probability
  