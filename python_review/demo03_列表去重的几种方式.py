origin_list=[4,2,1,3,5,3,1]
#方法１,利用set集合去重 不会保留原来列表中的元素顺序
print(list(set(origin_list)))

#方法二:利用字典中键的唯一性　不会保留原来列表中的元素顺序
print("方法二．．．．．．．．．．．．．．．．．．．．．．．．．．．．．")
dict1=dict.fromkeys(origin_list,10)
print(list(dict1))

#方法三：创建一个新列表,会保留原来列表中元素的顺序
print("方法三．．．．．．．．．．．．．．．．．．．．．．．．．．．．．．．")
new_list=[]
for i in origin_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)