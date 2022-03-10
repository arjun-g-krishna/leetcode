class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:        
        bestValue = arr[-1]
        arr[-1] = -1 

        for i in range(len(arr)-2, -1,-1):
            backup = arr[i]
            arr[i] = bestValue
            if(backup>bestValue):
                bestValue = backup
        return arr