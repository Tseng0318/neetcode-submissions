class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty = {}
        for labels in strs:
            label = "".join(sorted(labels))
            if label not in empty:
                empty[label] = []
            empty[label].append(labels)
        return list(empty.values())
        