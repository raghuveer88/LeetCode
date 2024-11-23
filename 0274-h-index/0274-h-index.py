class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sort_cit = sorted(citations)
        len_cit = len(citations)
        cit_dict = {}
        for i,c in enumerate(sort_cit):
            if c >= len_cit - i:
                return len_cit-i

        return 0
