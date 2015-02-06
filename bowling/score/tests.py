from django.test import TestCase

from score.models import Game


class BowlingTest(TestCase):
    def setUp(self):
        self.game = Game()

    def _roll_many(self, pins, number=20):
        for i in range(number):
            self.game.roll(pins)

    def test_gutter_game(self):
        self._roll_many(0)

        self.assertEqual(self.game.score(), 0)

    def test_single_pins2(self):
        self._roll_many(number=20, pins=1)

        self.assertEqual(self.game.score(), 20)

    def test_3s(self):
        self._roll_many(number=10, pins=3)
        self._roll_many(number=10, pins=4)

        self.assertEqual(self.game.score(), 70)

    def test_spare(self):
        self._roll_many(5, number=3)
        self._roll_many(pins=0, number=17)
        # 5 --> 5
        # 5 --> spare (undefined or 10?)
        # 5 --> spare worth 15, total 20
        # runme

        self.assertEqual(self.game.score(), 20)

    def test_spare_two(self):
        self._roll_many(pins=5, number=3)
        self._roll_many(pins=0, number=1)
        self._roll_many(pins=5, number=3)
        self._roll_many(pins=0, number=13)

        self.assertEqual(self.game.score(), 40)

    def test_strike(self):
        self._roll_many(pins=10, number=1)
        self._roll_many(pins=4, number=2)
        self._roll_many(pins=0, number=16)

        self.assertEqual(self.game.score(), 18+8)

