from nose.tools import istest
from unittest import TestCase

from refactoring.refactoring.decomposeconditional import OfferFinder


class OfferFinderTest(TestCase):
    @istest
    def finds_videogame_for_user(self):
        finder = OfferFinder()

        user = {
            'likes_sports': False,
            'belly_size': 'big',
            'tshirt_size': 'big',
        }
        offers = finder.find_for(user)

        self.assertEqual(offers, ['Videogame console'])

    @istest
    def finds_football_tshirt_for_user(self):
        finder = OfferFinder()

        user = {
            'likes_sports': True,
            'belly_size': 'big',
            'tshirt_size': 'medium',
        }
        offers = finder.find_for(user)

        self.assertEqual(offers, ['Football t-shirt'])
