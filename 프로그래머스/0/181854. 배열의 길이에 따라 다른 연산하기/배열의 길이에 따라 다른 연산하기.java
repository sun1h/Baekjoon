class Solution {
    public int[] solution(int[] arr, int n) {
        int le = arr.length;
        int[] answer = new int[le];
        
        if(le%2!=0){
            for(int i=0; i<le; i+=2){
                arr[i]+=n;
            }
        }else{
            for(int i=1; i<le; i+=2){
                arr[i]+=n;
            }
        }
        
        return arr;
    }
}