import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];


        for (int i=0; i<n; i++) {
            if (!visited[i]) {
                bfs(i, computers, visited, n);
                answer++;
            }
        }

        return answer;
    }

    private static void bfs(int x, int[][] computers, boolean[] visited, int n) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(x);

        while (!q.isEmpty()) {
            int i = q.poll();

            for (int j=0; j<n; j++) {
                if (computers[i][j] == 1 && !visited[j]) {
                    visited[j] = true;
                    q.offer(j);
                }
            }
        }
    }
}