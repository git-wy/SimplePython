# -*- coding: utf-8 -*-
# Author: W.Y.
# Date: 2020/2/25

import requests
import time
import pandas as pd
import sqlite3
from bs4 import BeautifulSoup


def get_url(header, weibo_id, max_id, max_id_type):

    url = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id={}&max_id_type={}'

    comment_url = url.format(weibo_id, weibo_id, max_id, max_id_type)

    try:
        r = requests.get(comment_url, headers=header)
        if r.status_code == 200:
            return r.json()
    except requests.ConnectionError as e:
        print('error', e.args)


def get_max(json_data):

    max_list = {}

    if json_data.get('ok') == 1:
        items = json_data.get('data')

        max_list['max_id'] = items['max_id']
        max_list['max_id_type'] = items['max_id_type']
    else:
        max_list['max_id'] = 'Zero'
        max_list['max_id_type'] = 'Zero'

    return max_list


def phrase_data(json_data, weibo_id):
    if json_data.get('ok') == 1:
        result_list = []
        datas = json_data.get('data').get('data')

        for data in datas:
            result = {}

            result['weibo_id'] = weibo_id
            result['comment_id'] = data.get('id')

            date_time = data.get('created_at')
            time_struct = time.strptime(date_time, '%a %b %d %H:%M:%S +0800 %Y')
            result['date_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time_struct)

            if data.get('comments'):
                result['reply'] = len(data.get('comments'))
            else:
                result['reply'] = 0
            result['like'] = data.get('like_count')

            result['user'] = data.get('user').get('screen_name')
            result['user_id'] = data.get('user').get('id')
            result['user_gender'] = data.get('user').get('gender')
            result['user_follower'] = data.get('user').get('followers_count')
            result['user_follow'] = data.get('user').get('follow_count')

            content = data.get('text')
            result['content'] = BeautifulSoup(content, 'html.parser').get_text()

            result['current_time'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 爬取时间

            if result not in result_list:
                result_list.append(result)
            else:
                pass

        return result_list


if __name__ == '__main__':

    ####################################  以下为自定义设置区  #####################################

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'cookie': 'SCF=AiBXx3WGn8XIfy52GrgK7EBvBxZ5Ix00ETzKCsezG3_NFuQVRKj8hNxCp7jneelrEobvdThpKItTsty1J6FwvjA.; SUB=_2A25zIUKuDeRhGeFM7FYW8y7MyT6IHXVQ6m7mrDV6PUJbktANLVH5kW1NQKJ2r15G6X8evwlpvIcO-HaUkFnmwcjG; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5nXSwyD.p2ZcK2acsL6AzJ5JpX5K-hUgL.FoMES0BNe057eoz2dJLoI7_0qg_fMJ2Neh24Sntt; SUHB=0jBYCzL56B0iAp; _T_WM=42334287993; WEIBOCN_FROM=1110006030; MLOGIN=1; XSRF-TOKEN=c3b986'
    }
    # 上面headers的获取方式请参考github上面的说明

    conn = sqlite3.connect(r'E:\Data Mining\Spider\Spider_Weibo\HomePage\weibo.sqlite')
    # 保存sqlite数据库的路径，路径改成自己的就好，注意这里的weibo.sqlite和GetWeibo里面是一样的，是同一个数据库
    # 如果GetWeibo里改了，这里也要改

    result_file = r'E:\Data Mining\Spider\Spider_Weibo\HomePage\comments.xlsx'
    # 保存最终结果的excel文件路径及文件名，注意这里的名称不能和GetWeibo里面的一样

    start = 0

    # 上面start这行代码正常情况下不需要修改的，直接运行即可。
    # 如果分析过程中出错，程序停止，则需要修改一下start
    # 比如到“开始爬取第100条微博的评论”时报错，那么重新分析的时候，把start改成99就可以，注意要减1哦
    # 注意，哪怕是第100条微博的评论爬到一半，也要从第100条重新爬哈，start还是改成99，要不然修改挺麻烦的，容易出错
    # 也可以不修改，为了防止出现这种情况而数据丢失，我用了sqlite数据库，
    # 如果不修改从头分析的话也可以，数据会重复，但是没关系，我最后导出到excel的时候设置了去重，所以不影响结果
    # 另外，如果中途报错，那么之前结果是不会保存到excel的，但是会存在sqlite里，所以没关系，跑完最后一条会导出所有数据的
    # 只有输出了最后一条“结果导出到excel成功”才是所有的都跑完了

    ####################################  以上为自定义设置区  #####################################

    w_id_df = pd.read_sql_query("select weibo_id from weibo", conn)
    w_id = w_id_df['weibo_id']

    m_id = 0
    m_id_type = 0
    total_comment = []

    for i in range(start, len(w_id)):
        print('################### 开始爬取第 %d 条微博的评论 ##################' % (i + 1))
        for j in range(9999):

            json = get_url(headers, w_id[i], m_id, m_id_type)
            max_id_list = get_max(json)

            time.sleep(1)

            if max_id_list['max_id'] != 'Zero':
                print('开始爬取第 %d 页评论……' % (j + 1))
                m_id = max_id_list['max_id']
                m_id_type = max_id_list['max_id_type']
            else:
                print('#################### 该条微博无评论 #################')
                m_id = 0
                m_id_type = 0
                break

            comment = list(phrase_data(json, w_id[i]))

            if comment not in total_comment:
                total_comment.append(comment)
                pd.DataFrame(comment).to_sql('comments', conn, if_exists='append', index=False)
            else:
                print('################### 完成爬取第 %d 条微博的评论 ##################' % (i + 1))
                m_id = 0
                m_id_type = 0
                break

    cursor = conn.cursor()
    cursor.execute("delete from comments where rowid not in(select max(rowid) from comments group by comment_id)")

    conn.commit()
    print('结果保存成功！')

    excel_result = pd.read_sql_query("select * from comments", conn)
    excel_result.to_excel(result_file, index=False)

    conn.close()

    print('结果导出到excel成功！')

