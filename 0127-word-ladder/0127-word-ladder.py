class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
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
                

