#字典的排序
infors= [{"name":"A","age":4},{"name":"B","age":2},{"name":"C","age":3}]

infors.sort(key=lambda x:x['age'])

print(infors)
