class Solution {
    public int solution(String s) {
        int answer = 1;
        
        if(s.charAt(0) == '-'){
            s = s.substring(1,s.length());
            answer *= (-1);
        }
        
        answer*=Integer.parseInt(s);
        return answer;
    }
}