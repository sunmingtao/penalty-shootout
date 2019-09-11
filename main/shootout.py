import random

FIRST_SCORE_PROBABILITY = 0.75
SECOND_SCORE_PROBABILITY = 2/3
PREDETERMINED_ROUND = 5

class Team:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.last_scored = False

    def shoot(self, probability):
        if random.uniform(0, 1) < probability:
            self.score += 1
            self.last_scored = True


class Rule:
    def __init__(self):
        self.round = 1
        self.team_a = Team('A')
        self.team_b = Team('B')
        self.first_team = None
        self.second_team = None

    def shoot(self):
        self.first_team.shoot(FIRST_SCORE_PROBABILITY)
        self.second_team.shoot(SECOND_SCORE_PROBABILITY)

    def winner(self):
        if self.round < PREDETERMINED_ROUND or self.team_a.score == self.team_b.score:
            return None
        elif self.team_a.score > self.team_b.score:
            return 'A'
        else:
            return 'B'

    def advance_round(self):
        self.round += 1

    def order_teams(self):
        self.set_first_team()
        self.set_second_team()

    def set_first_team(self):
        if self.first_team is None:
            self.first_team = self.team_a
        else:
            self.set_first_team_2nd_round_onwards()

    def set_second_team(self):
        assert self.first_team is not None
        self.second_team = self.team_b if self.first_team == self.team_a else self.team_a


class ClassicRule (Rule):

    def __init__(self):
        super().__init__()
        self.name = "Classic"

    def set_first_team_2nd_round_onwards(self):
        self.first_team = self.team_a


class AlternatingRule (Rule):

    def __init__(self):
        super().__init__()
        self.name = "Alternating"

    def set_first_team_2nd_round_onwards(self):
        self.first_team = self.team_a if self.first_team == self.team_b else self.team_b


class CatchUpRule (AlternatingRule):

    def __init__(self):
        super().__init__()
        self.name = "Catch Up"

    def set_first_team_2nd_round_onwards(self):
        if self.first_team.last_scored or not self.second_team.last_scored:
            super().set_first_team_2nd_round_onwards()


class AdjustedCatchUpRule (CatchUpRule):

    def __init__(self):
        super().__init__()
        self.name = "Adjusted Catch Up"

    def set_first_team_2nd_round_onwards(self):
        if self.round == PREDETERMINED_ROUND + 1:
            self.first_team = self.team_b
        else:
            super().set_first_team_2nd_round_onwards()


class Game:

    def __init__(self, rule):
        self.rule = rule

    def start_shoot_out(self):
        while True:
            self.rule.order_teams()
            self.rule.shoot()
            winner = self.rule.winner()
            if winner:
                return winner
            self.rule.advance_round()








