# Q. 사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다. 사분면은 아래와 같이 1부터 4까지 번호를매깁니다.
# x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.
# x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.
# x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.
# x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.

# S. 1 ≤ num_list의 길이 ≤ 100
#    0 ≤ num_list의 원소 ≤ 1,000

def solution(dot):
    if dot[0]>0:
        if dot[1]>0:
            return 1
        else:
            return 4
    else:
        if dot[1] >0:
            return 2
        else:
            return 3