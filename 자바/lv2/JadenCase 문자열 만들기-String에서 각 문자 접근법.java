import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";

        StringBuilder sb = new StringBuilder();     // 문자를 이어 붙일 StringBuilder 클래스

        for (int i=0; i<s.length(); i++) {          // 기존 문자열에서 조회 String의 길이는 length();이다.
            String temp = "";

            if (i == 0 || s.charAt(i-1) == ' ') {   // 첫번째이거나 앞 문자가 공백이면 첫단어의 첫문자이므로
                temp = String.valueOf(s.charAt(i)); // 문자를 가져오고 문자열로 다시 변환해준 후
                sb.append(temp.toUpperCase());      // 문자열에 대문자로 변환하고 삽입
            }
            else {                                  // 공백이거나 그외 문자들은 모두 소문자로 나타내라고 했으므로
                temp = String.valueOf(s.charAt(i)); // 문자를 가져오고 문자열로 다시 변환해준 후
                sb.append(temp.toLowerCase());      // 문자열에 소문자로 변환하고 삽입
            }
        }

        answer = sb.toString();                     // StringBuilder를 문자열로 변환해주고 정답에 넣기

        return answer;
    }
}