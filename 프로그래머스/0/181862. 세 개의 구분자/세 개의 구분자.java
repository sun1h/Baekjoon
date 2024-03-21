import java.util.*;

class Solution {
    public ArrayList solution(String myStr) {
        ArrayList answer = new ArrayList<>();
        String tmp = "";
        for(char c:myStr.toCharArray()){
            if(c=='a'||c=='b'||c=='c'){
                if(tmp.length()!=0){
                    answer.add(tmp);
                    tmp = "";
                }
            }else{
                tmp+=c;
            }
        }
        if(tmp.length()!=0){
            answer.add(tmp);
        }
        if(answer.size()==0){
            answer.add("EMPTY");
        }
        return answer;
    }
}