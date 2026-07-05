class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):

    def numbers_of_wins(self):
        return f'Футбольных побед: {self.victories}'

    def numbers_of_draws(self):
        return f'Футбольных ничьих: {self.draws}'

    def numbers_of_losses(self):
        return f'Футбольных поражений: {self.losses}'

    def total_points(self):
        return f'Общее количество очков: {3 * self.victories + self.draws}'


class Hockey(Results):

    def numbers_of_wins(self):
        return f'Хоккейных побед: {self.victories}'

    def numbers_of_draws(self):
        return f'Хоккейных ничьих: {self.draws}'

    def numbers_of_losses(self):
        return f'Хоккейных поражений: {self.losses}'

    def total_points(self):
        return f'Общее количество очков: {2 * self.victories + self.draws}'


football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)


for obj in [football_team, hockey_team]:
    print(obj.numbers_of_wins())
    print(obj.numbers_of_draws())
    print(obj.numbers_of_losses())
    print(obj.total_points())

