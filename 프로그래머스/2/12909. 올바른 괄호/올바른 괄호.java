class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int cnt = 0;
        
        if(s.charAt(0)==')'){
                return false;
        }
        
        
        for (char c : s.toCharArray()) {
            if (c == '(') {
                cnt++; 
            } else if (c == ')') {
                cnt--; 
            }

            if (cnt < 0) {
                return false; 
            }
        }
        
        if(cnt!=0){
            return false;
        }
            
        return answer;
    }
}