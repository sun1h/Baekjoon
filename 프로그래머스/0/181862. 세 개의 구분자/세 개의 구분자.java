import java.util.*;

class Solution {
    public ArrayList solution(String myStr) {
        ArrayList answer = new ArrayList<>();
        String[] splitStr = myStr.split("a|b|c");  

        for (String s : splitStr) {
            if (!s.isEmpty()) {
                answer.add(s);
            }
        }
        if(answer.size()==0){
            answer.add("EMPTY");
        }
        return answer;
    }
}