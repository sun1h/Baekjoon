import java.util.*;

class Solution {
    public ArrayList solution(String myString) {
        ArrayList answer = new ArrayList<>();
        ArrayList<Integer> id = new ArrayList<Integer>();

        for(int i=0; i<myString.length();i++){
            if(myString.charAt(i)=='x'){
                id.add(i);
            }
        }

        answer.add(id.get(0));
        for(int i=0; i<id.size()-1; i++){
            answer.add(id.get(i+1)-id.get(i)-1);
        }
        answer.add(myString.length()-id.get(id.size()-1)-1);
        return answer;
    }
}