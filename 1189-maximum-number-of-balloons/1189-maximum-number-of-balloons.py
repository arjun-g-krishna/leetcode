from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        countBalloon = Counter("balloon")
        result = len(text)
        for c in countBalloon:
            result = min(result,(countText[c] // countBalloon[c]))
        return result    