class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if not s or not words:
            return []

        word_len = len(words[0])
        m = len(words)
        need = Counter(words)
        res = []
        n = len(s)

        for offset in range(word_len):
            left = offset
            seen = Counter()
            count = 0

            for right in range(offset, n - word_len + 1, word_len):
                w = s[right:right + word_len]

                if w in need:
                    seen[w] += 1
                    count += 1

                    while seen[w] > need[w]:
                        lw = s[left:left + word_len]
                        seen[lw] -= 1
                        left += word_len
                        count -= 1

                    if count == m:
                        res.append(left)
                        lw = s[left:left + word_len]
                        seen[lw] -= 1
                        left += word_len
                        count -= 1
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return res
