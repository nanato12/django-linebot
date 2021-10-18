import os
from typing import List

from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from linebot.models.events import Event
from linebot.webhook import WebhookParser


@csrf_exempt
def callback(request: HttpRequest) -> HttpResponse:
    parser = WebhookParser(os.environ["LINE_CHANNEL_SECRET"])
    events: List[Event] = parser.parse(
        request.body.decode("utf-8"), request.headers["X-Line-Signature"]
    )
    for event in events:
        print(event)
    return HttpResponse("OK")
