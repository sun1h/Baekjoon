import java.util.*;

class Solution {
    public ArrayList solution(int n, int k) {
        ArrayList answer = new ArrayList<>();

        for(int i=1; i<=(n/k);i++){
            answer.add(k*i);
        }
        return answer;
    }
}