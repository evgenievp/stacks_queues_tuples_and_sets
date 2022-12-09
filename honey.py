from collections import deque

bees = deque([int(x) for x in input().split()])
honeys = [int(x) for x in input().split()]
operators = deque([x for x in input().split()])
total = 0
while bees and honeys:
    bee = bees[0]
    honey = honeys.pop()
    if bee > honey:
        continue

    bees.popleft()
    operator = operators.popleft()
    if operator == "+":
        total += abs(honey + bee)
    elif operator == "/" and honey > 0:
        total += abs(bee / honey)
    elif operator == "*":
        total += abs(bee * honey)
    elif operator == "-":
        total += abs(bee - honey)

print(f"Total honey made: {total}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if honeys:
    print(f"Nectar left: {', '.join(str(x) for x in honeys)}")
