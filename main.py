from main import *

GAME_NUM = 300000

def format_result(results):
    return '{0:.2f}'.format(results['A'] * 100 / GAME_NUM), '{0:.2f}'.format(results['B'] * 100 / GAME_NUM)


results = {'A': 0, 'B': 0}
for _ in range(GAME_NUM):
    game = Game(AlternatingRule())
    winner = game.start_shoot_out()
    results[winner] += 1

print('Alternating rule result:', format_result(results))


results = {'A': 0, 'B': 0}
for _ in range(GAME_NUM):
    game = Game(CatchUpRule())
    winner = game.start_shoot_out()
    results[winner] += 1

print('Catch up rule result:', format_result(results))


results = {'A': 0, 'B': 0}
for _ in range(GAME_NUM):
    game = Game(AdjustedCatchUpRule())
    winner = game.start_shoot_out()
    results[winner] += 1

print ('Adjusted Catch up rule result:', format_result(results))


