class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = deque([deck.pop()])
        while deck:
            ans.append(ans.popleft())
            ans.append(deck.pop())
        ans = list(ans)
        return ans[::-1]