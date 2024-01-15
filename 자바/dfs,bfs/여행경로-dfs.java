import java.util.*;
class Solution {

    public String[] solution(String[][] tickets) {
        List<String> answer = new ArrayList<>();
        boolean[] visited = new boolean[tickets.length];

        dfs("ICN", "ICN", tickets, answer, visited, 0);

        Collections.sort(answer);           // 여행 경로가 다양하게 나오는데 이중 알파벳순이라고 했으므로 정렬

        return answer.get(0).split(" ");    // "ICN SFO ATL" 같이 공백으로 구분했고 알바벳순으로 정렬한 제일 앞의 여행경로가 정답이므로
                                            //  첫번째항의 각 공백을 기준으로 String 배열로 변환
    }


    private void dfs(String start, String path, String[][] tickets, List<String> answer, boolean[] visited, int depth) {
        if (depth == tickets.length) {      // 주어진 티켓을 모두 조회했다면
            answer.add(path);               // 현재까지의 여행 경로를 정답 리스트에 추가하고 반환
            return;
        }

        for (int i = 0; i < tickets.length; i++) {
            if (start.equals(tickets[i][0]) && !visited[i]) {
                visited[i] = true;  // 방문했음으로 설정하고
                dfs(tickets[i][1], path + " " + tickets[i][1], tickets, answer, visited, depth + 1); // 재귀를 하고
                visited[i] = false; // for문 다음 조회에서 방문한 티켓을 다시 방문할 수 있어야하므로 방문안함으로 다시 설정
            }
        }
    }
}