class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        trans = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for w in words:
            code = ""
            for ch in w:
                code += morse[ord(ch)-97]
            trans.add(code)
        return len(trans)