"""
计算列表的和

递归  不使用循环
递归也是一种迭代
递归是一种解决问题的方法，他把问题分解为越来越小的子问题
直到问题的规模小到可以被很简单直接解决
通常为了达到分解问题的效果。递归过程中要引入一个（调用自身的函数）


def list_sum(li):
    if len(li) == 1:
        return li[0]
    else:
        return li[0]+list_sum(li[1:])

print(list_sum([1,2,3,4,5,6]))
"""
# li = [1,2,3,4,5,6,7]
# sum = li[0] if len(li)==1 else li[0]+sum(li[1:])
# print(sum)

# def list_num(num_list):
#     i = 0
#     if len(num_list) == 1:
#         print('列表长度',len(num_list))
#         return num_list[0]
#     else:
#         i+=1
#         print('else:',num_list[0] + list_num(num_list[1:]))
#         return num_list[0] + list_num(num_list[1:])
        
# print(list_num([1,2,3,4,5,6]))


def to_str(num,base):
    convert_str = '012345678ABCDEF'
    if num < base:
        return convert_str[num]
    else:
        return to_str(int(num//base),base) + convert_str[num%base]

print(to_str(769,10))