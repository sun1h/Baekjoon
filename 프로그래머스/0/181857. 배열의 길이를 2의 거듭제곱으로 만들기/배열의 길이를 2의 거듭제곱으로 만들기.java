import java.util.*;

class Solution {
    public ArrayList solution(int[] arr) {
        int tmp = 0;
        for(int i=1; i<=1024; i*=2){
            if(i-arr.length>=0){
                tmp = i;
                break;
            }
        }
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0; i<tmp; i++){
            if(i < arr.length){ 
                answer.add(arr[i]);
            }else{ 
                answer.add(0);
            }
        }
        return answer;
    }
}