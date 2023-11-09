// 스택에는 '('만 넣고 ')'이 올 때 스택의 '('을 지워주면서
// 모두 조회되었는데도 스택이 비어있지 않으면 짝이 안 맞았다는 것

import java.util.*;

public class Solution {

    public static boolean solution(String s) {
        boolean answer = true;

        Stack<Character> stack = new Stack<>();    // '('만 넣을 스택

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {                        // '('이면 스택에 넣어주기
                stack.push('(');
            } else if (s.charAt(i) == ')') {                 // ')'이면
                if (!stack.isEmpty()) {            // 스택에서 '(' 지워주기
                    stack.pop();
                } else {                           // 스택 안이 비어있으면 짝이 안맞으므로 False 적용
                    answer = false;
                }
            }
        }

        if (!stack.isEmpty()) {                    // 위 괄호 묶기를 모두 처리했는데도 스택 안에 남아있는 경우 False 적용
            answer = false;               
        }

        return answer;
    }
}