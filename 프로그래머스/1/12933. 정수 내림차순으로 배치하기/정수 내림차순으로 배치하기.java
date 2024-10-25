import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        int num = String.valueOf(n).length();
        int[] tmp = new int[num];
        for(int i=0; i<num; i++){
            tmp[i] = (int)(n%10);
            n/=10;
        }
        Arrays.sort(tmp);
        for(int i=0; i<tmp.length; i++){
            answer+=tmp[i]*Math.pow(10,i);
        }
        return answer;
    }
}