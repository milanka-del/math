from abc import ABC, abstractmethod


class Points(ABC):
    def __init__(self):
        self.points_board = {
            # "имя пользователя": 0
                }
    def plus_points(self, user_name):
        self.points_board[user_name] += 1
    def minus_points(self, user_name):
        self.points_board[user_name] -= 1
    def get_points(self, user_name):
        return self.points_board[user_name]

    def add_player(self, user_name):
        self.points_board[user_name] = 0
    @abstractmethod
    def load(self):
        ...

    @abstractmethod
    def save(self):
        ...


