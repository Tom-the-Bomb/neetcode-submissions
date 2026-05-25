class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            mapping[tuple(sorted(s))].append(s)
        return list(mapping.values())