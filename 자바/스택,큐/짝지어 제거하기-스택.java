/**
 * 스택에 쌓아가면서 비교하면 짝을 처리할 수 있다.
 */

import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;

        Stack<String> stack = new Stack<>();

        String[] s_arr = s.split("");

        for (String sa : s_arr) {
            if (stack.isEmpty()) {                    // 비어있으면 값 넣기
                stack.push(sa);
            } else if (stack.peek().equals(sa)) {     // 비어있지 않고 스택의 제일 위 값과 일치하면 
                stack.pop();                          // 제일 위 값 꺼내기
            } else {                                
                stack.push(sa);                       // 제일 위 값과 일치하지 않으면 값 넣기
            }
        }

        if (stack.isEmpty()) {                        // 비어있으면 모든 짝이 맞았으므로 1 반환
            answer = 1;
        }

        return answer;
    }
}