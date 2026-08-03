class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for str in strs:
            sorted_str = "".join(sorted(str))
            values = groups.get(sorted_str, [])
            groups[sorted_str] = values + [str]


        return [value for value in groups.values()]   