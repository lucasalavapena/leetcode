class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def MorseRepresentations(word):
            res = ""
            morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            for w in word:
                res += morse[ord(w) - 97]
            return res
        return len(set([MorseRepresentations(word) for word in words]))
            
        
        