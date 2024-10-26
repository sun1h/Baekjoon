class Solution {
    public String solution(String s) {
        String answer = "";
        boolean blank = false;
        int idx = 0;
        
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)==' '){
                idx = 0;
                answer+= ' ';
                blank = true;
            }else if(idx%2==0){
                answer+=Character.toUpperCase(s.charAt(i));
                ++idx;
            }else{
                answer+=Character.toLowerCase(s.charAt(i));
                ++idx;
            }
        }
        return answer;
    }
}