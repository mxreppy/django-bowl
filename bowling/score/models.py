from django.db import models

# Create your models here.

class Game():

    def __init__(self):
        self.accumulator = 0;

    def roll(self, pins):
        self.accumulator += pins

    def score(self):
        return self.accumulator
