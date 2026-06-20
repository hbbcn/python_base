import requests
from IPython.core.interactiveshell import make_main_module_type
from lxml import html
import csv
import re

# 常量
MOVE_LIST_FILE = "csv_data/move_list_optimize.csv"
TMDB_BASE_URL = "https://www.themoviedb.org"

TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"  # 高分电影榜单的url(默认第1也3)

TMDB_TOP_URL_PATTERN = r"https://www.themoviedb.org/movie/top-rated\?page=\d+"

def save_all_movies(movies):
    if not movies:
        print("没有数据可保存")
        return
    with open(MOVE_LIST_FILE, "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=movies[0].keys())
        writer.writeheader()
        writer.writerows(movies)
    print(f"成功保存 {len(movies)} 条电影数据到 {MOVE_LIST_FILE}")


def get_movie_year(movie_year):
    # 去除括号
    movie_year = movie_year.replace("(", "").replace(")", "")
    return movie_year


def get_movie_release(movie_release):
    # 处理上映时间 ,将 1957-04-10(US) 转为 1957-04-10
    return re.search(r"\d{4}-\d{2}-\d{2}",movie_release).group()


def get_movie_duration(movie_duration):
    # 转为分钟
    h_res = re.search(r"(\d+)h",movie_duration)
    m_res = re.search(r"(\d+)m",movie_duration)
    h = int(h_res.group(1) if h_res else 0)
    m = int(m_res.group(1) if m_res else 0)
    return h * 60 + m

def get_movie_detail(movie_url):
    """
    获取电影详情数据
    :param movie_url: 电影详情页的url
    :return:
    """
    print(f"发起请求{movie_url}, 获取电影详情数据...")
    # 发送请求 获取电影详情数据
    movie_response = requests.get(movie_url, timeout=60)
    movie_doc = html.fromstring(movie_response.text)
    # 电影名称
    movie_name_list = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    movie_name = movie_name_list[0].strip() if movie_name_list else '未知'
    # 年份
    movie_year_list = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    movie_year = movie_year_list[0].strip() if movie_year_list else ''
    movie_year = get_movie_year(movie_year)
    # 上映时间
    movie_release_list = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")
    movie_release = movie_release_list[0].strip() if movie_release_list else ''
    movie_release = get_movie_release(movie_release)
    # 电影类型
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    # 电影时长
    movie_duration_list = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    movie_duration = movie_duration_list[0].strip() if movie_duration_list else ''
    movie_duration = get_movie_duration(movie_duration)
    # 评分
    movie_score_list = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_score = movie_score_list[0].strip() if movie_score_list else ''
    # 语言
    movie_language_list = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movie_language = movie_language_list[0].strip() if movie_language_list else ''
    # 导演
    movie_director_list = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    movie_director = movie_director_list[0].strip() if movie_director_list else ''
    # 作者
    movie_author_list = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    movie_author = movie_author_list[0].strip() if movie_author_list else ''

    # 宣传标语
    movie_slogan_list = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")
    movie_slogan = movie_slogan_list[0].strip() if movie_slogan_list else ''

    # 简介
    movie_intro_list = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")
    movie_introduction = movie_intro_list[0].strip() if movie_intro_list else ''

    # 返回电影详情 ---字典
    move_info = {
        "电影名": movie_name,
        "年份": movie_year,
        "上映时间": movie_release,
        "电影类型": ",".join(movie_tags) if movie_tags else '',
        "电影时长": movie_duration,
        "评分": movie_score,
        "语言": movie_language,
        "导演": movie_director,
        "作者": movie_author,
        "宣传标语": movie_slogan,
        "简介": movie_introduction
    }
    return move_info
    print(move_info)
    # print(movie_name,":", movie_year,":" , movie_time, movie_tags, movie_time,movie_score,movie_language,movie_director,movie_author,movie_slogan,movie_introduction)

def main():
    print("发送请求，获取TMDB电影榜单数据...")
    # 1.发送请求, 获取高分电影榜单数据
    # 循环获取电影列表1-5页
    all_movies = []
    for page in range(1, 6):
        # 使用 f-string 直接把页码拼接到 ?page= 后面
        tmdb_top_url = f"{TMDB_TOP_URL}?page={page}"
        print(f"开始获取第{page}页数据...")
        print(f"正在请求: {tmdb_top_url}")
        response = requests.get(tmdb_top_url, timeout=60)
        response.encoding = "utf-8"
        document = html.fromstring(response.text)
        # 2.解析数据 获取电影列表
        # movie_list = document.xpath("//*[@id='page_1']/div/div/div[@class='comp:poster-card w-full bg-white border border-light-grey hover:border-gray-300 rounded-lg shadow-lg overflow-hidden']")
        movie_list = document.xpath("//*[@class='media-list-results contents']/div[@class='comp:poster-card w-full bg-white border border-light-grey hover:border-gray-300 rounded-lg shadow-lg overflow-hidden']")
        # 3.遍历电影列表，获取电影详情
        for movie in movie_list:
            movie_urls =  movie.xpath("./div/div/a/@href")
            if movie_urls:
                # 电影详情页面的url
                movie_url = TMDB_BASE_URL + movie_urls[0]
                # 发送请求，获取电影详情数据
                movie_info = get_movie_detail(movie_url)
                all_movies.append(movie_info)

    # 4.保存数据 到csv文件中
    print("保存数据到csv文件中...")
    save_all_movies(all_movies)

if __name__ == '__main__':
    main()