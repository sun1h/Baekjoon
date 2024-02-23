import java.util.*;

class Solution {
    public ArrayList solution(String[] intStrs, int k, int s, int l) {
        ArrayList answer = new ArrayList<Integer>();
        for(int i=0; i<intStrs.length; i++){
            int num = Integer.parseInt(intStrs[i].substring(s,l+s));
            System.out.println(num);
            if(num > k){
                answer.add(num);
            }
        }
        return answer;
    }
}