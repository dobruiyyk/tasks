from django.test import TestCase
from apps.tools.models import HttpRequest
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test.client import Client
from apps.personal_info.models import Person
from django.template import Template, Context, TemplateSyntaxError


class RequestMWTestCase(TestCase):
    ''' test model that stores all http requests in the DB
    '''
    def testHttpRequests(self):
        '''Http request -> +HttpRequest object
        '''

        objects_num = HttpRequest.objects.filter(request_path='/').count
        objects_num_before = objects_num()
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        objects_num_after = objects_num()
        self.assertEqual(1, objects_num_after - objects_num_before)

    def testContextProcessor(self):
        '''Context processor with django.conf.settings
        '''
        from django.conf import settings
        c = Client()
        response = c.get('/')
        self.assertEqual(response.context['settings'], settings)

    def testSettings(self):
        '''Required params in settings.py
        '''
        from django.conf import settings
        self.assertEqual(True, bool(settings.TEMPLATE_CONTEXT_PROCESSORS))


class TemplateTagsTestCase(TestCase):
    '''tag accepts any object and renders the link to its admin edit page
    ('{% edit_link request.user %}')
    '''
    def test_get_tag_for_pk1_user(self):
        "tag for Person.objects.get(pk=1)"
        out = Template(
                "{% load edit_link %}"
                "{% edit_link person %}"
            ).render(Context({
                'person': Person.objects.get(pk=1)
            }))
        self.assertEqual(out, "<a href='/admin/personal_info/person/1/'</a>")

    def test_parsing_errors(self):
        "template tag won't parse anything but onject"
        render = lambda t: Template(t).render(Context())

        self.assertRaises(TemplateSyntaxError, render,
                          "{% load edit_link %}{% edit_link bla-bla %}")

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
