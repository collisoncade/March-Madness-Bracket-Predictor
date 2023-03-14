from random import randint

divisions = {'Midwest', 'West', 'South', 'East'}
rounds = range(1, 6)

rnd = 0
d = 0
end_of_rnd_rng = 8

while d < 1:
    for division in divisions:
        print(division)
        while rnd < 4:   
            print(f"\tRound {rnd + 1}\n")
            rnd_range = range(1, int(end_of_rnd_rng + 1))
            for game in rnd_range:
                coin_flip = randint(0,1)
                if coin_flip == 0:
                    coin_flip = 'Top'
                else:
                    coin_flip = 'Bottom'
                print(f"\t\tGame {game}: {coin_flip}")
            print()
            end_of_rnd_rng //= 2
            rnd += 1
        rnd = 0
        end_of_rnd_rng = 8
    d += 1

print("National Championship\n")
coin_flip = randint(0,1)
if coin_flip == 0:
    coin_flip = 'Top'
else:
    coin_flip = 'Bottom'
print(f"\t{coin_flip}\n")
