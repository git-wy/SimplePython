# -*- coding: utf-8 -*-
# Author: W.Y.
# Date: 2020/2/24

import requests
import time
import re
import pandas as pd
import sqlite3
from bs4 import BeautifulSoup


class GetWeibo:

    def __init__(self):

        self.url = 'https://m.weibo.cn/api/container/getIndex?containerid={}' \
                   '_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid={}' \
                   '&page_type=03&page={}'
        self.detail_url = 'https://m.weibo.cn/detail/{}'

    def get_page(self, header, cid, did, page):
        try:
            home_url = self.url.format(cid, did, page)
            response = requests.get(home_url, header)

            if response.status_code == 200:
                json_data = response.json()
                return json_data

        except requests.ConnectionError as e:
            print('error', e.args)

    def get_detail(self, header, json_data):

        if json_data:
            all_data = json_data.get('data').get('cards')

            result_list = []

            for data in all_data:
                result = {}
                if data.get('card_type') == 9:
                    details = data.get('mblog')
                    result['weibo_id'] = details.get('id')  # 微博ID

                    ################### 获取全文和准确时间 ###################
                    long_url = self.detail_url.format(result['weibo_id'])
                    response = requests.get(long_url, header)
                    soup = BeautifulSoup(response.text, 'html.parser')

                    time_pattern = re.compile(r'\"created_at\": \"(.*?)\",', re.S)
                    real_time = time_pattern.findall(str(soup))
                    if real_time:
                        clean_time = real_time[0][11:19]
                    else:
                        clean_time = '爬取缺失'
                    text_pattern = re.compile(r'\"text\": \"(.*?)\",', re.S)
                    full_content = text_pattern.findall((str(soup)))
                    if full_content:
                        full_text = full_content[0]
                    else:
                        full_text = '爬取缺失'
                    ############################################################

                    title = details.get('title')
                    if title:
                        result['title'] = title.get('text')  # 是否置顶
                    else:
                        result['title'] = ''  # 为空则不是置顶微博
                    result['date'] = details.get('created_at')  # 发布日期
                    result['time'] = clean_time  # 发布时间点
                    result['source'] = details.get('source')  # 手机客户端
                    result['content'] = re.sub('<.*?>', '', full_text)  # 发布内容
                    result['pic_num'] = details.get('pic_num')  # 图片数量
                    result['repost'] = details.get('reposts_count')  # 转发数
                    result['comment'] = details.get('comments_count')  # 评论数
                    result['like'] = details.get('attitudes_count')  # 点赞数
                    result['user'] = details.get('user').get('screen_name')  # 用户名称

                    result['current_time'] = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))  # 爬取时间

                    result_list.append(result)

            return result_list


if __name__ == '__main__':

    #################################### 以下为自定义设置区 ###############################################

    headers = {
        'cookie': 'SCF=AiBXx3WGn8XIfy52GrgK7EBvBxZ5Ix00ETzKCsezG3_NFuQVRKj8hNxCp7jneelrEobvdThpKItTsty1J6FwvjA.; SUB=_2A25zIUKuDeRhGeFM7FYW8y7MyT6IHXVQ6m7mrDV6PUJbktANLVH5kW1NQKJ2r15G6X8evwlpvIcO-HaUkFnmwcjG; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5nXSwyD.p2ZcK2acsL6AzJ5JpX5K-hUgL.FoMES0BNe057eoz2dJLoI7_0qg_fMJ2Neh24Sntt; SUHB=0jBYCzL56B0iAp; _T_WM=42334287993; XSRF-TOKEN=d1555a; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D2302836380785598%26fid%3D2304136380785598_-_WEIBO_SECOND_PROFILE_WEIBO%26uicode%3D10000011',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    # 上面headers的获取方式请参考github上面的说明

    destination_list = pd.read_excel(r'E:\Data Mining\Spider\Spider_Weibo\HomePage\destination.xlsx',
                                     dtype={'containerid': str, 'lfid': str},
                                     encoding='gbk')
    # 保存景区首页网址的excel文件，具体的格式请参考github上的说明

    conn = sqlite3.connect(r'E:\Data Mining\Spider\Spider_Weibo\HomePage\weibo.sqlite')
    # 保存sqlite数据库的路径，路径改成自己的就好，名称weibo.sqlite建议不要改，不然后面也要改

    result_file = r'E:\Data Mining\Spider\Spider_Weibo\HomePage\weibo.xlsx'  # 保存最终结果的excel文件路径及文件名

    start = 0

    # 上面start这行代码正常情况下不需要修改的，直接运行即可。
    # 如果分析过程中出错，程序停止，则需要修改一下start
    # 比如到“开始爬取第100个景区的微博”时报错，那么重新分析的时候，把start改成99就可以，注意要减1哦
    # 注意，哪怕是第100个景区的微博爬到一半，也要从第100条重新爬哈，start还是改成99，要不然修改挺麻烦的，容易出错
    # 也可以不修改，为了防止出现这种情况而数据丢失，我用了sqlite数据库，
    # 如果不修改从头分析的话也可以，数据会重复，但是没关系，我最后导出到excel的时候设置了去重，所以不影响结果
    # 另外，如果中途报错，那么之前结果是不会保存到excel的，但是会存在sqlite里，所以没关系，跑完最后一条会导出所有数据的
    # 只有输出了最后一条“结果导出到excel成功”才是所有的都跑完了

    #################################### 以上为自定义设置区 ###############################################

    weibo = GetWeibo()

    for i in range(start, len(destination_list)):

        print('#################### 开始爬取第 %s 个景区的微博 ###############' % (i + 1))

        for p in range(1, 9999):

            print('正在爬取第 %s 页' % p)

            json = weibo.get_page(headers, destination_list['containerid'][i], destination_list['lfid'][i], p)
            time.sleep(1)

            if '暂无微博' not in str(json):
                final_result = weibo.get_detail(headers, json)
                pd.DataFrame(final_result).to_sql('weibo', conn, if_exists='append', index=False)

            else:
                print('#####################已经爬完该景区最后一页#####################')
                break

    cursor = conn.cursor()
    cursor.execute("delete from weibo where rowid not in(select max(rowid) from weibo group by weibo_id)")

    conn.commit()
    print('结果保存成功！')

    excel_result = pd.read_sql_query("select * from weibo", conn)
    excel_result.to_excel(result_file, index=False)

    conn.close()

    print('结果导出到excel成功！')
