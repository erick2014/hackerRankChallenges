def hurdleRace(maxHeight, hurdles):
    greaterHurdles = max(hurdles)
    totalOfPotions = greaterHurdles - maxHeight

    if totalOfPotions > 0:
        return totalOfPotions
    else:
        return 0


nk = input().split()

n = int(nk[0])

k = int(nk[1])

height = list(map(int, input().rstrip().split()))

result = hurdleRace(k, height)

print(result)
