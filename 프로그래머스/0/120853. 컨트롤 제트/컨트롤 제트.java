class Solution {
    public int solution(String s) {
        int answer = 0;
        int tmp = 0;
        String[] st = s.split(" ");
        for(int i=0; i<st.length; i++){
            if(st[i].equals("Z")){
                answer-=tmp;
                tmp = 0;
            }else{
                tmp = Integer.parseInt(st[i]);
                answer += tmp;
            }
        }
        return answer;
    }
}