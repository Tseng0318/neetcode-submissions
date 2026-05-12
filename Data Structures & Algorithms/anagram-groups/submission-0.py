class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty = {}

        for words in strs:
            sort = "".join(sorted(words))
            if sort not in empty:
                empty[sort] = []
            empty[sort].append(words)
        return list(empty.values())
        