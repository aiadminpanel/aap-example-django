from datetime import datetime, timezone

from django.http import HttpResponse, JsonResponse
from django.urls import path


def index(_request):
    now = datetime.now(timezone.utc).isoformat()
    return HttpResponse(
        "<!doctype html><title>aap-example:django</title><h1>Django</h1>"
        f"<p>Served at {now}. Marker: <code>aap-example:django</code></p>"
    )


def healthz(_request):
    return JsonResponse({"ok": True})


urlpatterns = [
    path("", index),
    path("healthz", healthz),
]
