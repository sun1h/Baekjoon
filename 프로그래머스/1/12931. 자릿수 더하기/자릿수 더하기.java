import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        int tmp = 0;
        
        while(n>=1){
            tmp = n%10;
            n /=10;
            answer += tmp;
        }

        return answer;
    }
}