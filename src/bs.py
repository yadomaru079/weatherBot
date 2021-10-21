import requests
from bs4 import BeautifulSoup

class Message:

  # スクレイピング対象の URL にリクエストを送り HTML を取得する
  res = requests.get('https://tenki.jp/indexes/cloth_dried/3/16/4410/13104/')

  # レスポンスの HTML から BeautifulSoup オブジェクトを作る
  soup = BeautifulSoup(res.text, 'html.parser')
  #def __init__(self):

  def makeMessage(self):
    # CSS セレクターを使って今日の洗濯情報を抽出＆形成
    today = self.soup.select_one('section.section-wrap time.date-time').get_text()
    today += "のお天気だぬお！"
  
    message = self.soup.select_one('section.today-weather span.indexes-telop-0').get_text()
    message = message + "、"

    detailMessage = self.soup.select_one('section.today-weather p.indexes-telop-1').get_text()
    detailMessage += "ぬお"
    
    todayTenki = self.soup.select_one('section.today-weather p.weather-telop').get_text()
    todayTenki = "今日の天気は" + todayTenki
    
    todayHighTemp = self.soup.select_one('section.today-weather span.high-temp').get_text()
    todayHighTemp = "最高気温は" + todayHighTemp

    todayLowTemp = self.soup.select_one('section.today-weather span.low-temp').get_text()
    todayLowTemp = "最低気温は" + todayLowTemp

    todayRainyPercent = self.soup.select_one('section.today-weather span.precip').get_text()
    todayRainyPercent = "降水確率は" + todayRainyPercent+ "だぬお！"

    returnMessage = today + '\n' + message + detailMessage + '\n' + todayTenki + '\n' + todayHighTemp + '\n' + todayLowTemp + '\n' + todayRainyPercent

    return returnMessage

  def makeTomorrowMessage(self):
    # CSS セレクターを使って明日の洗濯情報を抽出＆形成
  
    tomorrowMessage = self.soup.select_one('section.tomorrow-weather span.indexes-telop-0').get_text()
    tomorrowMessage = tomorrowMessage + "、"

    tomorrowDetailMessage = self.soup.select_one('section.tomorrow-weather p.indexes-telop-1').get_text()
    tomorrowDetailMessage += "ぬお"
    
    tomorrowTenki = self.soup.select_one('section.tomorrow-weather p.weather-telop').get_text()
    tomorrowTenki = "明日の天気は" + tomorrowTenki
    
    tomorrowHighTemp = self.soup.select_one('section.tomorrow-weather span.high-temp').get_text()
    tomorrowHighTemp = "最高気温は" + tomorrowHighTemp

    tomorrowLowTemp = self.soup.select_one('section.tomorrow-weather span.low-temp').get_text()
    tomorrowLowTemp = "最低気温は" + tomorrowLowTemp

    tomorrowRainyPercent = self.soup.select_one('section.tomorrow-weather span.precip').get_text()
    tomorrowRainyPercent = "降水確率は" + tomorrowRainyPercent + "だぬお！"

    returnMessage = "続いて明日の洗濯情報ぬお！" + '\n' + tomorrowMessage + tomorrowDetailMessage + '\n' + tomorrowTenki + '\n' + tomorrowHighTemp + '\n' + tomorrowLowTemp + '\n' + tomorrowRainyPercent

    return returnMessage