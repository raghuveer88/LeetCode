class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
       from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        parents = defaultdict(list)  # child -> all possible previous words on shortest paths
        queue = deque([beginWord])
        visited = set([beginWord])
        found = False
        word_len = len(beginWord)

        while queue and not found:
            level_visited = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(word_len):
                    original_char = word[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == original_char:
                            continue

                        next_word = word[:i] + c + word[i + 1:]

                        if next_word in word_set and next_word not in visited:
                            # Record all parents that reach next_word in the shortest way
                            parents[next_word].append(word)

                            if next_word not in level_visited:
                                level_visited.add(next_word)
                                queue.append(next_word)

                            if next_word == endWord:
                                found = True

            visited |= level_visited

        if not found:
            return []

        result = []

        def backtrack(word: str, path: List[str]):
            if word == beginWord:
                result.append(path[::-1])
                return

            for prev in parents[word]:
                backtrack(prev, path + [prev])

        backtrack(endWord, [endWord])
        return result
