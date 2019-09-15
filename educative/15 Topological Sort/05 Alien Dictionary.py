'''
Alien Dictionary
'''

from collections import deque


def find_order(words):
    edges = set()
    characters = set()

    for word in words:
        for character in word:
            characters.add(character)

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        n1, n2 = len(word1), len(word2)
        i1, i2 = 0, 0
        while i1 < n1 and i2 < n2 and word1[i1] == word2[i2]:
            i1 += 1
            i2 += 1

        if i1 < n1 and i2 < n2:
            edges.add((word1[i1], word2[i2]))

    return topologicalSort(edges, characters)


def topologicalSort(edges, characters):

    inDegree = {i: 0 for i in characters}  # {node, num}
    graph = {i: [] for i in characters}  #{node, [neighbors]}

    for edge in edges:
        parent, child = edge[0], edge[1]

        inDegree[child] += 1
        graph[parent].append(child)

    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    result = []
    while sources:
        node = sources.popleft()
        result.append(node)
        for child in graph[node]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    if len(result) != len(characters):
        return ""

    return ''.join(result)


def main():
    print(find_order(["ba", "bc", "ac", "cab", "cab"]))
    print(find_order(["cab", "aaa", "aab"]))
    print(find_order(["ywx", "xww", "xz", "zyy", "zwz"]))


main()
