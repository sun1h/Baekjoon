import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> arr = new HashSet<>();
        for(int i=0; i<nums.length; i++){
            arr.add(nums[i]);
        }
        
        return Math.min(arr.size(),(nums.length)/2);
    }
}