class Solution {
public:
    int max(int x,int y){
        return (x>y)?x:y;
    }
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];
        int curSum = 0;
        int num;
        for (auto num:nums){
            if (curSum < 0) curSum = 0;
            curSum += num;
            maxSum = max(maxSum,curSum);
        }
        return maxSum;
    }
};