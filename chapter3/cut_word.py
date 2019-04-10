# 读取指定路径下的文件，按行\n读取文件
def get_content(path):
    with open(path, 'r', encoding='gbk', errors='ignore') as file:
        content = ''
        for l in file:
            l = l.strip()
            content += l
        return content


# 高频词统计函数
def get_TF(words, topK=10):
    tf_dic = {}
    # for循环使用字段来计数出现的次数，dict.get(key, default).未找到则返回default
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0) + 1
    # 当待排序列表的元素由多字段构成时，我们可以通过sorted(iterable，key，reverse)的参数key来制定我们根据那个字段对列表元素进行排序。
    # 　　key=lambda 元素: 元素[字段索引]
    # 　　例如：想对元素第二个字段排序，则
    # 　　key=lambda y: y[1] 备注：这里y可以是任意字母，等同key=lambda x: x[1]

    return sorted(tf_dic.items(), key=lambda x: x[1], reverse=True)[:topK]
