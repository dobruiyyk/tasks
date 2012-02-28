from django.test import TestCase
from apps.tools.models import HttpRequest
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test.client import Client
from apps.personal_info.models import Person
from django.template import Template, Context, TemplateSyntaxError
from django.core.management import call_command
import sys
from django.utils.unittest.result import TestResult
from StringIO import StringIO
import textwrap
from django.utils.unittest import result
import traceback


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
        self.assertEqual(out,
                "<a href='/admin/personal_info/person/1/'>Edit (admin)</a>")

    def test_parsing_errors(self):
        "template tag won't parse anything but onject"
        render = lambda t: Template(t).render(Context())

        self.assertRaises(TemplateSyntaxError, render,
                          "{% load edit_link %}{% edit_link bla-bla %}")
"""
class PrintModelsCommandTestCase(TestCase):
    '''Create django command that prints all project models and the count of 
    objects in every model
    '''
    def test_run_command(self):
        self.assertEqual(None, call_command('print_models'))
"""
class PrintModelsCommandTestCase(TestCase):

    def setUp(self):
        self._real_out = sys.stdout
        self._real_err = sys.stderr

    def tearDown(self):
        sys.stdout = self._real_out
        sys.stderr = self._real_err

    def testBufferOutputOff(self):
        real_out = self._real_out
        real_err = self._real_err

        result = TestResult()
        self.assertFalse(result.buffer)

        self.assertIs(real_out, sys.stdout)
        self.assertIs(real_err, sys.stderr)

        result.startTest(self)

        self.assertIs(real_out, sys.stdout)
        self.assertIs(real_err, sys.stderr)

    def testBufferOutputStartTestAddSuccess(self):
        real_out = self._real_out
        real_err = self._real_err

        result = TestResult()
        self.assertFalse(result.buffer)

        result.buffer = True

        self.assertIs(real_out, sys.stdout)
        self.assertIs(real_err, sys.stderr)

        result.startTest(self)

        self.assertIsNot(real_out, sys.stdout)
        self.assertIsNot(real_err, sys.stderr)
        self.assertIsInstance(sys.stdout, StringIO)
        self.assertIsInstance(sys.stderr, StringIO)
        self.assertIsNot(sys.stdout, sys.stderr)

        out_stream = sys.stdout
        err_stream = sys.stderr

        result._original_stdout = StringIO()
        result._original_stderr = StringIO()

#        print 'foo'
#        print >> sys.stderr, 'bar'
        call_command('print_models')
        
        self.assertEqual(out_stream.getvalue(), 'Model : Permission, count : 30\nModel : Group, count : 0\nModel : User, count : 1\nModel : Message, count : 0\nModel : ContentType, count : 10\nModel : Session, count : 0\nModel : Site, count : 1\nModel : LogEntry, count : 0\nModel : Person, count : 1\nModel : HttpRequest, count : 0\n')
        self.assertEqual(err_stream.getvalue(), 'error: Model : Permission, count : 30\n\nerror: Model : Group, count : 0\n\nerror: Model : User, count : 1\n\nerror: Model : Message, count : 0\n\nerror: Model : ContentType, count : 10\n\nerror: Model : Session, count : 0\n\nerror: Model : Site, count : 1\n\nerror: Model : LogEntry, count : 0\n\nerror: Model : Person, count : 1\n\nerror: Model : HttpRequest, count : 0\n\n')

        self.assertEqual(result._original_stdout.getvalue(), '')
        self.assertEqual(result._original_stderr.getvalue(), '')

        result.addSuccess(self)
        result.stopTest(self)

        self.assertIs(sys.stdout, result._original_stdout)
        self.assertIs(sys.stderr, result._original_stderr)

        self.assertEqual(result._original_stdout.getvalue(), '')
        self.assertEqual(result._original_stderr.getvalue(), '')

        self.assertEqual(out_stream.getvalue(), '')
        self.assertEqual(err_stream.getvalue(), '')

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
