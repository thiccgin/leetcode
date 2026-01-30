class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        res = []

        for s in strs:
            ss = "".join(sorted(s))
            if ss not in keys:
                keys[ss] = [s]
            else:
                keys[ss].append(s)

        for key, s in keys.items():
            res.append(s)
        return res