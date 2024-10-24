class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        if(arr1.length>arr2.length){
            answer = 1;
        }else if (arr1.length<arr2.length){
            answer = -1;
        }else{
            int sumArr1 = sumArr(arr1);
            int sumArr2 = sumArr(arr2);
        
            if(sumArr1>sumArr2){
                answer = 1;
            }else if(sumArr1<sumArr2){
                answer = -1;
            }
        }
        return answer;
    }
    
    public int sumArr(int[] arr){
        int ans = 0;
        for(int i=0; i<arr.length; i++){
            ans+=arr[i];
        }
        return ans;
    }
}