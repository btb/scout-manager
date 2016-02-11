from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from htmlmin.decorators import minified_response
from scout.space_dao import get_spot_list, get_spot_by_id

# Create your views here.

def list(request):
    spots = get_spot_list()
    context = {"spots": spots}
    return render_to_response('scout_manager/list.html', context,
                              context_instance=RequestContext(request))


def add(request):
    return render_to_response(
        'scout_manager/add.html',
        context_instance=RequestContext(request))
        
def item(request):
    return render_to_response(
        'scout_manager/item.html',
        context_instance=RequestContext(request))


def publish(request):
    return render_to_response(
        'scout_manager/publish.html',
        context_instance=RequestContext(request))
        
def space(request):
    return render_to_response(
        'scout_manager/space.html',
        context_instance=RequestContext(request))
