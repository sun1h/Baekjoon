import java.util.*;

class Solution {
    public int totalN(int n){
        int total = 0;
        while(n>=1){
            total += n%10;
            n/=10;
        }
        return total;
    }
    
    public boolean solution(int x) {
        boolean answer = false;
        if(x%totalN(x)==0){
            answer = true;
        }
        return answer;
    }
}