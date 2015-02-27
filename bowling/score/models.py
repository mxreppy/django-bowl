# from django.db import models


class Game():
    def __init__(self):
        self.acc = []

    def roll(self, pins):
        self.acc.append(pins)

    def score(self):
        # return sum(self.acc)
        _sum = 0

        counter = 0

        frames = 0

        while True and frames <= 10 and counter < len(self.acc):

            # strike
            if self.acc[counter] == 10:
                _sum += 10 + self.acc[counter + 1] + self.acc[counter + 2]
                counter += 1
            # spare
            elif self.acc[counter] + self.acc[counter + 1] == 10:
                _sum += 10 + self.acc[counter + 2]
                counter += 2
            else:
                _sum += self.acc[counter] + self.acc[counter + 1]
                counter += 2

            frames += 1

        return _sum
