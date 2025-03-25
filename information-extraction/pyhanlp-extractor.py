# 基于hanlp信息抽取
# 参考资料：https://www.cnblogs.com/Gimm/p/18205237
# 2025-02-17

from pyhanlp import *
sentence=u'''今天是xxx等老一辈革命家为雷锋同志题词60周年，xxx***近日作出重要指示指出，雷锋的名字家喻户晓，雷锋的事迹深入人心，雷锋精神滋养着一代代中华儿女的心灵。党的十八大以来，xxx***对弘扬雷锋精神作出一系列重要论述，指导推动新时代学雷锋活动不断拓展内容、创新形式、丰富载体、涌现出一批又一批雷锋式先进集体和模范人物，为新时代伟大变革注入不竭精神动力。今天，党建网梳理了xxx***部分相关重要论述，邀您一起学习领会。'''
words=HanLP.segment(sentence)
for item in words:
	print(item.word,item.nature)
# 关键词提取
keyword_list=HanLP.extractKeyword(sentence,5) #提取五个关键词
# 文本摘要
summary_list=HanLP.extractSummary(sentence,2) #提取文本中两个关键句作为摘要
# 依存句法分析
Denpency_lst=HanLP.parseDepency(sentence)
# 短句提取 
phrase_list=HanLP.extractPhrase(sentence,5)
# 词性切分
analyzer=PerceptronLexicalAnalyzer()
segs=analyzer.analyze(sentence)
arr=str(segs).split(" ")

def get_result(arr):
	re_list=[]
	ner=['n','ns']
	for x in arr:
		temp=x.split("/")
		if (temp[1] in ner):
			re_list.append(temp[0])
	return re_list
	

# 使用jieba
import jieba.analyse
# 词性切分
kw=jieba.analyse.extract_tags(sentence,allowPOS=('n','ns'))
kw01=jieba.analyse.textrank(sentence,allowPOS=('n','ns'))
for item in kw01:
	print(item)
