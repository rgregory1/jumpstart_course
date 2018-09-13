import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                    'cond, temp, scale, loc')

def main():
    print_the_header()
    code = input('What zipcode do you want the weather for (97201)? ')
    code = code.lower().strip()
    html = get_html_from_web(code)
    report = get_weather_from_html(html)

    print('The temp in {} is {} {} and {}'.format(
      report.loc,
      report.temp,
      report.scale,
      report.cond,
      ))

def print_the_header():
    print('--------------------------------------')
    print('            WEATHER APP')
    print('--------------------------------------')
    print()

def get_html_from_web(zipcode):
    # url = 'https://www.wunderground.com/weather/us/vt/{}'.format(town)
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])
    return response.text

def get_weather_from_html(html):
    # cityCss = ''
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup)
    loc = soup.find(class_='city-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').find('p').get_text()
    temp = soup.find(class_='current-temp').find(class_='wu-value').get_text()
    scale = soup.find(class_='current-temp').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    #print(loc, condition, temp, scale)
    # return loc, condition, temp, scale
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report

def cleanup_text(text : str):
    if not text:
        return text
    text = text.strip()
    return text

if __name__ == '__main__':
    main()
