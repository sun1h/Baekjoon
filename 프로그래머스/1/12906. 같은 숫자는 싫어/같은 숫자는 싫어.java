import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        int preNum = -1;
        
        for(int a:arr){
            if(a!=preNum){
                answer.add(a);
                preNum = a;
            }
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}