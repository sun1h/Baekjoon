import java.util.*;

class Solution {
    public ArrayList solution(int[] arr, int[] delete_list) {
        ArrayList lst = new ArrayList<>();
        for(int num : arr) {
            lst.add(num);
        }
        
        for(int i=0; i<delete_list.length;i++){
            if(lst.contains(delete_list[i])){
               lst.remove(Integer.valueOf(delete_list[i]));
            }
        }
        return lst;
    }
}