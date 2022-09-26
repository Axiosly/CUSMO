from aip import AipOcr
from translate import Translator
import speech
# 定义常量
APP_ID = '27454690'
API_KEY = 'o0P6EKClZ6ia5Fk2T6anwo9l'
SECRET_KEY = 'Fx4Vx2jgQVq6RlKLHEzDktsQ0FMUb3Mz'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "test.jpg"

translator =Translator (to_lang='Chinese')  # 设置目标语言
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}
audio = ""
# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(filePath), options)
print(result)
words_result = result['words_result']
for i in range(len(words_result)):
    print(words_result[i]['words'])

    text = words_result[i]['words']
    translation = translator.translate(text)
    audio = audio + translation
    print(translation)
# 语音输出
speech.say(audio)
