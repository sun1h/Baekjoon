class Solution {
    public String solution(String n_str) {
        String answer = "";
        int id = 0;
        for(int i=id; i<n_str.length();i++){
            if(n_str.charAt(i)!='0'){
                System.out.println(i);
                id = i;
                break;
            }
        }
        answer = n_str.substring(id,n_str.length());
        return answer;
    }
}