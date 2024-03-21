import java.util.*;
class Solution {
    public ArrayList solution(int[] arr) {
        ArrayList answer = new ArrayList<>();
        
        int min = Integer.MAX_VALUE;;
        for(int a:arr){
            if(a<min){
                min = a;
            }
        }
        
        for(int a:arr){
            if(a!=min){
                answer.add(a);
            }
        }
        
        if(answer.size()==0){
            answer.add(-1);
        }
        return answer;
    }
}