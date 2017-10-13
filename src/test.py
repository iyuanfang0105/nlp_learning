# encoding=utf-8

import jieba
import jieba.posseg as posseg

jieba.load_userdict("../dict/food_dict.txt")

sentence = "哈哈哈，　吉他吃我爱吃酸辣粉和螺蛳粉"

# word segment
words = jieba.cut(sentence, cut_all=True)
print("Full Mode: " + ", ".join(words))
words = jieba.cut(sentence, cut_all=False)
print("Default Mode: " + ", ".join(words))
words = jieba.cut_for_search(sentence)
print("Search Model: " + ", ".join(words))

# part of speech
words = posseg.cut(sentence)
for word, flag in words:
    print word + ", " + flag
