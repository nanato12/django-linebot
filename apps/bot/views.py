import os

from django.core.exceptions import BadRequest
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage
from linebot.models.events import MessageEvent, TextMessage
from linebot.models.sources import SourceGroup, SourceRoom, SourceUser
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

    # profile
    if isinstance(event.source, SourceUser):
        profile = bot.get_profile(event.source.user_id)
    elif isinstance(event.source, SourceGroup):
        profile = bot.get_group_member_profile(
            event.source.group_id, event.source.user_id
        )
    elif isinstance(event.source, SourceRoom):
        profile = bot.get_room_member_profile(
            event.source.room_id, event.source.user_id
        )
    else:
        raise Exception("Invalid event.source type")

    if message.text == "メニュー":
        send_message = TextSendMessage("メニュー")
    elif message.text == "完了":
        send_message = TextSendMessage("注文を受付ました。")
    elif message.text == "なまえ":
        send_message = TextSendMessage(profile.display_name)
    else:
        send_message = TextSendMessage("テストメッセージ")

    bot.reply_message(event.reply_token, send_message)
