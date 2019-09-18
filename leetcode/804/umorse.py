class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = list()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            trans = str()
            for w in word:
                pos = ord(w)-97  # 'a' == 97
                trans += morse[pos]
            if trans not in codes:
                codes.append(trans)
        return len(codes)
            