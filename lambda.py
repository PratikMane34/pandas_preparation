#lambda function with sorted method
people= [
    { "name":"Alice","age":30,"department":"store"},
    {"name":"Bob","age":35,"department":"HR"},
    {"name":"Charlie","age":25,"department":"production"}
]
sorted_people = sorted(people,key=lambda x:x['department'])
print(sorted_people)