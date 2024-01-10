import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;

        String[] str_arr = String.valueOf(n).split("");   // 각 문자를 배열로 나누기

        Arrays.sort(str_arr);                             // 배열을 오름차순으로 정렬

        StringBuilder sb = new StringBuilder();           // 문자열을 이어붙이기 위한 StringBuilder 선언

        for (String s : str_arr) {
            sb.append(s);                                 // 문자열 연결
        }

        sb.reverse();                                     // 문자열 뒤집기

        answer = Long.parseLong(sb.toString());           // 문자열 -> long 변환
                                                          // StringBuilder는 toString()으로 String 형태로 변환해야한다.

        return answer;
    }
}