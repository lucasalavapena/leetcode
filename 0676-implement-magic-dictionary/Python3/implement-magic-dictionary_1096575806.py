class MagicDictionary:
    def __init__(self):
        self.magic_set = None

    def buildDict(self, dictionary: List[str]) -> None:
        self.magic_set = set(dictionary)

    def search(self, searchWord: str) -> bool:
        def diff(a, b):
            if len(a) != len(b): return False
            cnt = 0
            for c1, c2 in zip(a, b):
                if c1 != c2:
                    cnt += 1
                    if cnt > 1:
                        return False
            return True if cnt == 1 else False

        
        return any(diff(item, searchWord) for item in self.magic_set)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)