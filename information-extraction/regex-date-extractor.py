# -*- coding:utf-8 -*-
# @project: transcoding_stopword.py
# @filename: 时间实体识别.py
# @author: GaGim-H
# @github: https://github.com/GaGim-H
# @time:  2024/05/22 19:15


import re
from datetime import datetime, timedelta
from dateutil.parser import parse
import jieba.posseg as psg

UTIL_CN_NUM = {
    '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6,
    '七': 7, '八': 8, '九': 9, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}

UTIL_CN_UNIT = {'十': 10, '百': 100, '千': 1000, '万': 10000}


# 文本转换成数字
def cn2dig(src):
    if src == "":
        return None
    # 匹配数字
    m = re.match("\d+", src)
    if m:
        return int(m.group(0))

    rsl = 0
    unit = 1
    for item in src[::-1]:
        if item in UTIL_CN_UNIT.keys():
            unit = UTIL_CN_UNIT[item]
        elif item in UTIL_CN_NUM.keys():
            num = UTIL_CN_NUM[item]
            rsl += num * unit
        else:
            return None
    if rsl < unit:
        rsl += unit
    return rsl


# 文本转换成数字
def year2dig(year):
    res = ""
    for item in year:
        if item in UTIL_CN_NUM.keys():
            res = res + str(UTIL_CN_NUM[item])
        else:
            res = res + item
    m = re.match("\d+", res)
    if m:
        if len(m.group(0)) == 2:
            return int(datetime.today().year / 100) * 100 + int(m.group(0))
        else:
            return int(m.group(0))
    else:
        return None


def parse_datetime(msg):
    if msg is None or len(msg) == 0:
        return None
    try:
        # 使用时间自动识别库
        dt = parse(msg, fuzzy=True)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        # 使用正则表达式识别
        m = re.match(
            r"([0-9零一二三四五六七八九十]+年)?([0-9一二三四五六七八九十]+月)?"
            r"([0-9一二三四五六七八九十]+[号日])?([上中下五晚早]+)?"
            r"([0-9零一二三四五六七八九十百]+[点:\.时])?([0-9零一二三四五六七八九十百]+分?)?([0-9零一二三四五六七八九十百]+秒)?"
        ,msg)
        if m.group(0) is not None:
            res = {
                "year": m.group(1),
                "month": m.group(2),
                "day": m.group(3),
                "hour": m.group(5) if m.group(5) is not None else '00',
                'minute': m.group(6) if m.group(6) is not None else '00',
                'second': m.group(7) if m.group(7) is not None else '00',
            }
            params = {}
            # 遍历提取到的日期文字
            for name in res:
                if res[name] is not None and len(res[name]) != 0:
                    tmp = None
                    # 将日期文字转换成数字
                    if name == 'year':
                        tmp = year2dig(res[name][:-1])
                    else:
                        tmp = cn2dig(res[name][:-1])
                    if tmp is not None:
                        params[name] = int(tmp)
            # 提取数字日期
            target_date = datetime.today().replace(**params)
            is_pm = m.group(4)
            if is_pm is not None:
                if is_pm == u'下午' or is_pm == u'晚上' or is_pm == '中午':
                    hour = target_date.time().hour
                    print("hour:",hour)
                    if hour<12:
                        target_date=target_date.replace(hour=hour+12)
            return target_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return None


# 判断日期是否有效
def check_time_valid(word):
    m=re.match("%d+$",word)
    if m:
        if len(word)<=6:
            return None
    world=re.sub('[号|日]\d+$','日',word)
    if world!=word:
        return check_time_valid(world)
    else:
        return world


# 提取时间：解析句子，提取可能表示时间的词，并进行上下文拼接
def time_extract(txt):
    time_res=[]
    word=''
    keyDate={'今天':0,'明天':1,'后天':2,'今日':0,'明日':1}
    # print([ [k,v] for k,v in psg.cut(txt)])
    for k,v in psg.cut(txt):
        if k in keyDate:
            if word!="":
                time_res.append(word)
                word=(datetime.today()+timedelta(days=keyDate.get(k,0))).strftime("%Y年%m月%d日")
        elif word!='':
            if v in ['m','t']:
                word=word+k
            else:
                time_res.append(word)
                word=''
        elif v in ['m','t'] :
            word=k
    if word!='':
        time_res.append(word)

    result=list(filter(lambda x:x is not None,[ check_time_valid(w) for w in time_res]))
    final_res=[ parse_datetime(w) for w in result]
    return [ x for x in final_res if x is not None]


text1="中新网3月3日，据WTT世界乒联消息，WTT新加坡大满贯2023资格赛将于明日正式打响，3月7日至9日为资格赛，11日至19日为正赛。"
print(text1,time_extract(text1),sep=":")

