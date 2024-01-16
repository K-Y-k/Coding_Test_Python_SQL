import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();

        List<Integer> num_list = new ArrayList<>();                // 숫자를 비교할 리스트 생성

        String[] s_arr = s.split(" ");                             // 공백을 기준으로 String 배열로 분리하고

        for (String st : s_arr) {                                  // 각 배열을 조회하며
            num_list.add(Integer.parseInt(st));                    // String을 숫자로 변환후 숫자 리스트에 넣고
        }

        answer += String.valueOf(Collections.min(num_list));       // 리스트의 최솟값을 먼저 넣고
        answer += " " + String.valueOf(Collections.max(num_list)); // 공백후 최댓값을 넣는다.


        answer.append(String.valueOf(Collections.min(num_list))); // 숫자 리스트의 최솟값을 먼저 넣고
        answer.append(" ");                                       // 공백후
        answer.append(String.valueOf(Collections.max(num_list))); // 최댓값을 넣는다.


        return answer.toString();                                 // String으로 변환 후 반환
    }
}