from apps.tools.models import HttpRequest
import datetime


class save_httprequest_to_db():
    '''middleware that stores all http requests in DB
    '''
    def process_request(self, request):
        user = request.user if not 'Anonumous' else ':('
        time = datetime.datetime.now().replace(microsecond=0)
        ip = request.META['REMOTE_ADDR']
        request_path = request.path
        request_method = request.method
        obj = HttpRequest(user=user,
                            time=time,
                            ip=ip,
                            request_path=request_path,
                            request_method=request_method)
        obj.save()
        return None
