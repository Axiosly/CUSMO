from aip import AipImageClassify
import os
import speech

""" 填入参数 """

APP_ID = '27455236'
API_KEY = 'x6izsDsIe9fBwgXQDKgB4zRp'
SECRET_KEY = 'Qo0vR891g9A5X36xpEhY8IoQcMtPW7ld'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def dish_Detect():


        image = get_file_content("D:\\2.jpg")

        """ 调用菜品识别 """

        client.dishDetect(image)

        """ 如果有可选参数 """
        options = {}
        options["top_num"] = 10
        options["filter_threshold"] = "0.7"
        options["baike_num"] = 1
        """ 带参数调用菜品识别 """
        results = client.dishDetect(image, options)
        result = results['result'][0]

        print(

              result['name'],

              '	卡路里：', result['calorie'])
        s = result['name']+'	卡路里：'+result['calorie']

        # 语音输出
        speech.say(s)


if __name__ == '__main__':
    dish_Detect()