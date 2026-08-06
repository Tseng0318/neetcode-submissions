class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty = {}
        for st in strs:
            label = "".join(sorted(st))
            if label not in empty:
                empty[label]=[]
            empty[label].append(st)
        return list(empty.values())


