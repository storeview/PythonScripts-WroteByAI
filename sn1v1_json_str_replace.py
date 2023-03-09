"""
给定一个 JSON 字符串(json_str)和一组字符串(fields), 
    遍历该JSON(json_str)中的每一个key-value, 如果key没有包含在fields中, 
    且该key所对应的value值使用{{$DoNotCompare}}进行替换, 
    如果是对象或列表, 则将该对象或列表下的所有键的value值都用{{$DoNotCompare}}替换, 
    如果遇到对象或列表, 则继续进入其中进行处理.
"""

import json

def replace_value(json_str, fields):
    # 将 JSON 字符串转换为 Python 字典
    json_dict = json.loads(json_str)
    # 定义一个递归函数，用于遍历字典中的每个键值对
    def traverse_dict(d):
        # 如果 d 是一个字典
        if isinstance(d, dict):
            # 遍历 d 中的每个键值对
            for k, v in d.items():
                # 如果 k 不在 fields 中
                if k not in fields:
                    # 如果 v 是一个对象或列表
                    if isinstance(v, (dict, list)):
                        # 将 v 下的所有键的值都替换为 {{$DoNotCompare}}
                        replace_all(v)
                    else:
                        # 否则，将 v 替换为 {{$DoNotCompare}}
                        d[k] = "{{$DoNotCompare}}"
                else:
                    # 否则，继续递归遍历 v
                    traverse_dict(v)
        # 如果 d 是一个列表
        elif isinstance(d, list):
            # 遍历 d 中的每个元素
            for i in range(len(d)):
                # 如果 d[i] 是一个对象或列表
                if isinstance(d[i], (dict, list)):
                    # 将 d[i] 下的所有键的值都替换为 {{$DoNotCompare}}
                    replace_all(d[i])
                else:
                    # 否则，将 d[i] 替换为 {{$DoNotCompare}}
                    d[i] = "{{$DoNotCompare}}"

    def replace_all(obj):
        # 如果 obj 是一个字典
        if isinstance(obj, dict):
            # 遍历 obj 中的每个键值对
            for k in obj.keys():
                # 将 obj[k] 的值都替换为 {{$DoNotCompare}}
                obj[k] = "{{$DoNotCompare}}"
        # 如果 obj 是一个列表
        elif isinstance(obj, list):
            # 遍历 obj 中的每个元素
            for i in range(len(obj)):
                # 将 obj[i] 的值都替换为 {{$DoNotCompare}}
                obj[i] = "{{$DoNotCompare}}"

    traverse_dict(json_dict)
    return json.dumps(json_dict)

# 测试代码

json_str = '{"name": "Alice", "age": 20, "hobbies": ["reading", "writing"], "friends": [{"name": "Bob", "age": 21}, {"name": "Charlie", "age": 22}]}'
fields = ["name", "hobbies"]

result = replace_value(json_str, fields)

print(result)