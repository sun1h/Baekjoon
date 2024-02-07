class Solution {
    public String solution(String myString) {
        String answer = "";
        for(char my:myString.toCharArray()){
            if (my <'l'){
                answer += "l";
            }else{
                answer+= my;
            }
        }
        return answer;
    }
}