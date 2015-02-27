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

        self.assertEqual(self.game.score(), 18 + 8)

    def test_strike_second_frame(self):
        self._roll_many(pins=4, number=2)
        self._roll_many(pins=10, number=1)
        self._roll_many(pins=4, number=2)
        self._roll_many(pins=0, number=14)

        self.assertEqual(self.game.score(), 8 + 18 + 8)

    def test_strike_then_spare(self):
        self._roll_many(pins=10, number=1)
        self._roll_many(pins=5, number=2)
        self._roll_many(pins=3, number=2)
        self._roll_many(pins=0, number=14)

        self.assertEqual(self.game.score(), 20 + 13 + 6)

    def test_all_strikes(self):
        self._roll_many(pins=10, number=12)

        self.assertEqual(self.game.score(), 300)

    def _test_from_wiki(self):
        # 3,4,6,4,7,1,4,5,10,4,6,10,10,10,5,5,3 = 169
        # really?

        for x in [3, 4, 6, 4, 7, 1, 4, 5, 10, 4, 6, 10, 10, 10, 5, 5, 3]:
            self.game.roll(x)
            print('rolling %s' % x)

        self.assertEqual(self.game.score(), 169)
