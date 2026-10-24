from collections import deque

def solve(start, goal):
    q = deque([start])
    visited = {start}

    while q:
        state = q.popleft()

        if state == goal:
            return True

        i = state.index(0)
        for j in [i-3, i+3, i-1, i+1]:
            if 0 <= j < 9 and abs(i//3-j//3) + abs(i%3-j%3) == 1:
                s = list(state)
                s[i], s[j] = s[j], s[i]
                s = tuple(s)

                if s not in visited:
                    visited.add(s)
                    q.append(s)

    return False

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
print(solve(start, goal))
