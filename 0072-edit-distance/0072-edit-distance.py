class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) +1
        n = len(word2) +1
        # cache = [[float('inf')]*n]*m
        cache = [[float('inf')] * n for _ in range(m)]

        for j in range(n):
            cache[len(word1)][j] = len(word2)-j
        for i in range(m):
            cache[i][len(word2)] = len(word1)-i

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j],cache[i][j+1],cache[i+1][j+1])

        return cache[0][0] 
