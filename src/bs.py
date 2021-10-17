import requests
from bs4 import BeautifulSoup

class Message:

  # スクレイピング対象の URL にリクエストを送り HTML を取得する
  res = requests.get('https://tenki.jp/indexes/cloth_dried/3/16/4410/13104/')

  # レスポンスの HTML から BeautifulSoup オブジェクトを作る
  soup = BeautifulSoup(res.text, 'html.parser')
  #def __init__(self):

  def makeMessage(self):
    # CSS セレクターを使って 
    today = self.soup.select_one('section.section-wrap time.date-time').get_text()
  
    message = self.soup.select_one('section.today-weather span.indexes-telop-0').get_text()
    message = message + "、"

    detailMessage = self.soup.select_one('section.today-weather p.indexes-telop-1').get_text()
    
    todayTenki = self.soup.select_one('section.today-weather p.weather-telop').get_text()
    todayTenki = "今日の天気は" + todayTenki
    
    todayHighTemp = self.soup.select_one('section.today-weather span.high-temp').get_text()
    todayHighTemp = "最高気温は" + todayHighTemp

    todayLowTemp = self.soup.select_one('section.today-weather span.low-temp').get_text()
    todayLowTemp = "最低気温は" + todayLowTemp

    todayRainyPercent = self.soup.select_one('section.today-weather span.precip').get_text()
    todayRainyPercent = "降水確率は" + todayRainyPercent
    

    returnMessage = today + '\n' + message + detailMessage + '\n' + todayTenki + '\n' + todayHighTemp + '\n' + todayLowTemp + '\n' + todayRainyPercent

    return returnMessage