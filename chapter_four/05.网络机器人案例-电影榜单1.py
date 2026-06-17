import requests
from IPython.core.interactiveshell import make_main_module_type
from lxml import html
import csv

# 常量
MOVE_LIST_FILE = "csv_data/move_list.csv"
TMDB_BASE_URL = "https://www.themoviedb.org"

TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"

def save_all_movies(movies):
    if not movies:
        print("没有数据可保存")
        return
    with open(MOVE_LIST_FILE, "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=movies[0].keys())
        writer.writeheader()
        writer.writerows(movies)
    print(f"成功保存 {len(movies)} 条电影数据到 {MOVE_LIST_FILE}")

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
    movie_name = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")[0]
    # 年份
    movie_year = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")[0]
    # 上映时间
    movie_time = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()")[0]
    # 电影类型
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()")
    # 电影时长
    movie_time = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()")[0]
    # 评分
    movie_score = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    # 语言
    movie_language = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    # 导演
    movie_director = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    # 作者
    movie_author = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")

    # 宣传标语
    movie_slogan = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")

    # 简介
    movie_introduction = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")

    # 返回电影详情 ---字典
    move_info = {
        "电影名": movie_name.strip() if movie_name else '',
        "年份": movie_year.strip() if movie_year else '',
        "上映时间": movie_time.strip() if movie_time else '',
        "电影类型": ",".join(movie_tags) if movie_tags else '',
        "电影时长": movie_time.strip() if movie_time else '',
        "评分": movie_score[0].strip() if movie_score else '',
        "语言": movie_language[0].strip() if movie_language else '',
        "导演": movie_director[0].strip() if movie_director else '',
        "作者": movie_author[0].strip() if movie_author else '',
        "宣传标语": movie_slogan[0].strip() if movie_slogan else '',
        "简介": movie_introduction[0].strip() if movie_introduction else ''


    }
    return move_info
    print(move_info)
    # print(movie_name,":", movie_year,":" , movie_time, movie_tags, movie_time,movie_score,movie_language,movie_director,movie_author,movie_slogan,movie_introduction)

def main():
    print("发送请求，获取TMDB电影榜单数据...")
    # 1.发送请求, 获取高分电影榜单数据
    response = requests.get(TMDB_TOP_URL, timeout=60)
    response.encoding = "utf-8"
    document = html.fromstring(response.text)
    # 2.解析数据 获取电影列表
    # movie_list = document.xpath("//*[@id='page_1']/div/div/div[@class='comp:poster-card w-full bg-white border border-light-grey hover:border-gray-300 rounded-lg shadow-lg overflow-hidden']")
    movie_list = document.xpath("//*[@class='media-list-results contents']/div[@class='comp:poster-card w-full bg-white border border-light-grey hover:border-gray-300 rounded-lg shadow-lg overflow-hidden']")

    # 3.遍历电影列表，获取电影详情
    all_movies = []
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