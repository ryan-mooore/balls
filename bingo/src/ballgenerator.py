from os import path
import csv
import random


# represents a ball that has a number and a bingo code
# associated with it (from the bingo_condes csv file)
class BingoBall:
    def __init__(self, ball, code=None):
        self.value = ball
        self.code = code


# bingo ball generator class
class BallGenerator:
    def __init__(self, limits):
        (self.lower_limit, self.upper_limit) = limits

    # load in bingo codes from a csv file
    def set_codes_path(self, g_path):
        # intelligently join and create path to file
        self.codes_path = path.normpath(
            path.join(path.dirname(__file__), g_path)
        )

        # open csv file and create new DictReader
        with open(self.codes_path) as csvfile:
            self.reader = csv.DictReader(csvfile)

            # create a tuple containing every code in the csv file
            self.bingo_codes = tuple([line["code"] for line in self.reader])

    # actual generator function
    def generate(self, picked_balls):

        # create a list of the available balls in the limit
        balls = list(range(self.lower_limit, self.upper_limit + 1))
        # sample them
        sample = random.sample(balls, picked_balls)
        for ball in sample:
            try:
                # try to yield the bingo code with the ball number
                yield BingoBall(ball, self.bingo_codes[int(ball) - 1])
            except Exception:
                # if no codes have been set just return the ball number
                yield BingoBall(ball)
