class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;
        if(my_string.contains(is_suffix)){
            int tmp =0;
            for(int i=is_suffix.length()-1; i>=0; i--){
                int id = my_string.length()-is_suffix.length();        
                if(is_suffix.charAt(i)==my_string.charAt(id+i)){
                    tmp+=1;
                }
            }
            if(tmp==is_suffix.length()){
                answer= 1;
            }
        }
        return answer;
    }
}