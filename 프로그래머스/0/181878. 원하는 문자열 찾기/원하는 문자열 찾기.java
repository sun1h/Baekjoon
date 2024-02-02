class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String my = myString.toLowerCase();
        String p = pat.toLowerCase();;
        if(my.contains(p)){
            answer = 1;
        }
  
        return answer;
    }
}