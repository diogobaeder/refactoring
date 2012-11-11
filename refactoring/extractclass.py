# -*- coding: utf-8 -*-
class UserRepository(object):
    def __init__(self):
        self._fake_database = []

    def find_active_users(self):
        active_users_data = self._find_in_database('active', True)
        return [User(user['name'], True) for user in active_users_data]

    def insert_users(self, users):
        self._fake_database.extend(users)

    def _find_in_database(self, constraint, value):
        # Vamos fingir que isto é uma query real em banco
        return [user for user in self._fake_database
                if user[constraint] == value]


class User(object):
    def __init__(self, name, active):
        self.name = name
        self.active = active
