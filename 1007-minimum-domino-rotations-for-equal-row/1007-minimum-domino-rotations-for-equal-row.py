class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for target in [tops[0],bottoms[0]]:
            missTop,missBottom = 0,0
            for i,pair in enumerate(zip(tops,bottoms)):
                top,bottom = pair
                if not(top ==  target or bottom == target):
                    break
                if top != target:
                    missTop += 1
                if bottom != target:
                    missBottom += 1
                if i == len(tops) - 1:
                    return(min(missTop,missBottom))
        return -1                