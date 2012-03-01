from apps.tools.models import HttpRequest
from django.shortcuts import render_to_response
from django.template import RequestContext


def requests(request):
    '''View for the /requests/ page
    on a separate page show first 10 http requests
    that are stored by middleware
    '''
    last_requests = HttpRequest.objects.order_by('time')[:10].values_list(
                                                    'ip', 'time',
                                                    'request_method',
                                                    'request_path')
    return render_to_response('tools/requests.html',
                              {'last_requests': last_requests},
                              context_instance=RequestContext(request))
