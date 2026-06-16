class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty = {}
        for word in strs:
            label = "".join(sorted(word))
            if label not in empty:
                empty[label] = []
            empty[label].append(word)

        return list(empty.values())

