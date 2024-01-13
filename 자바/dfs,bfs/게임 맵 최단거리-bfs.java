import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;

        int n = maps.length;
        int m = maps[0].length;

        boolean[][] visited = new boolean[n][m];
        int[][] distance = new int[n][m];
        distance[0][0] = 1;

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        bfs(maps, n, m, visited, distance, dx, dy);

        if (!visited[n-1][m-1]) {
            answer = -1;
        } else {
            answer = distance[n-1][m-1];
        }

        return answer;
    }

    private static void bfs(int[][] maps, int n, int m, boolean[][] visited, int[][] distance, int[] dx, int[] dy) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];

            for (int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0<=nx&&nx<n && 0<=ny&&ny<m) {
                    if (!visited[nx][ny] && maps[nx][ny] == 1) {
                        visited[nx][ny] = true;
                        distance[nx][ny] = distance[x][y] + 1;
                        q.offer(new int[]{nx, ny});
                    }
                }
            }
        }
    }
}