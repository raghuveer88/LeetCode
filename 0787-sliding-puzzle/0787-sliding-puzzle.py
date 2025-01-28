class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # you can solve this using BFS just go to every place where there is 0 and
        # try all kinds of combinations and repeat it.
        b = []
        for i in board:
            for j in i:
                b.append(j)

        neighbours = {
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4],
            4: [1,3,5],
            5: [2,4]
        }

        q = deque([(b.index(0),b,0)])
        visit = set([tuple(b)])

        while q:
            i,b,length = q.popleft()

            if b == [1,2,3,4,5,0]:
                return length

            for j in neighbours[i]:
                new_arr = b.copy()
                new_arr[j],new_arr[i] = b[i],b[j]

                if tuple(new_arr) not in visit:
                    q.append((j,new_arr, length + 1))
                    visit.add(tuple(new_arr))
        return -1
            