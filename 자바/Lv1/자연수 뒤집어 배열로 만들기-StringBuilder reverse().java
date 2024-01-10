// 배열의 길이는 배열명.length고 String 관련 클래스는 문자명.length()다!
class Solution {
    public int[] solution(long n) {
        String s = String.valueOf(n);
        int[] answer = new int[s.length()];            // 배열의 길이는 배열명.length고 String 관련 클래스는 문자명.length()다!

        StringBuilder sb = new StringBuilder(s);
        sb.reverse();

        String[] str_arr = sb.toString().split("");

        for (int i=0; i<s.length(); i++) {
            answer[i] = Integer.parseInt(str_arr[i]);
        }

        return answer;
    }
}