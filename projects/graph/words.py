from util import Queue, Stack


def find_ladders(beginWord, endWord):
    visited = set()
    q = Queue()

    q.enqueue([beginWord])

    while q.size() > 0:
        path = q.dequeue()
        node = path[-1]

        if node == endWord:
            return len(path)

        if node not in visited:
            visited.add(node)
            for val in get_neighbours(node):
                copy_path = path.copy()
                copy_path.append(val)
                q.enqueue(copy_path)

    pass


wordList = set(["hot", "dot", "dog", "lot", "log", "cog"])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def get_neighbours(word):
    neighbours = []

    string_word = list(word)

    for i in range(len(string_word)):
        for letter in letters:
            temp_word = list(string_word)
            temp_word[i] = letter

            w = "".join(temp_word)

            if w != word and w in wordList:
                neighbours.append(w)

    return neighbours


print(get_neighbours('log'))
print(find_ladders('hit', 'cog'))
