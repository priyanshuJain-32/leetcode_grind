class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        i,j,k,n,m = 0,0,0,len(s),len(dictionary)
        dictionary.sort(reverse=True)
        longest = 0
        ans = ''
        while k<m:
            word = dictionary[k]
            lWord = len(word)
            if lWord<longest:
                k+=1
                continue
            i,j=0,0
            while i<n and j<lWord:
                if s[i]==word[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            if j==lWord:
                if lWord>longest:
                    longest = lWord
                    ans = word
                elif lWord==longest:
                    if ans>word:
                        ans = word
            k+=1
        return ans