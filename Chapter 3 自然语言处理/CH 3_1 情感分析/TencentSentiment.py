# -*- coding: utf-8 -*-
# Author: W.Y.
# Date: 2020/2/29

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.nlp.v20190408 import nlp_client
import json
import pandas as pd
import sqlite3


def cal_sentiment(pre_data, t_id, t_key):

    cred = credential.Credential(t_id, t_key)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "nlp.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

    params = {'Flag': 4, 'Text': pre_data}
    res = client.call('SentimentAnalysis', params)

    response = json.loads(res)
    positive = response['Response']['Positive']
    negative = response['Response']['Negative']
    sentiment = response['Response']['Sentiment']

    return positive, negative, sentiment


if __name__ == '__main__':

    #####################################  以下为自定义设置区 ##############################

    secret_id = '自己的secretId'   # 腾讯云secretId
    secret_key = '自己的secretKey'      # 腾讯云secretKey

    data = pd.read_excel(r'E:\Data Mining\SimplePython\Chapter 3 自然语言处理\CH 3_1 情感分析\data.xlsx')  # 要分析的excel文件
    text_col = 'text'  # 文本列的列名

    conn = sqlite3.connect(r'E:\Data Mining\SimplePython\Chapter 3 自然语言处理\CH 3_1 情感分析\sentiment.sqlite')
    # 保存sqlite数据库的路径，路径改成自己的就好，名称sentiment.sqlite建议不要改，不然后面也要改
    result_file = r'E:\Data Mining\SimplePython\Chapter 3 自然语言处理\CH 3_1 情感分析\result.xlsx'  # 保存结果的路径和文件名

    #####################################  以上为自定义设置区 ##############################

    data['clean_data'] = data['%s' % text_col].str.replace(r'[^\u4e00-\u9fa5^a-z^A-Z]', ' ')  # 剔除特殊字符和标点
    data['clean_data'] = data['clean_data'].str.replace(' +', ' ')  # 替换多个空格

    data['content_len'] = data['clean_data'].str.len()

    short_data = data[data['content_len'] < 200]  # 只保留长度小于200的
    short_data = short_data.reset_index()  # 重建索引。不删除原索引，数据第二列index则为原始数据的索引

    #####################################  以下可能需要自定义设置 ##############################

    # 如果需要单独保存文本长度大于等于200的数据，就把下面两行代码前面的#号删掉，改一下路径，再运行即可。
    # long_data = data[data['content_len'] >= 200]
    # long_data.to_excel(r'E:\Data Mining\NLP_SentimentAnalysis\Tencent_Sentiment\long_data.xlsx', index_label='index')

    start = 0

    # 上面start这行代码正常情况下不需要修改的，直接运行即可。
    # 如果分析过程中出错，程序停止，则需要修改一下start
    # 比如到“开始分析第100条数据……”时报错，那么重新分析的时候，把start改成99就可以，注意要减1哦
    # 也可以不修改，为了防止出现这种情况而数据丢失，我用了sqlite数据库，
    # 如果不修改从头分析的话也可以，数据会重复，但是没关系，我最后导出到excel的时候设置了去重，所以不影响结果
    # 另外，如果中途报错，那么之前结果是不会保存到excel的，但是会存在sqlite里，所以没关系，跑完最后一条会导出所有数据的
    # 只有输出了最后一条“结果导出到excel成功”才是所有的都跑完了

    ####################################  以上可能需要自定义设置 ##############################

    for i in range(start, len(short_data['clean_data'])):

        print('开始分析第 %d 条数据' % (i+1))

        pos, neg, sent = cal_sentiment(short_data['clean_data'][i], secret_id, secret_key)

        result = pd.DataFrame({'positive': [pos],
                               'negative': [neg],
                               'sentiment': [sent]}, index=[i])

        final = pd.concat([short_data.iloc[[i]], result], axis=1)

        final.to_sql('sentiment', conn, if_exists='append', index=True, index_label='new_index')

    cursor = conn.cursor()
    cursor.execute("delete from sentiment where rowid not in(select max(rowid) from sentiment group by new_index)")

    conn.commit()
    print('结果保存成功！')

    excel_result = pd.read_sql_query("select * from sentiment", conn)
    excel_result.to_excel(result_file, index=False)

    conn.close()

    print('结果导出到excel成功！')







