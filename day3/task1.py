import requests
from bs4 import BeautifulSoup


def three():
    # 定义爬取网址
    url = "https://movie.douban.com/chart"
    # 定义浏览器表头信息，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 向目标网站发送请求并获取网页源码
        rs = requests.get(url, headers=headers)
        rs.raise_for_status()  # 检查请求是否成功

        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(rs.text, 'html.parser')

        # 查找所有电影条目 - 通过观察网页结构确定的选择器
        movie_items = soup.select('tr.item')

        # 提取前10个电影的标题
        titles = []
        for i, item in enumerate(movie_items[:10]):
            # 提取电影标题（包含在<a>标签内）
            title_tag = item.select_one('.pl2 a')
            if title_tag:
                # 清理标题中的多余空格/换行
                title = title_tag.get_text().strip().replace('\n', '').replace(' ', '')
                titles.append(title)

        # 打印前10个电影标题
        print("豆瓣电影排行榜TOP10:")
        for idx, title in enumerate(titles, 1):
            print(f"{idx}. {title}")

        return titles

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return []
    except Exception as e:
        print(f"解析出错: {e}")
        return []


if __name__ == "__main__":
    three()