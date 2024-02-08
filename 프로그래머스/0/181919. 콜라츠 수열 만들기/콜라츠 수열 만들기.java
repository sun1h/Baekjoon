import java.util.*;

class Solution {
    public ArrayList solution(int n) {
        ArrayList answer = new ArrayList<>();
        while(n!=1){
            answer.add(n);
            if(n%2==0){
                n/=2;
            }else{
                n=(3*n+1);
            }
        }
        answer.add(1);
        return answer;
    }
}