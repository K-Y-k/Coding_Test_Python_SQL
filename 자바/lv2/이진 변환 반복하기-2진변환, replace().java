class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int count = 0;                                   // 반복 횟수 초기화
        int deleteZeroCount = 0;                         // 0을 제거한 총 개수 초기화

        while (!s.equals("1")) {                         // "1"이 될 때까지 반복
            String[] s_arr = s.split("");

            for (String sa : s_arr) {
                if (sa.equals("0")) {
                    s = s.replace("0", "");
                    deleteZeroCount++;
                }
            }

            // s = s.replaceAll("0", "");                // 전체를 기준으로 변경하려면
            s = Integer.toBinaryString(s.length());      // 현재 10진수를 2진수로 변환 후 String형으로 변환
            count++;
        }

        answer[0] = count;
        answer[1] = deleteZeroCount;

        return answer;
    }
}