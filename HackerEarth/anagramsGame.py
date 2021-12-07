from math import pi
import random
game_pad = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
start_points = {'p1':[4,2],'p2':[4,2]}
points = [1,2,3,4,8]
end_point = [2,2]
p1_entry_point = [4,1]
p2_entry_point = [0,4]
p1_coins = ['p1_1','p1_2','p1_3','p1_4']
p2_coins = ['p2_1','p2_2','p2_3','p2_4']
roll = random.choice(points)
p1 = start_points['p1']
p2 = start_points['p2']
coins = 4
if roll==8 and game_pad[p1[0]][p1[1]] == 0 and coins>=2:
    game_pad[p1[0]][p1[1]] = p1_coins[0:2]
    p1_coins.pop(0)
    p1_coins.pop(0)
    coins-=2
if roll == 4 and game_pad[p1[0]][p1[1]] == 0 and coins>=1:
    game_pad[p1[0]][p1[1]] = p1_coins[0:1]
    p1_coins.pop(0)
    coins-=1
print(roll)
print(coins)
for i in range(len(game_pad)):
    print(*game_pad[i])
print(p1_coins)