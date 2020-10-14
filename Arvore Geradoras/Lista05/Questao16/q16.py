from collections import deque


class Node:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dist = dis

    def __repr__(self):
        return str((self.x, self.y))


def findPath(matrix, N, x, y):

    q = deque()

    src = Node(x, y, 0)
    q.append(src)

    visited = set()

    key = (src.x, src.y)
    visited.add(key)

    while q:
        curr = q.popleft()
        i = curr.x
        j = curr.y

        if i == N - 1 and j == N - 1:
            return curr.dist

        value = matrix[i][j]

        # moving up
        if (i - 1 >= 0 and value != -1 and (i-1, j) not in visited):
            q.append(Node(i-1, j, curr.dist+1))
            visited.add((i-1, j))

        # moving down
        if (i + 1 < N and value != -1 and (i+1, j) not in visited):
            q.append(Node(i+1, j, curr.dist+1))
            visited.add((i+1, j))

        # moving left
        if (j - 1 >= 0 and value != -1 and (i, j-1) not in visited):
            q.append(Node(i, j-1, curr.dist+1))
            visited.add((i, j-1))

        # moving right
        if (j + 1 < N and value != -1 and (i, j+1) not in visited):
            q.append(Node(i, j+1, curr.dist+1))
            visited.add((i, j+1))

    return None


if __name__ == '__main__':

    matrix = [
        [0, 0, 0, 0],
        [-1, 0, -1, 0],
        [-1, 0, 0 ,0],
        [-1, 0, -1, 0]
    ]

    N = len(matrix)

    node = findPath(matrix, N, 0, 0)

    print("dis ", node)
