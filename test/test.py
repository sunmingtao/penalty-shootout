from main import *
import unittest


class TeamTest(unittest.TestCase):

    def test_shoot(self):
        team = Team('A')
        team.shoot(0.75)
        if team.last_scored:
            self.assertEqual(team.score, 1)
        else:
            self.assertEqual(team.score, 0)


class ClassicRuleTest(unittest.TestCase):

    def setUp(self):
        self.rule = ClassicRule()

    def test_order_teams(self):
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_advance_round_first(self):
        self.rule.advance_round()
        self.assertEqual(self.rule.round, 2)

    def test_shoot(self):
        self.rule.order_teams()
        self.rule.shoot()
        self.rule.advance_round()
        self.rule.order_teams()
        self.rule.shoot()
        self.assertEqual(self.rule.first_team.name, 'A')

    def test_winner_round_less_than_5(self):
        self.rule.first = False
        self.rule.round = 4
        self.assertIsNone(self.rule.winner())

    def test_winner_round_equal_score(self):
        self.rule.first = False
        self.rule.round = 5
        self.rule.team_a.score = 4
        self.rule.team_b.score = 4
        self.assertIsNone(self.rule.winner())

    def test_winner_round_equal_a_greater_than_b(self):
        self.rule.first = False
        self.rule.round = 5
        self.rule.team_a.score = 4
        self.rule.team_b.score = 3
        self.assertEqual(self.rule.winner(), 'A')

    def test_winner_round_equal_b_greater_than_a(self):
        self.rule.first = False
        self.rule.round = 5
        self.rule.team_a.score = 3
        self.rule.team_b.score = 4
        self.assertEqual(self.rule.winner(), 'B')


class AlternatingRuleTest (unittest.TestCase):

    def setUp(self):
        self.rule = AlternatingRule()

    def test_order_teams_first_round(self):
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_order_teams_second_round(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_third_round(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_order_teams_fourth_round(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')


class CatchUpRuleTest (unittest.TestCase):

    def setUp(self):
        self.rule = CatchUpRule()

    def test_order_teams_first_round(self):
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_order_teams_second_round_both_score_in_first_round(self):
        self.rule.order_teams()
        self.rule.team_a.last_scored = True
        self.rule.team_b.last_scored = True
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_second_round_neither_score_in_first_round(self):
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = False
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_second_round_team_a_score_team_b_not_score_in_first_round(self):
        self.rule.order_teams()
        self.rule.team_a.last_scored = True
        self.rule.team_b.last_scored = False
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_second_round_team_a_not_score_team_b_score_in_first_round(self):
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = True
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_order_teams_third_round_team(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_order_teams_third_round_team_a_not_score_team_b_score_in_first_round_neither_score_in_second_round(self):
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = True
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = False
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_fifth_round_team(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_order_teams_sixth_round_team(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_sixth_round_team_team_a_not_score_team_b_score_in_fifth_round(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = True
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')


class AdjustedCatchUpRuleTest (unittest.TestCase):

    def setUp(self):
        self.rule = AdjustedCatchUpRule()

    def test_order_teams_first_round(self):
        self.rule.order_teams()
        self.rule.round = 1
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_order_teams_second_round_both_score_in_first_round(self):
        self.rule.order_teams()
        self.rule.team_a.last_scored = True
        self.rule.team_b.last_scored = True
        self.rule.round = 2
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_second_round_neither_score_in_first_round(self):
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = False
        self.rule.round = 2
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_second_round_team_a_score_team_b_not_score_in_first_round(self):
        self.rule.order_teams()
        self.rule.team_a.last_scored = True
        self.rule.team_b.last_scored = False
        self.rule.round = 2
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_second_round_team_a_not_score_team_b_score_in_first_round(self):
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = True
        self.rule.round = 2
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_order_teams_third_round_team(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.round = 3
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_order_teams_third_round_team_a_not_score_team_b_score_in_first_round_neither_score_in_second_round(self):
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = True
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = False
        self.rule.round = 3
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_fifth_round_team(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')

    def test_order_teams_sixth_round_team(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.round = 6
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_sixth_round_team_team_a_not_score_team_b_score_in_fifth_round(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = True
        self.rule.round = 6
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'B')
        self.assertEqual(self.rule.second_team.name, 'A')

    def test_order_teams_seventh_round_team_team_a_not_score_team_b_score_in_fifth_round(self):
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.order_teams()
        self.rule.team_a.last_scored = False
        self.rule.team_b.last_scored = True
        self.rule.round = 6
        self.rule.order_teams()
        self.rule.round = 7
        self.rule.order_teams()
        self.assertEqual(self.rule.first_team.name, 'A')
        self.assertEqual(self.rule.second_team.name, 'B')


class GameTest(unittest.TestCase):

    def test_start_shoot_out(self):
        game = Game(ClassicRule())
        winner = game.start_shoot_out()
        self.assertIsNotNone(winner)


if __name__ == '__main__':
    unittest.main()