from django.test import TestCase
from apps.tools.models import HttpRequest
from django.test.client import Client


class RequestMWTestCase(TestCase):
    ''' test model that stores all http requests in the DB
    '''

    def test_http_requests(self):
        '''Http request -> +HttpRequest object
        '''
        objects_num = HttpRequest.objects.filter(request_path='/').count
        objects_num_before = objects_num()
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        objects_num_after = objects_num()
        self.assertEqual(1, objects_num_after - objects_num_before)

from os import path
from windmill.authoring import djangotest
import os

wmtests = path.join(path.dirname(path.abspath(__file__)), "windmilltests")
for nm in os.listdir(wmtests):
    if nm.startswith("test") and nm.endswith(".py"):
        testnm = nm[:-3]

        class WindmillTest(djangotest.WindmillDjangoUnitTest):
            fixtures = ['http_requests_db.json']
            test_dir = path.join(wmtests, nm)
            browser = "firefox"
        WindmillTest.__name__ = testnm
        globals()[testnm] = WindmillTest
        del WindmillTest
