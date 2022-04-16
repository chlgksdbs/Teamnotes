data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# 2차원 리스트(행렬)를 90도로 회전하는 함수
def rotate_matrix(data):
    row_len = len(data) # 행 길이 계산
    column_len = len(data[0]) # 열 길이 계산

    graph = [[0] * row_len for _ in range(column_len)] # 회전 결과를 담을 리스트

    for i in range(row_len):
        for j in range(column_len):
            graph[j][row_len - i - 1] = data[i][j]
    
    return graph

print(rotate_matrix(data))
