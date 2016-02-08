from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from bookwormsunite.models import Readathon

@require_http_methods(["GET"])
def index(request):
    html = "<html><body>index</body></html>"
    return HttpResponse(html)


@require_http_methods(["GET", "POST"])
def readathon_info(request, readathon_name_slug):
    html = "<html><body>readathon_info: {0}</body></html>".format(readathon_name_slug)
    return HttpResponse(html)


@require_http_methods(["GET"])
def user_info(request, uid):
    html = "<html><body>user_info: {0}</body></html>".format(uid)
    return HttpResponse(html)


@require_http_methods(["GET"])
def user_summary(request, uid):
    html = "<html><body>user_summary: {0}</body></html>".format(uid)
    return HttpResponse(html)


@require_http_methods(["POST"])
def login(request):
    html = "<html><body>login</body></html>"
    return HttpResponse(html)


@require_http_methods(["POST"])
def register(request):
    html = "<html><body>register</body></html>"
    return HttpResponse(html)


@require_http_methods(["POST"])
def search(request, readathonName):
    try:
        readathons = Readathon.objects.filter(name=readathonName)
    except Readathon.DoesNotExist:
        readathons = None
        pass

    html = "<html><body>search: {{s}}</body></html>"
    return HttpResponse(html)
