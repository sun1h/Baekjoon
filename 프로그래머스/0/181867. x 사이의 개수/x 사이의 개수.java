import java.util.*;

class Solution {
    public ArrayList solution(String myString) {
        ArrayList answer = new ArrayList<>();
        myString+="Xx";
        String[] tmp = myString.split("x");
        
        for(int i=0; i<tmp.length; i++){
            if(tmp[i].contains("X")){
                answer.add(tmp[i].length()-1);
                break;
            }else{
                answer.add(tmp[i].length());
            }
        }
        return answer;
    }
}