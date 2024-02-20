# Q. 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# S. 1 ≤ my_string의 길이 ≤ 1,000
#    my_string은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.

def solution(my_string):
    count=0
    for i in my_string:
        if i.isdigit():
            count+=int(i)
    return count


# def solution(my_string):
#     return sum(int(i) for i in my_string if i.isdigit())