class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        int_to_letters = {
            "2": "abc", 
            "3": "def",
            "4":"ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if digits == "":
            return []
        res = [""]
        
        for digit in digits:
            res_len = len(res)
            new_res = []
            for j in int_to_letters[digit]:
                for k in range(res_len):
                    new_entry = res[k] + j
                    new_res.append(new_entry)
            res = new_res[:]
        return res