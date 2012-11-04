# -*- coding: utf-8 -*-
class UserRepository(object):
    def find_active_users(self):
        active_users_data = self._find_in_database('active', True)
        return [User(user['name'], True) for user in active_users_data]

    def _find_in_database(self, constraint, value):
        # Vamos fingir que isto é uma query real em banco
        fake_data = [
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
        ]
        return [user for user in fake_data if user[constraint] == value]


class User(object):
    def __init__(self, name, active):
        self.name = name
        self.active = active
