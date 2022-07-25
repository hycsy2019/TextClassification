import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python stopPriLib.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

content = open(file_name, 'rb').read()

jieba.analyse.set_stop_words("stop_words.txt")#此处写自己的停止词语料库
jieba.analyse.set_idf_path("userdict.txt");#此处写自己的idf语料库

tags = jieba.analyse.extract_tags(content, topK=topK)

print(",".join(tags))