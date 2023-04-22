class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        self.permuteHelper([], nums)
       
        return self.res
    
    def permuteHelper(self, path, remaining):
        if remaining == []:
            self.res.append(path)
            return
        
        for i, item in enumerate(remaining):
            self.permuteHelper(path + [item], remaining[:i] + remaining[i+1:])