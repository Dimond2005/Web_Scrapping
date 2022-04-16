import requests
import bs4


def to_set(input):
    clean_set = set(clean.text.strip() for clean in input)
    return clean_set


Headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.shicheng.one',
    'Referer': 'https://www.shicheng.one/user/login',
    'Upgrade-Insecure-Requests': '1'
}

# определяем список ключевых слов
KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Информационная безопасность *'}

responce = requests.get('https://habr.com/ru/all/', headers=Headers)
text = responce.text

soup = bs4.BeautifulSoup(text, features='html.parser')
data = soup.findAll('article')

for article in data:
    date = article.find_all(class_='tm-article-snippet__datetime-published')
    titles = article.find_all(class_='tm-article-snippet__title-link')
    tag = article.find_all(class_='tm-article-snippet__hubs-item')
    if len(KEYWORDS.intersection(to_set(tag))) != 0:
        for hub in titles:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = "https://habr.com/ru/all/" + href
            print(to_set(date), to_set(titles), link)


