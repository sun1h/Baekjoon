class Solution {
    public int solution(String[] strArr) {
        int answer = 0;
        int [] len = new int [31];
        for(String s:strArr){
            len[s.length()]+=1;
            
        }
        for(int l:len){
            if(answer<l){
                answer=l;
            }
        }
        return answer;
    }
}