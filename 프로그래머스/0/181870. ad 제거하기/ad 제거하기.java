import java.util.*;

class Solution {
    public ArrayList solution(String[] strArr) {
        ArrayList answer = new ArrayList<>();
        for(int i=0; i<strArr.length; i++){
            if(!strArr[i].contains("ad")){
                answer.add(strArr[i]);
            }
        }
        return answer;
    }
}