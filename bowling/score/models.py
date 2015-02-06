# from django.db import models


class Game():
    def __init__(self):
        self.acc = []

    def roll(self, pins):
        self.acc.append(pins)

    def score(self):
        # return sum(self.acc)
        sum = 0

        counter = 0

        while True and counter < len(self.acc):

            # strike
            if self.acc[counter] == 10:
                sum += 10 + self.acc[counter + 1] + self.acc[counter + 2]
                counter += 1
            # spare
            elif self.acc[counter] + self.acc[counter + 1] == 10:
                sum += 10 + self.acc[counter + 2]
                counter += 2
            else:
                sum += self.acc[counter] + self.acc[counter + 1]
                counter += 2

        return sum
