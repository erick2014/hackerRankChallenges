def catAndMouse(catA, catB, mouse):
    distanceCatA = mouse - catA
    distanceCatB = mouse - catB

    if distanceCatA < 0:
        distanceCatA *= -1
    if distanceCatB < 0:
        distanceCatB *= -1

    if distanceCatA < distanceCatB:
        return "Cat A"
    elif distanceCatB < distanceCatA:
        return "Cat B"
    elif distanceCatA == distanceCatB:
        return "Mouse C"


q = int(input())
distances = []

for q_itr in range(q):
    locations = input().split()

    catALocation = int(locations[0])

    catBLocation = int(locations[1])

    mouseLocation = int(locations[2])

    distances.append(catAndMouse(catALocation, catBLocation, mouseLocation))

for distance in distances:
    print(distance)
