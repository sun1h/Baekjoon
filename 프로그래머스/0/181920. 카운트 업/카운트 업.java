import java.util.*;

class Solution {
    public ArrayList solution(int start_num, int end_num) {
        ArrayList answer = new ArrayList<Integer>();
        for(int i=start_num; i<=end_num; i++){
            answer.add(i);
        }
        return answer;
    }
}