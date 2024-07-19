import os
import json
from datetime import datetime
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(["标题",  "链接"])
urls = []

def read_and_print_files(folder_path):
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print(f"错误: 文件夹 '{folder_path}' 不存在")
        return

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 确保它是一个文件而不是子文件夹
        if os.path.isfile(file_path):
            try:
                # 尝试以UTF-8编码读取文件
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    extract_wechat_url(content)
            except UnicodeDecodeError:
                print(f"警告: 无法以UTF-8编码读取文件 '{filename}'。可能不是文本文件或使用了不同的编码。")
            except Exception as e:
                print(f"读取文件 '{filename}' 时发生错误: {str(e)}")


def extract_wechat_url(content):
    json_data = json.loads(content)
    general_msg_list_str = json_data['general_msg_list']
    general_msg_list = json.loads(general_msg_list_str)
    msg_list = general_msg_list['list']
    for msg in msg_list:
        app_msg_ext_info = msg['app_msg_ext_info']
        content_url = app_msg_ext_info['content_url']
        title = app_msg_ext_info['title']
        # 将&amp;替换为&
        content_url = content_url.replace('&amp;', '&')
        ws.append([title, content_url])
        urls.append(content_url)


# 使用函数
folder_path = r"C:\Users\79969\Desktop\Dump-0719-20-51-49\mp.weixin.qq.com\mp"
read_and_print_files(folder_path)
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
filename = f'微信公众号_{timestamp}.xlsx'
wb.save(filename)
print(f"数据已保存到 {filename}")

txt_filename = f'微信公众号URL_{timestamp}.txt'
with open(txt_filename, 'w', encoding='utf-8') as f:
    for url in urls:
        f.write(f"{url}\n")
print(f"URL已保存到 {txt_filename}")