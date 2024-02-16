import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        s = s.toLowerCase();
        
        int pCnt = (int) s.chars().filter(i->i=='p').count();
        int yCnt = (int) s.chars().filter(i->i=='y').count();   
        
        if(pCnt!=yCnt){
            answer = false;
        }
        
        return answer;
    }
}