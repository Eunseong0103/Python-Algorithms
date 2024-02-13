# Q. 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.


# S. 1 ≤ num_list의 길이 ≤ 1,000
#    0 ≤ num_list의 원소 ≤ 1,000

def solution(num_list):
  
    return list(reversed(num_list))


#!! list.reverse() 메서드는 None을 반환하며, 원래의 리스트를 역순으로 변경합니다.
#!! 따라서 return num_list.reverse()는 항상 None을 반환할 것입니다.