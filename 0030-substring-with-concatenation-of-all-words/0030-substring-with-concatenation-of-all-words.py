from collections import Counter, defaultdict
from typing import List

class Solution:


    def findSubstring(self,s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)

        # Frequency of required words
        target = Counter(words)
        result = []

        # Try each possible alignment
        for offset in range(word_len):
            left = offset
            right = offset
            window_count = defaultdict(int)
            matched_words = 0

            # Move right pointer in word-sized steps
            while right + word_len <= s_len:
                word = s[right:right + word_len]
                right += word_len

                # If word is not needed, reset the window
                if word not in target:
                    window_count.clear()
                    matched_words = 0
                    left = right
                    continue

                # Add current word to the window
                window_count[word] += 1
                matched_words += 1

                # If a word is overused, shrink from the left
                while window_count[word] > target[word]:
                    left_word = s[left:left + word_len]
                    window_count[left_word] -= 1
                    matched_words -= 1
                    left += word_len

                # If window has exactly all words, record start
                if matched_words == num_words:
                    result.append(left)

                    # Slide one word forward to look for next match
                    left_word = s[left:left + word_len]
                    window_count[left_word] -= 1
                    matched_words -= 1
                    left += word_len

        return result