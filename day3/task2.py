import requests
from lxml import etree
import os


def download_images():
    url = "http://pic.netbian.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # 创建图片保存目录
    save_dir = 'e:\\shixun\\day3\\images'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"创建目录: {save_dir}")

    # 获取网页内容
    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'  # 网站使用gbk编码
    html_content = response.text

    # 解析HTML
    html = etree.HTML(html_content)
    # 修正XPath：提取图片的真实URL（注意@src后面可能有空格）
    img_elements = html.xpath("//ul[@class='clearfix']/li/a/span/img/@src")
    print(f"发现 {len(img_elements)} 张图片")

    for idx, img_path in enumerate(img_elements):
        # 正确拼接图片URL（处理相对路径）
        img_url = requests.compat.urljoin(url, img_path)

        # 获取图片文件名和扩展名
        img_name = os.path.basename(img_url)
        _, ext = os.path.splitext(img_name)
        if not ext:  # 如果URL中没有扩展名，默认使用.jpg
            ext = '.jpg'

        # 下载图片
        img_data = requests.get(img_url, headers=headers).content
        save_path = os.path.join(save_dir, f"image_{idx}{ext}")

        # 保存图片
        with open(save_path, 'wb') as f:
            f.write(img_data)
            print(f"已保存: {save_path}")

    print("所有图片下载完成")


if __name__ == "__main__":
    download_images()