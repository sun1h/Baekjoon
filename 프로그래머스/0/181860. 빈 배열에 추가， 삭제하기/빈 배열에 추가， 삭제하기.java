import java.util.*;

class Solution {
    public ArrayList solution(int[] arr, boolean[] flag) {
        ArrayList answer = new ArrayList<Integer>();
        
        for(int i=0; i<flag.length; i++){
            if(flag[i]){
                for(int j=0; j<arr[i]*2; j++) {
                    answer.add(arr[i]);
                }
            }else{
                for(int j=0; j<arr[i]; j++) {
                    answer.remove(answer.size()-1);
                }
            }
        }
        return answer;
    }
}