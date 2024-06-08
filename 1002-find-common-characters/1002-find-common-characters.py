class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = list(words[0])

        for i in range(1, len(words)):
            word = words[i]
            new_common_chars = []
            for c in word:
                if c in common_chars:
                    new_common_chars.append(c)
                    common_chars.remove(c)
            common_chars = new_common_chars

            if common_chars==[]:
                return []
        return common_chars