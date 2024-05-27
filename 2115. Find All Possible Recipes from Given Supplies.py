class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        aList = defaultdict(set)
        indegree = defaultdict(int)
        wordToNum = defaultdict(int)
        numToWord = defaultdict(str)
        start = 0
        
        for idx,r in enumerate(recipes):
            wordToNum[r] = start
            numToWord[start] = r
            indegree[start] = 0
            recipes[idx] = wordToNum[r]
            start += 1
        
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in wordToNum:
                    wordToNum[ingredients[i][j]] = start
                    numToWord[start] = ingredients[i][j]
                    indegree[start] = 0
                    start += 1

                indegree[recipes[i]] += 1
                ingredients[i][j] = wordToNum[ingredients[i][j]]
                
                aList[ingredients[i][j]].add(recipes[i])

        recipes = set(recipes)
        zeroQ = deque()
        for s in supplies:
            if s not in wordToNum: continue
            if not indegree[wordToNum[s]]: zeroQ.append(wordToNum[s])
        
        ans = []
        while zeroQ:
            curr = zeroQ.popleft()
            if curr in recipes:
                ans.append(numToWord[curr])
            indegree[curr] -= 1

            for ingre in aList[curr]:
                indegree[ingre] -= 1
                if indegree[ingre]==0:
                    zeroQ.append(ingre)
        return ans