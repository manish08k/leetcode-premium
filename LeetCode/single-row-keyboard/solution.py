class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_dict={}
        for i,key in enumerate(keyboard):
            key_dict[key]=i
        ans=0
        cur_idx=0
        for c in word:
            ans+=abs(cur_idx-key_dict[c])
            cur_idx=key_dict[c]
        return ans