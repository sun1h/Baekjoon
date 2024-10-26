import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        boolean blank = false;
        
        if(s.charAt(0)==' '){
            blank = true;
        }else{
            answer += Character.toUpperCase(s.charAt(0));
        }
                 
        for(int i=1; i<s.length(); i++){
            if(s.charAt(i)==' '){
                answer+= ' ';
                blank = true;
            } else if(blank==true && s.charAt(i)!=' '){
                answer+= Character.toUpperCase(s.charAt(i));
                blank = false;
            }else{
                answer+= Character.toLowerCase(s.charAt(i));
            }
        }
        return answer;
    }
}