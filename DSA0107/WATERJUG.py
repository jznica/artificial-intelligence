from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([(0,0)])

    while queue:
        x, y = queue.popleft()

        if (x,y) in visited:
            continue
        visited.add((x,y))

        print(x, y)

        if x == target or y == target:
            print("Target reached")
            return

        queue.append((jug1, y))   # fill jug1
        queue.append((x, jug2))   # fill jug2
        queue.append((0, y))      # empty jug1
        queue.append((x, 0))      # empty jug2
        queue.append((max(0, x-(jug2-y)), min(jug2, y+x)))  # pour jug1→jug2
        queue.append((min(jug1, x+y), max(0, y-(jug1-x))))  # pour jug2→jug1


water_jug(4,3,2)


