#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 18-7-3
@Author  : leemiracle
"""
import time
import nltk
from nltk.book import *


def first_chapter():
    '''
    文本搜索： 文本里找相似相近词
    统计信息：文本特征【词频、词分布】，输入特征【输入可近似 词的列表(Python 列表、字符串的操作)】
    多个词组成一个词向量：bigrams、ngrams

    待解决的问题：词义消歧、代词、 自动生成语言【问答、机器翻译】

    口语对话： phonology音韵学【pronunciation model 发音模型】、 morphology形态学【语言】【morphological rules形态规则】、syntax【句法：lexicon and grammar 词汇和语法】、
            semantics语义【discourse context话语语境】、reasoning推理【领域内知识】
    Textual Entailment文本蕴涵：Recognizing Textual Entailment (RTE)【蕴涵背景知识】
    :return:
    '''
    text1.concordance("monstrous") # concordance:查找包含目标词的句子
    text1.similar("monstrous") # similar:相似的语境
    text2.common_contexts(["monstrous", "very"]) # 列表词都出现的情况下，出现次数最多的词
    text1.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]) # 词的分布
    # text1.generate() # 生成文本


def second_chapter():
    '''
    text语料

    所有语料库类型：
        [
        'CorpusReader', 'CategorizedCorpusReader',
        'PlaintextCorpusReader', 'find_corpus_fileids',
        'TaggedCorpusReader', 'CMUDictCorpusReader',
        'ConllChunkCorpusReader', 'WordListCorpusReader',
        'PPAttachmentCorpusReader', 'SensevalCorpusReader',
        'IEERCorpusReader', 'ChunkedCorpusReader',
        'SinicaTreebankCorpusReader', 'BracketParseCorpusReader',
        'IndianCorpusReader', 'ToolboxCorpusReader',
        'TimitCorpusReader', 'YCOECorpusReader',
        'MacMorphoCorpusReader', 'SyntaxCorpusReader',
        'AlpinoCorpusReader', 'RTECorpusReader',
        'StringCategoryCorpusReader','EuroparlCorpusReader',
        'CategorizedBracketParseCorpusReader',
        'CategorizedTaggedCorpusReader',
        'CategorizedPlaintextCorpusReader',
        'PortugueseCategorizedPlaintextCorpusReader',
        'tagged_treebank_para_block_reader',
        'PropbankCorpusReader', 'VerbnetCorpusReader',
        'BNCCorpusReader', 'ConllCorpusReader',
        'XMLCorpusReader', 'NPSChatCorpusReader',
        'SwadeshCorpusReader', 'WordNetCorpusReader',
        'WordNetICCorpusReader', 'SwitchboardCorpusReader',
        'DependencyCorpusReader', 'NombankCorpusReader',
        'IPIPANCorpusReader', 'Pl196xCorpusReader',
        'TEICorpusView', 'KNBCorpusReader', 'ChasenCorpusReader',
        'CHILDESCorpusReader', 'AlignedCorpusReader',
        'TimitTaggedCorpusReader', 'LinThesaurusCorpusReader',
        'SemcorCorpusReader', 'FramenetCorpusReader', 'UdhrCorpusReader',
        'BNCCorpusReader', 'SentiWordNetCorpusReader', 'SentiSynset',
        'TwitterCorpusReader', 'NKJPCorpusReader', 'CrubadanCorpusReader',
        'MTECorpusReader', 'ReviewsCorpusReader', 'OpinionLexiconCorpusReader',
        'ProsConsCorpusReader', 'CategorizedSentencesCorpusReader',
        'ComparativeSentencesCorpusReader', 'PanLexLiteCorpusReader',
        'NonbreakingPrefixesCorpusReader', 'UnicharsCorpusReader',
        'MWAPPDBCorpusReader',]
    词汇：corpus模块
        word list：[nltk.corpus.gutenberg.words(), nltk.corpus.nps_chat.words(), nltk.corpus.stopwords.words(), nltk.corpus.names]
        Pronouncing Dictionary[发音字典]：nltk.corpus.cmudict.entries()
        Comparative Wordlists【比较词:相对其他语言】：nltk.corpus.swadesh
        Shoebox and Toolbox Lexicons【工具词典】：nltk.corpus.toolbox.entries('rotokas.dic')
        WordNet(面向语义的词典：nltk.corpus.wordNet)： 同义词[wn.synsets('motorcar') -->所有定义过该词的[Synset('car.n.01')]-->所有的近义词wn.synset('car.n.01').lemma_names()]
            同义词的层级(wn.synset('car.n.01').hyponyms())
            词汇的关系：wn.synset('tree.n.01').part_meronyms()、wn.synset('tree.n.01').substance_meronyms()、wn.synset('tree.n.01').member_holonyms()等synset的成员函数
            语义的相似性【wn.synset('motorcar').lowest_common_hypernyms(wn.synset('minke_whale.n.01'))】
    :return:
    '''
    nltk.corpus.gutenberg.CorpusView()

def third_chapter():
    '''
    处理原始文本

    1.从网络下载文本：a.下载 b.word_tokenize[词向量化] c. nltk.Text(tokens:词列表)
    2.处理html：BeautifulSoup(html).get_text(
    3.处理搜索引擎的结果
    4.RSS Feeds【feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")】
    5.本地文件：open('document.txt')
    6.用户输入：input()

    处理字符串的方法
    字符串编码
    正则表达式处理 word pattern： a.提取词re.findall() b.查找词干

    规范化文本： a.词干 b.Lemmatization词形还原
    nltk的正则表达式：nltk.regexp_tokenize(text, pattern)

    分割：
        句子的分割
        词的分割

    format：把list变成字符串的方法
    :return:
    '''
    pass

def fourth_chapter():
    '''
    结构化编程

    变量作用范围：local global build-in
    函数的使用： Documenting Functions， 高阶
    :return:
    '''

def main():
    while True:
        s = input("haha: ")
        time.sleep(1)
        print("leemiracle: {}".format("笑什么"))


if __name__ == '__main__':
    main()
