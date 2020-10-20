class GameEntry:
    

    def __init__(self, score, name):
        """
        docstring
        """
        self.score = score
        self.name = name

    def get_score(self):
        """
        docstring
        """
        return self.score

    def get_name(self):
        """
        docstring
        """
        return self.name

    def __str__(self):
        """
        docstring
        """
        return f'{self.score}, {self.name}'

class ScoreBoard:

    def __init__(self, board, n, capacity = 10):

        self.board = [None] * capacity

    

    