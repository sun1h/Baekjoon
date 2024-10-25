class Solution {
    boolean solution(String s) {
        boolean answer = true;
        s = s.toUpperCase();
        int p = s.length() - s.replace("P","").length();
        int y = s.length() - s.replace("Y","").length();
        
        if(p!=y){
            answer = false;
        }

        return answer;
    }
}