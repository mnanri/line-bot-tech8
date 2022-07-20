import logging
import os
import azure.functions as func
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

# Azure FunctionsのApplication Settingに設定した値から取得する↓
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # get x-line-signature header value
    signature = req.headers['x-line-signature']

    # get request body as text
    body = req.get_body().decode("utf-8")
    logging.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        func.HttpResponse(status_code=400)

    return func.HttpResponse('OK')


def get_answer(name: str, question: str):
    f = open("./LineAzureHandler/db.json", "r")
    db_json = json.load(f)
    return db_json[name][question]


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    _body = event.message.text.split("/")
    name = _body[0]
    question = _body[1]
    answer = get_answer(name, question)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=answer)
    )
