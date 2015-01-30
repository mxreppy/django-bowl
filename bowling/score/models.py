# from django.db import models

# Create your models here.

class Game():

    def __init__(self):
        self.accumulator = []

    def roll(self, pins):
        self.accumulator.append(pins)

    def score(self):
        return sum(self.accumulator)
