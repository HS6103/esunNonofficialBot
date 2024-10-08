#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for cardless

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join("reply", "reply_cardless.json")), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[cardless] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    for i in range(len(args)):
        args[i] = args[i].lower().strip(' ')   # 前處理，把argument變小寫並去頭尾空格
    
    if utterance == "[APP]預約[行動]無卡提款需於多[久][時間][內]至[ATM]進行交易":
        if CHATBOT_MODE:
            if args[3] == '時間' and args[5] in userDefinedDICT['atm']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "無卡交易[密碼][該]如何[重新]設定呢":
        if CHATBOT_MODE:
            if args[0] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[一天][可以]預[約]幾[筆][行動]無卡提款[序號]":
        if CHATBOT_MODE:
            if args[0] == '一天' and args[5] == '序號':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]至[他][行][ATM]進行跨行無卡提款嗎":
        if CHATBOT_MODE:
            if args[1] == '他' and args[2] == '行' and args[3] in userDefinedDICT['atm']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[外國人][能]否使用[行動]無卡提款":
        if CHATBOT_MODE:
            if args[0] == '外國人':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "無卡交易[密碼]錯誤[上]限是幾[次]":
        if CHATBOT_MODE:
            if args[0] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "無卡交易[密碼]錯誤達到[上]限[後][應該]怎麼辦":
        if CHATBOT_MODE:
            if args[0] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "無卡提款[序號]如何取消":
        if CHATBOT_MODE:
            if args[0] == '序號':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "無卡提款[序號]如何查詢":
        if CHATBOT_MODE:
            if args[0] == '序號':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "無卡提款[序號]逾時怎麼辦":
        if CHATBOT_MODE:
            if args[0] == '序號':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[行動]無卡提款的[限額]":
        if CHATBOT_MODE:
            if args[1] == '限額':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "身份證字號重號[能]否使用[行動]無卡提款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "金融卡[不見]了還[可以]使用[行動]無卡提款嗎":
        if CHATBOT_MODE:
            if args[0] == '不見':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申請[行動]無卡提款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何註銷[行動]無卡提款":
        if CHATBOT_MODE:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何開通無卡提款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass


    if utterance == "忘記無卡交易[密碼]":
        if CHATBOT_MODE:
            if args[0] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "掛失金融卡需要再[重新]開通[行動]無卡提款服務嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "更換金融卡需要再[重新]開通[行動]無卡提款服務嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "補發金融卡需要再[重新]開通[行動]無卡提款服務嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "變更無卡交易[密碼]":
        if CHATBOT_MODE:
            if args[0] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨行無卡提款[手續費]":
        if CHATBOT_MODE:
            if args[0] in ['手續費', '費用']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "重設無卡交易[密碼]":
        if CHATBOT_MODE:
            if args[0] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "開通[行動]無卡提款[成功]但是[我]的金融卡[不見]了":
        if CHATBOT_MODE:
            if args[1] == '成功' and args[3] == '不見':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[ATM][可以]進行跨行無卡提款嗎":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['atm']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "開通時使用的金融卡[會]影響[行動]無卡提款時[能]選擇的提領[帳戶]嗎":
        if CHATBOT_MODE:
            if args[3] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT