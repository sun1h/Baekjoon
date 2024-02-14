import java.util.*;
class Solution {
    public ArrayList solution(String my_string) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        for(char c:my_string.toCharArray()){
            if(Character.isDigit(c)){
                answer.add(Character.getNumericValue(c));
            }
        }
        Collections.sort(answer);
        return answer;
    }
}