import glob
import random
import jieba
import chapter3.cut_word as help

# glob是一个操作文件的模块，主要获取指定路径下的所有匹配文件列表
files = glob.glob('G:\\learning-nlp\\chapter-3\\data\\news\\C000013\\*.txt')
corpus = [help.get_content(x) for x in files]

# randint 返回一个0-1990之间的随机数
sample_inx = random.randint(0, len(corpus))
split_words = list(jieba.cut(corpus[sample_inx]))
#print('样本之一：' + corpus[sample_inx])
#print('样本分词效果：' + '/ '.join(split_words))
print('样本的topK(10)词：' + str(help.get_TF(split_words)))

