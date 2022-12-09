from collections import deque

expression = input().split()
nums = deque()
for ch in expression:
    if ch in "+-/*":
        while len(nums) > 1:
            first = nums.popleft()
            second = nums.popleft()
            if ch == '*':
                result = first * second
            elif ch == "-":
                result = first - second
            elif ch == "+":
                result = first + second
            elif ch == "/":
                result = first // second
            nums.appendleft(int(result))
    else:
        nums.append(int(ch))

print(result)