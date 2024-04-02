class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        def match(sentence, word):
            i = 0
            if len(sentence)<len(word):
                return False
            while i<len(word):
                if sentence[i]!=word[i]:
                    return False
                i+=1
            return True
        for i in range(len(sentence)):
            if match(sentence[i], searchWord):
                return i+1
        return -1