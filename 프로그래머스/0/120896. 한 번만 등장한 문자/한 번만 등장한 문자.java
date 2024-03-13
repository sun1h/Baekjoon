class Solution {
    public String solution(String s) {
        String answer = "";
        int[] cnt = new int[26];
        for(char c:s.toCharArray()){
            cnt[c-'a']++;
        }
        
        for(int i=0; i<cnt.length; i++){
            if(cnt[i]==1){
                answer+=(char)(i + 'a');
            }
        }
        return answer;
    }
}