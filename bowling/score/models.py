# from django.db import models


class Game():
    def __init__(self):
        self.acc = []

    def roll(self, pins):
        self.acc.append(pins)

    def score(self):
        # return self._score_procedural()
        return self._score_recursive_worker(0, self.acc)

    def _is_strike(self, list_in):
        return list_in[0] == 10

    def _is_spare(self, list_in):
        return list_in[0] + list_in[1] == 10

    def _score_recursive_worker(self, summer, list_in):
        # recursive
        # if list_in is emtpy return summer
        result = 0
        if len(list_in) == 0:
            result = summer
        elif self._is_strike(list_in):
            result = summer + list_in[0] + list_in[1] + list_in[2] + \
                     self._score_recursive_worker(summer, list_in[1:])
        elif self._is_spare(list_in):
            result = summer + list_in[0] + list_in[1] + list_in[2] + \
                     self._score_recursive_worker(summer, list_in[2:])
        else:
            result = summer + list_in[0] + list_in[1] + \
                     self._score_recursive_worker(summer, list_in[2:])

        return result

    def _score_procedural(self):
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
