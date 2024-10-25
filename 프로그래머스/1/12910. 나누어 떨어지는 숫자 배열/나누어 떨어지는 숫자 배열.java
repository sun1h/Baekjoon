import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> answerList = new ArrayList<>();
        for(int i=0; i<arr.length; i++){
            if(arr[i]%divisor==0){
                answerList.add(arr[i]);
            }
        }
        
        if(answerList.size()==0){
            return new int[]{-1};
        }else{
            int[] answer = answerList.stream()
                                 .mapToInt(i->i)
                                 .toArray();
        
            Arrays.sort(answer);
            return answer;
        }     
    }
}