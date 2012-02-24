from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import TestCase
import os
from django.contrib.auth.models import User
from apps.personal_info.models import Person
from django.test.client import Client
from django_webtest import WebTest


class FilesTestCase(TestCase):
    '''ticket1 : required files
    '''
    def test_files(self):
        '''Files existance check -*-.gitignore, Makefile, requrements.txt -*-
        '''
        is_file = os.path.isfile
        self.assertEqual(True, is_file('.gitignore'))
        self.assertEqual(True, is_file('Makefile'))
        self.assertEqual(True, is_file('requirements.txt'))

    def test_fixture(self):
        '''Fixture check -*- default admin@admin user presence + info-*-
        '''
        admin = User.objects.get(username='admin')
        self.assertEqual('admin', admin.username)

        password = u'sha1$7e4c2$b0921efc8462153d88a755436e3f371d67dadf1d'
        self.assertEqual(password, admin.password)
        info = Person.objects.get(pk=1)
        self.assertEqual('Dmitry', info.name)


class AuthTestCase(TestCase):
    '''Different situations where user authentification is involved
    '''
    def setUp(self):
        '''Every test needs a client.
        '''
        self.c = Client()

    def test_login(self):
        '''url '/login/' : test client login capability
        '''
        self.c.post('/login/', {'username': 'admin', 'password': 'admin'})
        response = self.c.get('/login/')
        self.assertEqual(response.context['user'].username, u'admin')
        self.c.logout()
        response = self.c.get('/login/')
        self.assertNotEqual(response.context['user'].username, u'admin')

    def test_form_auth(self):
        '''get '/form/' = redirect to login page if anonymous
                                else response.status_code, 200
        '''
        response = self.c.get('/form/', follow=True)
        self.assertEqual(response.redirect_chain,
                         [('http://testserver/login/?next=/form/', 302)],)
        self.assertEqual(response.context['user'].username, '')

        self.c.login(username='admin', password='admin')
        response = self.c.get('/form/')
        self.assertEqual(response.context['user'].username, u'admin')
        response = self.c.get('/form/')
        self.assertEqual(response.status_code, 200)


class FormTestCase(WebTest):
    '''functionality of the /form/ form
    '''
    def test_my_view(self):
        c = Client()
        c.login(username='admin', password='admin')
        res = self.app.get('/form/', user='admin')
        self.assertEqual(res.status, '200 OK')
        form = self.app.get('/form/').forms

        for field in ('bio', 'last_name', 'name',
#                      'contacts',
                      'email', 'other_contacts', 'skype', 'jabber'):
            form = self.app.get('/form/').form
            form[field] = '1@1.com'
            response = form.submit().follow()
            self.assertEqual(response.context['object'][field], '1@1.com')

from os import path
from windmill.authoring import djangotest

wmtests = path.join(path.dirname(path.abspath(__file__)), "windmilltests")
for nm in os.listdir(wmtests):
    if nm.startswith("test") and nm.endswith(".py"):
        testnm = nm[:-3]

        class WindmillTest(djangotest.WindmillDjangoUnitTest):
            test_dir = path.join(wmtests, nm)
            browser = "firefox"
        WindmillTest.__name__ = testnm
        globals()[testnm] = WindmillTest
        del WindmillTest
