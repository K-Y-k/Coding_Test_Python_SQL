// 딕셔너리를 사용한 방식: 전체 참여자를 하나씩 딕셔너리에 카운팅해 놓은 것을
//                     완주자를 조회할 때 하나씩 카운팅을 감소시켜서 최종 카운팅이 1인 것이 완주 못한 자가 나오게함

import java.util.*;

public class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        Map<String, Integer> hashDic = new HashMap<>();

        for (String name : participant) {                   // 전체 참여자를 하나씩 딕셔너리에 카운팅해 놓음
            if (hashDic.containsKey(name)) {
                hashDic.put(name, hashDic.get(name) + 1);
            } else {
                hashDic.put(name, 1);
            }
        }

        for (String name : completion) {                    // 완주자를 조회하면서 딕셔너리에 있으면
            if (hashDic.containsKey(name)) {
                hashDic.put(name, hashDic.get(name) - 1);   // -1 카운팅
            }
        }

        for (String name : hashDic.keySet()) {              // 딕셔너리를 조회하여
            if (hashDic.get(name) == 1) {                   // 1인 값이 결국 완주하지 못한 자이므로
                answer = name;                              // 답에 적용
                break;
            }
        }

        return answer;
    }
}


