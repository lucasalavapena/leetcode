from string import ascii_lowercase
# from deepcopy import copy

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        score_by_letter = dict(zip(ascii_lowercase, score))
        cnt = Counter(letters)
        def compute_score(word):
            return sum(score_by_letter[c] for c in word)
        word_scores = [compute_score(word) for word in words]
        word_cnt = [Counter(word) for word in words]
        letters_cnter = Counter(letters)

        # could make a cache using an tuple of vector counts or something
        def dp(i, letters_cnt):
            nonlocal word_scores, word_cnt
            if i == len(words):
                return 0
            
            # do not take, note we do this one first, otherwise I think the letters state will
            # be wrong or I will have to do some deepcopy if that makes sense
            score = dp(i + 1, letters_cnt)
            # checking this earlier, so I can use the counter subtraction
            if all(letters_cnt[k] >= v for k, v in word_cnt[i].items()):
                score = max(dp(i + 1, letters_cnt-word_cnt[i]) + word_scores[i], score)
            return score

        return dp(0, letters_cnter)