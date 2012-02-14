from django.test import TestCase
from apps.tools.models import HttpRequest
from django.test.client import Client


class RequestMWTestCase(TestCase):
    ''' test model that stores all http requests in the DB
    '''
    
    def testHttpRequests(self):
        '''Http request -> +HttpRequest object
        '''
        
        objects_num = HttpRequest.objects.filter(request_path = '/').count
        objects_num_before = objects_num()
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        objects_num_after = objects_num()
        self.assertEqual(1, objects_num_after - objects_num_before)

    def testContextProcessor(self):
        '''Context processor with settings.__dict__
        '''
        import settings
        c = Client()
        response = c.get('/')
        settings_dict = settings.__dict__
        context_dict = response.context
        for i,j in settings_dict.items():
            self.assertEqual(context_dict[i], j)