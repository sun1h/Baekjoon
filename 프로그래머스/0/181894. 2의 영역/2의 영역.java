import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int start_tmp = -1;
        int end_tmp = 0; 
        boolean foundTwo = false; 

        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == 2) {
                foundTwo = true; 
                if(start_tmp == -1) {
                    start_tmp = i;
                }
                end_tmp = i + 1;
            }
        }

        if(!foundTwo) {
            return new int[]{-1};
        }

        return Arrays.copyOfRange(arr, start_tmp, end_tmp);
    }
}
