class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        pat = pat.replaceAll("A","1")
                 .replaceAll("B","A")
                 .replaceAll("1","B");
        
        if(myString.contains(pat)){
            answer = 1;
        }
        return answer;
    }
}