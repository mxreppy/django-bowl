from django.test import TestCase

from score.models import Game as Kevin

class BowlingTest(TestCase):
    def setUp(self):
        pass

    def test_gutter_game(self):
        game = Kevin()
        for i in range(20):
            game.roll(0)

        self.assertEqual(game.score(), 0)
