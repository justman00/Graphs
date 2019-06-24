class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def get_latest(ans):
    # loop over all of the ancestors and store the minimum per length of path
    # return that minimum

    min_val = -1
    longest_path = 1

    for idx, val in enumerate(ans):

        if longest_path < val[1]:
            longest_path = val[1]
            min_val = val[0]
        else:
            if val[0] < min_val:
                min_val = val[0]

    return min_val


def earliest_ancestor(ancestors, starting_node):
    visited = set()

    q = Queue()

    q.enqueue([starting_node])

    ans = []

    while q.size() > 0:
        path = q.dequeue()

        last_one = path[-1]

        if len(path) > 1:
            ans.append((last_one, len(path)))

        if last_one not in visited:
            visited.add(last_one)

            for t in ancestors:
                if t[-1] == last_one:
                    copy_path = list(path)
                    copy_path.append(t[0])

                    q.enqueue(copy_path)

    return get_latest(ans)


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
#                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(test_ancestors, 8))
