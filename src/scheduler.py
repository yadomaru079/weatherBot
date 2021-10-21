from flask import Flask, request, abort
import os
import bs
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
MY_LINE_USER_ID = os.environ["MY_LINE_USER_ID"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)

def main():
  m = bs.Message()
  todayText = m.makeMessage()
  tomorrowText = m.makeTommorowMessage()
  pushText = TextSendMessage(todayText + '\n' + '\n' + tomorrowText)
  line_bot_api.push_message(MY_LINE_USER_ID, messages=pushText)

if __name__ == "__main__":
    main()
