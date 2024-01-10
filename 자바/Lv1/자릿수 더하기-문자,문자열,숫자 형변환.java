import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        String str = String.valueOf(n);

        for (int i=0; i<str.length(); i++) {
            char c = str.charAt(i);

             answer += Character.getNumericValue(c);
//            answer += Integer.parseInt(String.valueOf(c));
        }

//        다른 방식 : 문자열 배열로 문자를 담고 각 문자열을 숫자로 변환
//        String[] strArr = str.split("");
//        for (String s : strArr) {
//            answer += Integer.parseInt(s);
//        }


        return answer;
    }
}