class Solution {
    public String solution(String my_string, int s, int e) {
        char[] answer = new char[my_string.length()];
        for(int i = 0; i < my_string.length(); i++){
            if(s <= i && i <= e){
                answer[e + s - i] = my_string.charAt(i);
            } else {
                answer[i] = my_string.charAt(i);
            }
        }
        return new String(answer);
    }
}
