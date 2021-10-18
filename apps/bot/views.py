from django.http import HttpRequest, HttpResponse


def callback(request: HttpRequest) -> HttpResponse:
    return HttpResponse("OK")
