class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)== len(word2) and set(word1) == set(word2):
            return True
        return False
        