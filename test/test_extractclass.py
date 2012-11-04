from nose.tools import istest
from unittest import TestCase

from refactoring.refactoring.extractclass import UserRepository


class UserRepositoryTest(TestCase):
    @istest
    def finds_active_users(self):
        repository = UserRepository()

        users = sorted(repository.find_active_users())

        self.assertTrue(all(user.active for user in users))
