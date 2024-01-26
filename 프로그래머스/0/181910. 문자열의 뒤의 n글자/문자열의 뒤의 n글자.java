class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        int l = my_string.length()-n;
        for(int i=l; i<my_string.length(); i++){
            answer+=my_string.charAt(i);
        }
        return answer;
    }
}