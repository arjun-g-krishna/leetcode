class Solution {
    public int[] sortedSquares(int[] nums) {
        // Initialise left and right pointers at beginning and end respectively
        int left=0,right=nums.length-1;
        // Initialise a pointer that points to the last element
        int pointer=nums.length-1;
        // Create an array to store result
        int[] result = new int[nums.length];
        while(left<=right){
            if(Math.abs(nums[left])>Math.abs(nums[right])){
                result[pointer]=nums[left]*nums[left];
                left++;
            }
            else{
                result[pointer]=nums[right]*nums[right];
                right--;
            }
            pointer--;
        }
    return result;        
    }
}