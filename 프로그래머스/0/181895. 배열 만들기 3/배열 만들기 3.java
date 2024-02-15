import java.util.*;

class Solution {
    public ArrayList solution(int[] arr, int[][] intervals) {
        ArrayList answer = new ArrayList <Integer> ();
        
        for(int i=0; i<=1; i++){
            for(int j=intervals[i][0]; j<=intervals[i][1]; j++){
                answer.add(arr[j]);
            }
        }
        return answer;
    }
}