class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0,len(arr)):
            for j in range(i,len(arr)):
                if (i!=j) and (arr[j]/2 == arr[i] or arr[j]*2 == arr[i]):
                    return True
        return False