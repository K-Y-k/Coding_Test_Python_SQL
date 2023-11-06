// nums의 숫자가 포켓몬 종류로 종류별로 딕셔너리에 담아 개수를 카운팅한다.
// nums의 총 개수의 절반이 포켓몬을 가져갈 수 있는 최대 개수이므로
// 종류별로 담은 딕셔너리의 총 길이에 따른 포켓몬 종류 개수를 출력할 수 있다.


import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;

        Map<Integer, Integer> pocketDic = new HashMap<>();

        for (int i : nums) {
            if (!pocketDic.containsKey(i)) {
                pocketDic.put(i, 1);
            } else {
                pocketDic.put(i, pocketDic.get(i) + 1);
            }
        }

        int count = nums.length / 2;

        int resultCount = pocketDic.size() - count;

        if (resultCount >= 0) {
            answer = count;
        } else {
            answer = pocketDic.size();
        }

        return answer;
    }
}