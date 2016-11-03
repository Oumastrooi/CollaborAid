from django.http import HttpResponse
from django.template import RequestContext

def index(request):
    """
    Return a list of stories that match the provided search term
    in either the title or the main content.
    """
    return HttpResponse("Hello, world. You're at the polls index.")

