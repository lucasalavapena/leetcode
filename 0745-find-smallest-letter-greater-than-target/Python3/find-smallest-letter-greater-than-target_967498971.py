class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect(letters, target)
        return letters[idx] if idx < len(letters) else letters[0]