import bisect

# 값이 [left_value, right_value] 범위에 있는 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    left_index = bisect.bisect_left(array, left_value)
    right_index = bisect.bisect_right(array, right_value)
    return right_index - left_index


# 리스트 선언
array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 7, 8, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(array, 4, 4))

# 값이 array [-2, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(array, -2, 3))