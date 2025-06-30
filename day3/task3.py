import os
import time
import random
import pickle
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import json
import sys
import subprocess

from fake_useragent import UserAgent

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(os.path.dirname(__file__), "cnki_crawler_edge.log")),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('CNKI_Edge_Crawler')

# 要搜索的论文列表
PAPER_LIST = [
    "基于视觉信息的煤矸识别分割定位方法",
    "基于YOLO11的无人机航拍图像小目标检测算法",
    "AA-GM-YOLO：基于改进YOLO的机加工切屑监测方法",
    "轻量化输电线路缺陷检测方法",
    "基于关键点检测的服装尺寸测量方法",
    "基于YOLO的小目标检测算法研究"
]


class CNKIEdgeCrawler:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.cookie_file = os.path.join(os.path.dirname(__file__), "cnki_edge_cookies.pkl")
        self.results = []
        self.ua = UserAgent()

    def init_browser(self):
        """初始化Edge浏览器设置"""
        try:
            # 创建Edge服务对象
            service = Service()

            # 配置Edge选项
            options = webdriver.EdgeOptions()
            options.use_chromium = True
            options.add_argument('--start-maximized')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

            # 设置随机User-Agent
            user_agent = self.ua.random
            options.add_argument(f"user-agent={user_agent}")

            # 创建Edge浏览器实例
            self.driver = webdriver.Edge(service=service, options=options)
            self.wait = WebDriverWait(self.driver, 20)  # 等待时间20秒

            # 隐藏Selenium自动化特征
            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    })
                """
            })

            logger.info("Edge浏览器初始化成功")
            return True
        except Exception as e:
            logger.error(f"浏览器初始化失败: {str(e)}")
            return False

    def load_cookies(self):
        """加载Cookies（如果存在）"""
        if os.path.exists(self.cookie_file):
            try:
                self.driver.get("https://www.cnki.net/")
                time.sleep(2)

                for cookie in pickle.load(open(self.cookie_file, "rb")):
                    # 确保cookie域正确
                    if 'cnki.net' in cookie.get('domain', ''):
                        try:
                            self.driver.add_cookie(cookie)
                        except Exception as e:
                            logger.warning(f"添加cookie失败: {str(e)}")

                self.driver.refresh()
                time.sleep(random.uniform(1, 3))
                logger.info("已加载Cookies")
                return True
            except Exception as e:
                logger.error(f"加载Cookies失败: {str(e)}")
                return False
        return False

    def save_cookies(self):
        """保存Cookies"""
        try:
            with open(self.cookie_file, "wb") as f:
                pickle.dump(self.driver.get_cookies(), f)
            logger.info("已保存Cookies")
            return True
        except Exception as e:
            logger.error(f"保存Cookies失败: {str(e)}")
            return False

    def check_captcha(self):
        """检查并处理人机验证"""
        try:
            # 检查是否有验证码提示
            if "验证码" in self.driver.page_source:
                logger.warning("检测到知网人机验证，请手动处理...")
                print("⚠️ 检测到知网人机验证，请手动处理后按Enter继续...")
                input()
                self.save_cookies()  # 保存通过验证后的Cookies
                return True

            # 检查是否跳转到登录页面
            if "login" in self.driver.current_url:
                logger.warning("检测到需要登录知网账户，请手动登录...")
                print("⚠️ 请手动登录知网账户，登录完成后按Enter继续...")
                input()
                self.save_cookies()
                return True

            return False
        except Exception as e:
            logger.error(f"检查验证码时出错: {str(e)}")
            return False

    def simulate_human_behavior(self):
        """模拟人类行为"""
        try:
            # 随机滚动页面
            scroll_height = random.randint(300, 800)
            self.driver.execute_script(f"window.scrollTo(0, {scroll_height});")
            time.sleep(random.uniform(0.5, 1.5))

            # 随机移动鼠标
            actions = webdriver.ActionChains(self.driver)
            actions.move_by_offset(random.randint(10, 100), random.randint(10, 100)).perform()
            time.sleep(random.uniform(0.3, 0.8))

            return True
        except Exception as e:
            logger.warning(f"模拟人类行为失败: {str(e)}")
            return False

    def search_paper(self, title):
        """搜索论文"""
        try:
            # 确保在知网首页
            if "cnki.net" not in self.driver.current_url:
                self.driver.get("https://www.cnki.net/")
                time.sleep(2)

            # 等待搜索框加载
            search_box = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='txt_SearchText']"))
            )
            time.sleep(random.uniform(0.5, 1.5))

            # 清除搜索框并输入标题
            search_box.clear()
            for char in title:
                search_box.send_keys(char)
                time.sleep(random.uniform(0.05, 0.15))  # 模拟人类输入速度

            # 模拟人类行为
            self.simulate_human_behavior()

            # 点击搜索按钮
            search_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='检索']"))
            )
            search_btn.click()
            logger.info(f"已提交搜索: {title}")

            # 等待搜索结果加载
            time.sleep(random.uniform(2, 4))
            return True
        except Exception as e:
            logger.error(f"搜索论文失败: {title}, 错误: {str(e)}")
            return False

    def get_first_result(self):
        """获取第一条搜索结果"""
        try:
            # 等待结果加载
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//table[@class='result-table-list']/tbody/tr"))
            )

            # 获取第一条结果
            first_result = self.driver.find_element(
                By.XPATH, "//table[@class='result-table-list']/tbody/tr[1]"
            )

            # 提取标题
            title_element = first_result.find_element(By.CLASS_NAME, "name")
            title = title_element.text

            # 提取作者
            try:
                author_element = first_result.find_element(By.CLASS_NAME, "author")
                authors = author_element.text.split(';')
            except:
                authors = []

            # 提取来源
            try:
                source_element = first_result.find_element(By.CLASS_NAME, "source")
                source = source_element.text
            except:
                source = ""

            # 提取日期
            try:
                date_element = first_result.find_element(By.CLASS_NAME, "date")
                date = date_element.text
            except:
                date = ""

            # 获取详情链接
            link = title_element.find_element(By.TAG_NAME, "a").get_attribute("href")

            return {
                "title": title,
                "authors": authors,
                "source": source,
                "date": date,
                "link": link
            }
        except Exception as e:
            logger.error(f"获取搜索结果失败: {str(e)}")
            return None

    def get_paper_details(self, link):
        """获取论文详情"""
        try:
            # 打开详情页
            self.driver.get(link)
            time.sleep(random.uniform(3, 5))

            # 检查验证码
            if self.check_captcha():
                # 如果遇到验证码，重新打开详情页
                self.driver.get(link)
                time.sleep(random.uniform(3, 5))

            # 获取摘要
            try:
                abstract_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'abstract')]"))
                )
                abstract = abstract_element.text.replace("摘要：", "").strip()
            except:
                abstract = ""

            # 获取关键词
            try:
                keywords_element = self.driver.find_element(
                    By.XPATH, "//label[contains(text(), '关键词')]/following-sibling::div"
                )
                keywords = [kw.strip() for kw in keywords_element.text.split(';') if kw.strip()]
            except:
                keywords = []

            # 获取DOI
            try:
                doi_element = self.driver.find_element(
                    By.XPATH, "//label[contains(text(), 'DOI')]/following-sibling::div"
                )
                doi = doi_element.text.strip()
            except:
                doi = ""

            # 获取引用格式
            citation_text = ""
            try:
                # 点击引用按钮
                quote_btn = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'quote')]"))
                )
                quote_btn.click()
                time.sleep(random.uniform(1, 2))

                # 切换到引用格式框
                self.wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "modal-content"))
                )

                # 选择GB/T 7714格式
                format_select = self.wait.until(
                    EC.element_to_be_clickable((By.ID, "export_type"))
                )
                format_select.click()
                time.sleep(0.5)

                # 选择GB/T 7714选项
                gb_option = self.driver.find_element(
                    By.XPATH, "//option[contains(text(), 'GB/T 7714')]"
                )
                gb_option.click()
                time.sleep(1)

                # 获取引用文本
                citation_text = self.driver.find_element(
                    By.ID, "export_content"
                ).text
            except Exception as e:
                logger.warning(f"获取引用格式失败: {str(e)}")

            return {
                "abstract": abstract,
                "keywords": keywords,
                "doi": doi,
                "citation": citation_text
            }
        except Exception as e:
            logger.error(f"获取论文详情失败: {str(e)}")
            return {}

    def crawl_papers(self):
        """爬取所有论文"""
        if not self.init_browser():
            logger.error("无法初始化浏览器，程序终止")
            return

        try:
            # 打开知网
            self.driver.get("https://www.cnki.net/")
            logger.info("已打开知网")
            time.sleep(random.uniform(2, 4))

            # 加载Cookies
            self.load_cookies()

            # 检查是否需要登录或验证
            self.check_captcha()

            for paper_title in PAPER_LIST:
                logger.info(f"开始处理论文: {paper_title}")

                # 搜索论文
                if not self.search_paper(paper_title):
                    logger.warning(f"跳过论文: {paper_title}")
                    self.results.append({
                        "title": paper_title,
                        "error": "搜索失败"
                    })
                    continue

                # 检查验证码
                if self.check_captcha():
                    # 如果遇到验证码，重新搜索
                    self.search_paper(paper_title)

                # 获取第一条结果
                result = self.get_first_result()
                if not result:
                    logger.warning(f"未找到论文: {paper_title}")
                    self.results.append({
                        "title": paper_title,
                        "error": "未找到结果"
                    })
                    continue

                # 获取论文详情
                details = self.get_paper_details(result["link"])

                # 合并结果
                paper_data = {
                    "search_title": paper_title,
                    "found_title": result["title"],
                    "authors": result["authors"],
                    "source": result["source"],
                    "date": result["date"],
                    "link": result["link"],
                    **details
                }

                self.results.append(paper_data)
                logger.info(f"成功获取论文: {result['title']}")

                # 随机等待，避免请求过快
                time.sleep(random.uniform(3, 8))

            logger.info("所有论文处理完成")
        except Exception as e:
            logger.error(f"爬取过程中出错: {str(e)}")
        finally:
            # 保存结果
            self.save_results()
            # 关闭浏览器
            if self.driver:
                self.driver.quit()
                logger.info("浏览器已关闭")

    def save_results(self):
        """保存结果到文件"""
        if not self.results:
            logger.warning("没有结果可保存")
            return

        try:
            # 创建结果目录 - 使用原始字符串解决路径问题
            output_dir = r"E:\shixun\day3\wenxian"
            os.makedirs(output_dir, exist_ok=True)

            # 保存为文本文件
            txt_path = os.path.join(output_dir, "cnki_papers.txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("知网论文爬取结果 (Edge浏览器)\n\n")
                for i, paper in enumerate(self.results, 1):
                    f.write(f"论文 {i}:\n")
                    f.write(f"  搜索标题: {paper.get('search_title', '')}\n")
                    f.write(f"  匹配标题: {paper.get('found_title', '')}\n")

                    if 'authors' in paper:
                        f.write(f"  作者: {', '.join(paper['authors'])}\n")

                    f.write(f"  来源: {paper.get('source', '')}\n")
                    f.write(f"  日期: {paper.get('date', '')}\n")
                    f.write(f"  链接: {paper.get('link', '')}\n")
                    f.write(f"  DOI: {paper.get('doi', '')}\n")

                    if 'abstract' in paper:
                        f.write(f"  摘要: {paper['abstract']}\n")

                    if 'keywords' in paper:
                        f.write(f"  关键词: {', '.join(paper['keywords'])}\n")

                    if 'citation' in paper and paper['citation']:
                        f.write(f"  引用格式:\n{paper['citation']}\n")

                    f.write("\n" + "-" * 80 + "\n")

            # 保存为Markdown文件
            md_path = os.path.join(output_dir, "cnki_papers.md")
            with open(md_path, "w", encoding="utf-8") as f:
                f.write("# 知网论文爬取结果 (Edge浏览器)\n\n")
                for i, paper in enumerate(self.results, 1):
                    f.write(f"## {i}. {paper.get('found_title', paper.get('search_title', ''))}\n\n")
                    f.write(f"- **搜索标题**: {paper.get('search_title', '')}\n")
                    f.write(f"- **匹配标题**: {paper.get('found_title', '')}\n")

                    if 'authors' in paper:
                        f.write(f"- **作者**: {', '.join(paper['authors'])}\n")

                    f.write(f"- **来源**: {paper.get('source', '')}\n")
                    f.write(f"- **日期**: {paper.get('date', '')}\n")
                    f.write(f"- **链接**: [{paper.get('link', '')}]({paper.get('link', '')})\n")
                    f.write(f"- **DOI**: {paper.get('doi', '')}\n")

                    if 'abstract' in paper:
                        f.write(f"- **摘要**: {paper['abstract']}\n")

                    if 'keywords' in paper:
                        f.write(f"- **关键词**: {', '.join(paper['keywords'])}\n")

                    if 'citation' in paper and paper['citation']:
                        f.write("\n**引用格式**:\n```\n")
                        f.write(paper['citation'])
                        f.write("\n```\n")

                    f.write("\n")

            # 保存为JSON文件
            json_path = os.path.join(output_dir, "cnki_papers.json")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(self.results, f, ensure_ascii=False, indent=2)

            logger.info(f"结果已保存到 {output_dir}")
            return True
        except Exception as e:
            logger.error(f"保存结果失败: {str(e)}")
            return False


if __name__ == "__main__":
    print("=" * 80)
    print("知网论文爬取工具 (Edge浏览器版)".center(80))
    print("=" * 80)
    print("注意事项:")
    print("1. 请确保已安装Microsoft Edge浏览器")
    print("2. 程序会自动下载Edge WebDriver")
    print("3. 首次运行可能需要手动处理验证码或登录")
    print("4. 结果将保存在E:/shixun/day3/wenxian目录中")
    print("=" * 80)

    crawler = CNKIEdgeCrawler()
    crawler.crawl_papers()

    # 打印结果摘要
    print("\n" + "=" * 80)
    print(f"{'爬取结果摘要':^80}")
    print("=" * 80)
    for i, paper in enumerate(crawler.results, 1):
        print(f"\n论文 {i}: {paper.get('found_title', paper.get('search_title', '未知标题'))}")
        if 'error' in paper:
            print(f"  状态: 失败 - {paper['error']}")
        else:
            print(f"  作者: {', '.join(paper.get('authors', ['未知']))}")
            print(f"  来源: {paper.get('source', '未知')}")
            print(f"  日期: {paper.get('date', '未知')}")
            print(f"  成功获取: {'是' if paper.get('citation') else '否'}")
    print("\n" + "=" * 80)
    print(
        f"共处理 {len(crawler.results)} 篇论文, 成功获取 {sum(1 for p in crawler.results if 'citation' in p and p['citation'])} 篇引用信息")
    print("=" * 80)
    print(r"详细结果请查看 E:\shixun\day3\wenxian")
    print("日志文件: cnki_crawler_edge.log")