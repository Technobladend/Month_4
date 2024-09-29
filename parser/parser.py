import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt


URL = "http://www.manascinema.com/movies"
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}


def get_html_content(url, params=None):
    """
    возвращает html код страницы
    """
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        raise e


def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all(
        "div", class_="short_movie_info"
    )
    manas_films = []

    if items:
        for item in items:
            title_div = item.find("div", class_="m_title")
            title_url = item.find("a")
            image_div = item.find("div", class_="m_thumb").find('img')

            title_name = title_div.get_text() if title_div else 'Нет названия'
            title_url = URL + title_url.get('href') if title_url else 'Нет ссылки'
            image_url = URL + image_div.get('src') if image_div else 'Нет картинки'

            manas_films.append(
                {
                    "title_name": title_name,
                    "title_url": title_url,
                    "image": image_url,
                }
            )

        return manas_films


def parser(pages=1):
    manas_films = []
    try:
        for page in range(pages):
            params = {"page": page}
            html = get_html_content(URL, params=params)

            if html:
                films = get_data(html.text)
                if films:
                    manas_films.extend(films)

                else:
                    raise f'no films was found on page {page}'

            else:
                raise f'no films was found on page {page}'
        return manas_films
    except Exception as e:
        raise e