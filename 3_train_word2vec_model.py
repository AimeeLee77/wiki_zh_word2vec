#!/usr/bin/env python
# -*- coding: utf-8  -*-
#使用gensim word2vec训练脚本获取词向量

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')# 忽略警告

import logging
import os.path
import sys
import multiprocessing

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


if __name__ == '__main__':

    #print open('/Users/sy/Desktop/pyRoot/wiki_zh_vec/cmd.txt').readlines()
    #sys.exit()
    
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # inp为输入语料, outp1 为输出模型, outp2为原始c版本word2vec的vector格式的模型
    fdir = '/Users/sy/Desktop/pyRoot/wiki_zh_vec/'
    inp = fdir + 'wiki.zh.simp.seg.txt'
    outp1 = fdir + 'wiki.zh.text.model'
    outp2 = fdir + 'wiki.zh.text.vector'

    # 训练skip-gram模型
    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())

    # 保存模型
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)


