from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
    """
    Return a list of stories that match the provided search term
    in either the title or the main content.
    """
    return HttpResponse("Hello, world. You're at the polls index.")
#    return render_to_response("index.html", {}, RequestContext(request))

