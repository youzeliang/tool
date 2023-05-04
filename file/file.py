import webbrowser
import urllib.parse


def find_str():
    """
    打开文件。然后去除特定的关键词，在原有基础上保存为文件
    """
    # 打开目标markdown文件
    with open('/Users/youzeliang/go/src/github.com/youzeliang/news/new1.md', 'r+') as f:
        # 按行读取文件内容
        lines = f.readlines()

        # 初始化一个空list来存储新的文件内容
        new_lines = []

        # 遍历每一行
        for line in lines:
            # 如果行中包含特定的字符串，则打印该行并跳过不添加到新文件内容列表中
            if 'json' in line.lower():
                # 打开网站
                https_index = line.find("https")
                if https_index != -1:
                    new_line = line[https_index:].strip()
                    webbrowser.open(new_line)

                print(line)
                continue
                # return
            # 否则将该行添加到新文件内容列表中
            else:
                new_lines.append(line)
                continue

        # 在原有文件基础上修改，清空文件内容并将新内容写入文件中
        f.seek(0)
        f.truncate()
        f.writelines(new_lines)

        # 将新内容写入文件中
        # with open('/path/to/new/file.md', 'w') as f:
        #     f.writelines(new_lines)


if __name__ == '__main__':
    find_str()
