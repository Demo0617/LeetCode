class MagicDictionary:

    def __init__(self):
        self.words = list()


    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary


    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(searchWord) != len(word):
                continue
            else:
                diff = 0
                for chx, chy in zip(searchWord, word):
                    if chx != chy:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    return True
        return False

