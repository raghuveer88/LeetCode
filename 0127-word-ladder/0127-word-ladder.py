class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # there is improved way to code this in the below comments
        q = deque()
        q.append((beginWord,1))
        visited = set()

        if endWord not in wordList:
            return 0

        while q:
            word, move = q.popleft()
            for i in range(len(wordList)):
                change = 0
                for j in range(len(beginWord)):
                    if word[j] != wordList[i][j]:
                        change += 1
                        if change >= 2:
                            break
                if change == 1 and wordList[i] == endWord:
                    return move+1
                if change == 1 and wordList[i] not in visited:
                    q.append((wordList[i],move+1))
                    visited.add(wordList[i])
        return 0
                
# from typing import List
# from collections import defaultdict, deque

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0

#         L = len(beginWord)
#         all_words = wordList[:]  # copy
#         all_words.append(beginWord)

#         patterns = defaultdict(list)
#         for w in all_words:
#             for i in range(L):
#                 pat = w[:i] + "*" + w[i+1:]
#                 patterns[pat].append(w)

#         q = deque([(beginWord, 1)])
#         visited = {beginWord}

#         while q:
#             word, dist = q.popleft()
#             if word == endWord:
#                 return dist

#             for i in range(L):
#                 pat = word[:i] + "*" + word[i+1:]
#                 for nxt in patterns[pat]:
#                     if nxt not in visited:
#                         visited.add(nxt)
#                         q.append((nxt, dist + 1))
#                 patterns[pat] = []  # key optimization

#         return 0


