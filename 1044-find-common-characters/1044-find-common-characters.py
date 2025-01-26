class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # can solve it using hash table for the first word get the hash table then
        # compare the all other words with the first hash table if there are any common
        # then keep the min count of the letter in the compared words.
        first_hash = {}
        res = []
        for c in words[0]:
            if c in first_hash:
                first_hash[c] += 1
            else:
                first_hash[c] = 1

        for word in words[1:]:
            temp_hash = {}
            for c in word:
                if c in temp_hash:
                    temp_hash[c] += 1
                else:
                    temp_hash[c] = 1
            for c in first_hash:
                if c in temp_hash:
                    first_hash[c] = min(first_hash[c],temp_hash[c])
                else:
                    first_hash[c] = 0
        for key,count in first_hash.items():
            res.extend(key*count)

        return res