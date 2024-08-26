class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        # Just take in two queues for R and D and append the indexes 
        # now compare the indexes to decide on what element to be removed
        # if the index is smaller which means it has first chance to get rid
        # of the other element. So compare the indexes and the smaller index 
        # need to be added to the back of the same queue with an offset of len(senate)
        # to maintain the element order in the queue

        
        senate = list(senate)

        r,d = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            dturn = d.popleft()
            rturn = r.popleft()

            if dturn > rturn:
                r.append(rturn + len(senate))
            else:
                d.append(dturn + len(senate))

        return "Radiant" if r else "Dire"
