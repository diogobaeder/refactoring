from nose.tools import istest
from unittest import TestCase

from refactoring.refactoring.extractclass import UserRepository


class UserRepositoryTest(TestCase):
    def populate_database(self, repository):
        repository.insert_users([
            {
                'name': 'Nat Pryce',
                'active': True,
            },
            {
                'name': 'Steve Freeman',
                'active': True,
            },
            {
                'name': 'Alfred Hitchcock',
                'active': False,
            },
        ])

    @istest
    def finds_active_users(self):
        repository = UserRepository()
        self.populate_database(repository)

        users = sorted(repository.find_active_users())

        self.assertEqual(len(users), 2)
        self.assertTrue(all(user.active for user in users))
