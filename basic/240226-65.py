# Q. 문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을,
#    만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

# S. 0 < before의 길이 == after의 길이 < 1,000
#    before와 after는 모두 소문자로 이루어져 있습니다.


def solution(before, after):
    a=list(before)
    b=list(after)
    a.sort()
    b.sort()
    if a==b:
        return 1
    else:
        return 0

before = "allefd"
after="apple"

#! 주의
# list(before.sort()) , sort()
# sort() 메서드는 원본 리스트를 정렬하고, 반환 값은 None

# def solution(before, after):
#     before=sorted(before)
#     after=sorted(after)
#     if before==after:
#         return 1
#     else:
#         return 0