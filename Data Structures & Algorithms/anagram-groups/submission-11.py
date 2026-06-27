class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anag_dict = {}

        for item in strs:
            anag_sorted = sorted(item)
            anag = "".join(anag_sorted)
            if anag not in anag_dict:
                anag_dict[anag] = []

            anag_dict[anag].append(item)

        return list(anag_dict.values())

