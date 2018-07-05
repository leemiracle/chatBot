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
    pass


def fifth_chapter():
    '''
    word分类以及标签化

    读已经被标记过的语料
    通用的词性标注集

    Python字典：词性

    自动标记
        默认标记：tags = [tag for (word, tag) in brown.tagged_words(categories='news') （已经标记好的）
        正则表达式tagger
            >>> patterns = [
            ...     (r'.*ing$', 'VBG'),               # gerunds
            ...     (r'.*ed$', 'VBD'),                # simple past
            ...     (r'.*es$', 'VBZ'),                # 3rd singular present
            ...     (r'.*ould$', 'MD'),               # modals
            ...     (r'.*\'s$', 'NN$'),               # possessive nouns
            ...     (r'.*s$', 'NNS'),                 # plural nouns
            ...     (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
            ...     (r'.*', 'NN')                     # nouns (default)
            ... ]
        Lookup Tagger：
            likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
            baseline_tagger = nltk.UnigramTagger(model=likely_tags)
            baseline_tagger.evaluate(brown_tagged_sents)

        N-Gram Tagging：
            Unigram Tagging【nltk.UnigramTagger(brown_tagged_sents)】：分开training和testing
            General N-Gram Tagging
        联合taggers：
        标注未知words

        存储tagger：pickle.dump pickle.load

        性能限制：

        基于转换的标记

        词的分类：形态、句法、语义、新词、语音标签集的形态学
    :return:
    '''
    # text = word_tokenize("And now for something completely different")
    # nltk.pos_tag(text) # 打tag
    pass

def six_chapter():
    '''
    文本分类：常用的统计模型介绍，以及在文本处理上的应用
    监督学习：
        1.名字识别性别
        2.特征选择
        3.文档分类
        4.词性标注
        5.语境
        6.Sequence序列 Classification
    实例
        7.语句分割
        8.识别对话的Act Types
        9.识别文本蕴涵Textual Entailment
        10.提高样本集
    Evaluation 评估：
        1.测试集
        2.精度
        3.准确度和recall【召回率】
        4.混淆矩阵
        5.交叉验证
    决策树：
        1.熵和信息增益
    朴素贝叶斯分类器
        1.基础概率模型
        2.Zero Counts and Smoothing平滑
        3.Non-Binary Features
        4.独立性
        5.造成 Double-Counting
    最大熵Classifiers：
        1.最大熵模型
        2.最大化熵
        3.生成分类器 vs 条件分类器
    语言模式建模
    :return:
    '''
    pass

def seventh_chapter():
    '''
    文本信息提取： 类似知识图谱

    1.架构：文本-->语句分割-->tokenization-->part of speech tagging--> 实体检测--> 关系检测-->relations
    2.chunking分块：
        名词语句
        tag pattern
        正则表达式
        文本语料库
        Chinking：语法
        表示 语句块：标签 vs 树
    3.Chunkers：
        读取IOB格式 和 CoNLL 2000语料库
        基准
        训练基于分类的Chunkers
    4.语言结构的递归
           Cascaded级联 Chunkers的网状结构
           树状
           树的遍历
    5.命名实体的识别
    6.关系提取

    :return:
    '''
    pass

def eighth_chapter():
    '''
    分析句子结构

    语法困境：
        1.语言数据及其无限可能性
        2.无处不在的歧义
    什么时候使用语法：
        1.n-grams
    上下文free文法
        2.自己的文法
        3.句法结构中的递归
    使用Context Free Grammar解析
        1.递归下降 解析
        2.Shift-Reduce 解析
        3.Left-Corner 解析器
        4.Well-Formed 子串表
        5. Dependencies and Dependency 语法
    语法扩展：
        1. Treebanks 和 Grammars
        2.歧义
        3.加权语法
    :return:
    '''
    pass


def ninth_chapter():
    '''
    基于特征的语法
    1.语法特征
        句法协议
        使用属性和约束
        术语
    2.处理特征结构： 共有的特征结构
    3.扩展
        次范畴
        heads的重访问
        辅助动词 和 Inversion
        无限的依赖结构
        德语的例子
    :return:
    '''
    pass


def tenth_chapter():
    '''
    分析句子的意思

    1.自然语言的理解：
        查询数据库
        自然语言，语义和逻辑
    2.命题逻辑
    3.一阶逻辑的语言
        句法
        一阶定理证明
        模型：构建
        变量
        定量
        量词范围模糊
    4.英语的语义学
        基于特征的
        λ-演算子
        NPs量化
        及物动词
    5.话语语义学
        话语表征理论
        话语处理
    :return:
    '''
    pass


def eleventh_chapter():
    '''
    管理语言数据
    1.语料结构【实例】
        TIMIT【设计特点】【基本数据类型】
    2.语料的生命周期
        语料的创建场景
        质量控制
        策划与进展
    3.获取数据
        web
        字处理器文件中获取
        表格和数据库
        转换数据格式
        决定要包含哪些注释层
        标准工具
        使用濒危语言时的特殊注意事项
    4.处理xml
        xml作为语言的结构
        xml的角色
        ElementTree接口
        使用ElementTree接口访问Toolbox类的数据
        实体Formatting
    5.处理Toolbox的数据
        添加一个字段给每个Entry
        验证Toolbox的词汇
    6.使用OLAC Metadata描述 语言资源【OLAC: Open Language Archives Community】
    :return:
    '''
    pass


def twelfth_chapter():
    '''
    语言学的挑战

    1.作为语言来处理 vs 作为符号来处理
    2.哲学分歧
    3.nltk roadmap
    :return:
    '''


def main():
    while True:
        s = input("haha: ")
        time.sleep(1)
        print("leemiracle: {}".format("笑什么"))


if __name__ == '__main__':
    main()
