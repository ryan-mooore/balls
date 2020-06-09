from os import path
import csv
import random

class BallGenerator:
    def __init__(self, limits):
        (self.lower_limit, self.upper_limit) = limits


    def set_codes_path(self, g_path):
        self.codes_path = path.join(path.dirname(__file__), g_path)

        with open(self.codes_path) as csvfile:
            self.reader = csv.DictReader(csvfile)
            self.bingo_codes = tuple([line["code"] for line in self.reader])

    def generate(self, picked_balls):
        balls = list(range(self.lower_limit, self.upper_limit + 1))
        sample = random.sample(balls, picked_balls)
        for ball in sample:
            try:
                yield f"{str(ball)} {self.bingo_codes[int(ball) - 1]}"
            except Exception:
                yield f"{str(ball)}"