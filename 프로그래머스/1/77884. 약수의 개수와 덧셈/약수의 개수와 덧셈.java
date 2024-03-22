import java.util.*;

class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for(int i=left; i<=right; i++){
            ArrayList numbers = new ArrayList<>();
            for(int j=1; j<=i;j++){
                if(i%j==0){
                    numbers.add(j);
                }
            }
            if(numbers.size()%2==0){
                answer+=i;
            }else{
                answer-=i;
            }
        }
        
        return answer;
    }
}