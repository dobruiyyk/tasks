from django.contrib.gis.utils import GeoIP
from apps.tools.models import HttpRequest
import datetime

class save_httprequest_to_db():
    def process_request(self, request):
        g = GeoIP()
        user = request.user if not 'Anonumous' else ':('
        time = datetime.datetime.now().replace(microsecond=0)
        ip = request.META['REMOTE_ADDR']
        try:    
            country = g.country(str(ip))['country_name'] 
        except:
            country = ':('
        request_path = request.path
        request_method = request.method
        obj = HttpRequest(user=user,
                            time=time,
                            country=country,
                            ip=ip,
                            request_path=request_path,
                            request_method=request_method)
        obj.save()
        return None  