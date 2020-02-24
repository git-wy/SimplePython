# -*- coding: utf-8 -*-
# Author: W.Y.
# Date: 2020/2/24

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models
import base64
import os
import json
import pandas as pd


class TencentAudio2Text:
    def __init__(self):

        #####################################  以下为自定义设置区 ##########################################
        self.my_id = ''   # 自己的腾讯云secretId
        self.my_key = ''      # 自己的腾讯云secretKey

        #####################################  以上为自定义设置区 ##########################################

        cred = credential.Credential(self.my_id, self.my_key)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        clientProfile.signMethod = "TC3-HMAC-SHA256"

        self.client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile)

    def create_request(self, data, data_len):

        try:

            req = models.CreateRecTaskRequest()
            params = {"EngineModelType": "8k_zh", "ChannelNum": 1, "ResTextFormat": 0, "SourceType": 1,
                      "Data": data, "DataLen": data_len}
            req._deserialize(params)

            resp = self.client.CreateRecTask(req)

            result_task_id = resp.to_json_string()
            json_task_id = json.loads(result_task_id)
            task_id = json_task_id['Data']['TaskId']

            return task_id

        except TencentCloudSDKException as err:
            print(err)

    def get_result(self, task_id):

        try:

            req_result = models.DescribeTaskStatusRequest()
            params_result = {"TaskId": task_id}
            req_result._deserialize(params_result)

            resp_result = self.client.DescribeTaskStatus(req_result)

            result = resp_result.to_json_string()
            final_result = json.loads(result)
            text = final_result['Data']['Result']

            return text

        except TencentCloudSDKException as err:
            print(err)


if __name__ == '__main__':

    #####################################  以下为自定义设置区 ##########################################
    file_path = 'E:\\Data Mining\\NLP_VoiceMining\\Audio2Text_YYT\\Data'      # 存放语音数据的文件夹路径
    result_file = 'E:\\Data Mining\\NLP_VoiceMining\\Audio2Text_YYT\\Data\\result.xlsx'   # 保存最终结果的xlsx名称及路径

    #####################################  以上为自定义设置区 ##########################################

    data_list = os.listdir(file_path)
    processor = TencentAudio2Text()
    TaskIdList = []
    ResultList = []

    for i in range(0, len(data_list)):
        data_file = open(r'{}\{}'.format(file_path, data_list[i]), mode='rb')
        data_b = data_file.read()
        data_length = len(data_b)
        data_code = base64.b64encode(data_b).decode()

        TaskIdList.append(processor.create_request(data_code, data_length))

    for j in range(0, len(TaskIdList)):
        ResultList.append(processor.get_result(TaskIdList[j]))

    result_df = pd.DataFrame(ResultList, columns=['text'])
    data_df = pd.DataFrame(data_list, columns=['file'])
    final = pd.concat([data_df, result_df], axis=1)

    final.to_excel(result_file, index=False)

