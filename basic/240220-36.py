# Q. 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
#    구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.



# S. 10 ≤ price ≤ 1,000,000
#    price는 10원 단위로(1의 자리가 0) 주어집니다.
#    소수점 이하를 버린 정수를 return합니다.


def solution(price):
    if price>=500000:
        price = price-price*0.2
        
    elif price>=300000:
        price =price-price*0.1
        
    elif price>=100000 :
        price = price-price*0.05
        
    return int(price)

#!  if 문은 독립적으로 실행되므로 모든 조건이 참일 경우 해당하는 모든 블록이 실행됩니다. 
#!  elif 문은 가장 먼저 참이 되는 조건만 실행되며, 이후의 조건들은 검사되지 않습니다.

def solution(price):
    if price>=500000:
        return price-price*0.2
    if price>=300000:
        return price-price*0.1
    if price>=100000:
        return price-price*0.05