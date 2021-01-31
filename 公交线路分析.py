# coding=utf-
import re
def read_file():
    f = open('houshayu_subway_bus.txt')
    readline = f.readlines()
    word = []  # 存储单词

    # 得到文章的单词并且存入列表中：

    for line in readline:
        # 因为原文中每个单词都是用空格 或者逗号加空格分开的，
        if line == '\n':
            continue
        # line.replace('\n','')
        line = re.sub('\n', '', line)
        # wo = line.split(' ')

        word.append(line)


    return word


def clear_account(lists):
    # 去除重复的值
    wokey = {}
    wokey = wokey.fromkeys(lists)

    word_1 = list(wokey.keys())
    # 然后统计单词出现的次数,并将它存入一个字典中
    for i in word_1:
        wokey[i] = lists.count(i)
    # del wokey['']
    return wokey


def sort_1(wokey):
    # 排序,按values进行排序，如果是按key进行排序用sorted(wokey.items(),key=lambda d:d[0],reverse=True)
    wokey_1 = {}
    wokey_1 = sorted(wokey.items(), key=lambda d: d[1], reverse=True)

    # wokey_1=dict(wokey_1) 转成字典又会打乱顺序
    return wokey_1

def find_luxian(dict,zhanming):
    word1 = read_file()
    z = list()
    t = list()
    xianlu = list()
    for x, y in dict.items():
        z.append(x)
        t.append(int(y))

    for i in range(len(z)):
        if i != len(z)-1:
            if re.findall(zhanming, str(word1[t[i]:t[i+1]])) != list():
                xianlu.append(z[i])
        else:
            if re.findall(zhanming, str(word1[t[i]:len(word1)-1])) != list():
                xianlu.append(z[i])
    return str(xianlu)

# print(sort_1(clear_account(read_file())))
def main(wokey_1):
    # 输出前10个
    word = read_file()
    luxian = dict()
    with open('result.txt', 'w') as f:
        for x, y in wokey_1:
            for z in word:
                if re.findall('\d路', z) != list():
                    luxian[z] = word.index(z)

            text = '公交站名： %s,经过线路数： %d' % (x, y)
            xianlus = find_luxian(luxian, str(x))
            print(xianlus)
            f.write(text+xianlus+'\n')


main(sort_1(clear_account(read_file())))
