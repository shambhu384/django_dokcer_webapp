from django.http import HttpResponse
import json
from django.shortcuts import render


def index(request):
    response_data = {
        "name": "apps",
        "data": [
            { "label": "#No Tweet at all" },
            { "label": "#Delete Facebook" }
        ]
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def render_theme(request):
    return HttpResponse('Plain text')

def render_html(request):
    context = {"message": "hello"}
    return render(request, 'index.html', context)
