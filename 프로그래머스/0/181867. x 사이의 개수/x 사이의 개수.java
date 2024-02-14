import java.util.*;

class Solution {
    public ArrayList solution(String myString) {
        ArrayList answer = new ArrayList<>();
        String[] tmp = myString.split("x",myString.length());
        
        for(int i=0; i<tmp.length; i++){
            answer.add(tmp[i].length());
        }
        return answer;
    }
}