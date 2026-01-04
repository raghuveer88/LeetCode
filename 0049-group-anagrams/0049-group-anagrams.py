class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        unique_sets = defaultdict(list)

        i = 0
        for word in strs:
            temp = str(sorted(word))
            
            unique_sets[temp].append(word)

        for temp in unique_sets:
            output.append(unique_sets[temp])

            
            
            
        
        return output