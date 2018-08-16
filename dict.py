# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json


def findCi(fpath,ci):
    with open(fpath,'r',encoding='UTF-8') as fp:
        records=json.load(fp)
        print('从'+str(len(records))+'条目中找:'+ci)
    merged=dict()
    for item in records:
        merged.update({item.get('ci'):item.get('explanation')})
    print(merged.get(ci,'没找到!'))

def findWord(fpath,word):
    with open(fpath,'r',encoding='UTF-8') as fp:
        records=json.load(fp)
        print('从'+str(len(records))+'条目中找:'+word)
    merged=dict()
    for item in records:
        merged.update({item.get('word'):'曾写作: '+item.get('oldword')+' 笔画数： '+item.get('strokes')+' 拼音:'+item.get('pinyin')+' 部首: '+item.get('radicals')+'部\n解释： '+item.get('explanation')+'\n\n扩展阅读： '+item.get('more')})
    print(merged.get(word,'没找到!'))

def findIdiom(fpath,idiom):
    with open(fpath,'r',encoding='UTF-8') as fp:
        records=json.load(fp)
        print('从'+str(len(records))+'条目中找'+idiom)
    merged=dict()
    for item in records:
        merged.update({item.get('word'):'拼音: '+item.get('pinyin')+'\n解释： '+item.get('explanation')+'\n衍生阅读:'+item.get('derivation')+'\n例句: '+item.get('example')+'\n缩写： '+item.get('abbreviation')})
    print(merged.get(idiom,'没找到!'))

def findxiehouyu(fpath,word):
    with open(fpath,'r',encoding='UTF-8') as fp:
        records=json.load(fp)
        print('从'+str(len(records))+'条目中找:'+word)
    merged=dict()
    for item in records:
        merged.update({item.get('riddle'):item.get('answer')})
    print(merged.get(word,'没找到!'))

def initFileConfig(path):
    rootpath=path
    xiehouyupath=rootpath+r'\xiehouyu.json'
    cidianpath=rootpath+r'\ci.json'
    idiompath=rootpath+r'\idiom.json'
    wordpath=rootpath+r'\word.json'
    return xiehouyupath,cidianpath,idiompath,wordpath
   
            
    


if __name__=='__main__':
    path=r'C:\Users\Administrator\git\chinese-xinhua\data'  #替换成自己的目录
    print('数据文件目录:'+path)
    xhy,cidian,idiom,word=initFileConfig(path)
    inputword=input('输入随便什么东西 :')
    #懒得做分支了 以下四个函数自己切换注释
    #findxiehouyu(xhy,inputword) 
    #findIdiom(idiom,inputword)
    #findWord(word,inputword)
    findCi(cidian,inputword)
    
