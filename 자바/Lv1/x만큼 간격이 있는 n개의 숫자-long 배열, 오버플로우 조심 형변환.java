class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];           // 배열 생성
        answer[0] = x;

        for (int i=1; i<n; i++) {
            answer[i] = (long)x * (i+1);       // 오버플로우 조심하기 위해 long으로 형변환 후 넣어주기
        }

        // for (int i=1; i<n; i++) {
        //     answer[i] = answer[i-1] + x;
        // }

        return answer;
    }
}