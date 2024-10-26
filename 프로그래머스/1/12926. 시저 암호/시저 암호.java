class Solution {
    public String solution(String s, int n) {
        StringBuilder answer = new StringBuilder();
        for(char c:s.toCharArray()){
            if(c==(' ')){
                answer.append(' ');
            }else if((int)c>=97){
                answer.append((char) ((c - 'a' + n) % 26 + 'a'));
            }else{
                answer.append((char) ((c - 'A' + n) % 26 + 'A'));
            }
        }

        return answer.toString();
    }
}