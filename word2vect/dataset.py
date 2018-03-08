# coding=utf-8
import argparse
import sys
import re
import jieba

reload(sys)
sys.setdefaultencoding("utf-8")

parser = argparse.ArgumentParser()
parser.add_argument('--corpus', type=str, default='/home/meizu/WORK/public_dataset/sougou_CA_corpus/corpus.txt', help='the path of corpus')
parser.add_argument('--output', type=str, default='/home/meizu/WORK/public_dataset/sougou_CA_corpus/corpus_seg.txt', help='the output file')

FLAGS = parser.parse_args()

if FLAGS.corpus == '':
    print '===>>> Please set the corpus path'
    sys.exit(-1)
if FLAGS.output == '':
    print '===>>> Please set the output path'
    sys.exit(-1)

print '===>>> Corpus: ' + FLAGS.corpus
print '===>>> output: ' + FLAGS.output


# 正则将<content>和</content>去掉
def my_re(content):
    s = re.sub('<content>|</content>', '', content)
    return s

input_file = open(FLAGS.corpus)
output_file = open(FLAGS.output, 'w')
count = 0
for line in input_file:
    line_seg = jieba.cut(my_re(line))
    output_file.write(' '.join(line_seg))
    count = count + 1
    if count % 1000 == 0:
        print "Precessing " + str(count) + " lines"

input_file.close()
output_file.close()
print "Finished Saved "
