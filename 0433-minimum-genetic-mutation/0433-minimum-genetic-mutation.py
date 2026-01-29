class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque()
        q.append((startGene,0))
        visited = set()
        chars = ['A','C','G','T']
        while q:
            gene, move = q.popleft()
            if gene == endGene:
                return move
            for i in range(8):
                
                for j in range(len(chars)):
                    if gene[i] != chars[j]:
                        term = gene[:i] + chars[j] + gene[i + 1:]
                        if term in bank and term not in visited:
                            q.append((term,move+1))
                            visited.add(term)
        return -1

