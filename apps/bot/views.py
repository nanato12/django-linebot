import os

from django.core.exceptions import BadRequest
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage
from linebot.models.events import MessageEvent, TextMessage
from linebot.webhook import WebhookHandler

handler = WebhookHandler(os.environ["LINE_CHANNEL_SECRET"])


@csrf_exempt
def callback(request: HttpRequest) -> HttpResponse:
    try:
        handler.handle(
            request.body.decode("utf-8"), request.headers["X-Line-Signature"]
        )
    except InvalidSignatureError:
        raise BadRequest("Invalid request.")
    return HttpResponse("OK")


@handler.add(MessageEvent, message=TextMessage)
def text_message(event: MessageEvent) -> None:
    # LINEBot
    bot = LineBotApi(os.environ["LINE_CHANNEL_ACCESS_TOKEN"])

    # message
    message: TextMessage = event.message

    if message.text == "メニュー":
        send_message = TextSendMessage("メニュー")
    elif message.text == "完了":
        send_message = TextSendMessage("注文を受付ました。")
    else:
        send_message = TextSendMessage("テストメッセージ")

    bot.reply_message(event.reply_token, send_message)
