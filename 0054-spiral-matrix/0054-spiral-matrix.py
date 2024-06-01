class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)  # 행렬의 세로 길이
        m = len(matrix[0])  # 행렬의 가로 길이
        
        # y축, x축 이동방향 배열 (오른쪽, 아래, 왼쪽, 위)
        dir_y = [0, 1, 0, -1]
        dir_x = [1, 0, -1, 0]
        
        visited = [[0] * m for _ in range(n)]  # 방문 여부를 체크하는 배열
        answer = []  # 결과를 저장할 배열
        
        y, x = 0, 0  # 시작 좌표
        dir = 0  # 처음 이동 방향은 오른쪽
        
        for _ in range(n * m):
            answer.append(matrix[y][x])
            visited[y][x] = 1
            
            # 다음 좌표 계산
            next_y = y + dir_y[dir]
            next_x = x + dir_x[dir]
            
            # 다음 좌표가 유효한지 체크 (범위를 벗어나지 않고, 방문하지 않은 위치)
            if 0 <= next_y < n and 0 <= next_x < m and not visited[next_y][next_x]:
                y, x = next_y, next_x
            else:
                # 다음 좌표가 유효하지 않으면 방향 전환
                dir = (dir + 1) % 4
                y += dir_y[dir]
                x += dir_x[dir]
        
        return answer