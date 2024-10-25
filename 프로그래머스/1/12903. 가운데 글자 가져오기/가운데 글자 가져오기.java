class Solution {
    public String solution(String s) {
        int le = s.length();
        if(le%2!=0){
            return String.valueOf(s.charAt(le/2));
        }else{
            return s.substring(le/2-1,le/2+1);
        }
    }
}