class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return len(max((s.split(" ") for s in sentences), key=len))