# import jieba
#
# sent = '中文分词是文本处理不可或缺的一步'
#
# seg_list = jieba.cut(sent, cut_all=True)
#
# print('全模式：','/ '.join(seg_list))
#
# seg_list = jieba.cut(sent, cut_all=False)
#
# print('精确模式：','/ '.join(seg_list))

with open('G:\\learning-nlp\\chapter-3\\data\\news\\C000013\\10.txt', 'r') as file:
    content = ''
    for l in file:
        l = l.strip()
        content += l
        print(content)
