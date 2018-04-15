# 51ape 歌手歌曲下载地址获取（百度云链接&密码）

使用 BeautifulSoup4 和 requests 进行网页内容抓取分析。

提取出歌手所有歌曲的百度云链接&密码

### 使用说明：

1. 先看 main 函数， 首先提供 51ape 对应歌手的前缀，从歌手列表点进去后，选择任意歌曲即可看到此地址

2. 设定总页数

3. 设定保存下载地址的文件名，会保存为 txt 文档


```python
if __name__ == "__main__":
    base_url = 'http://www.51ape.com/jay'
    page_count = 8
    file_name = 'jay'

    select_item_list(base_url, page_count, file_name)

```