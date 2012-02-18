from django.test import TestCase
import os
from django.contrib.auth.models import User
from apps.personal_info.models import Person
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test.client import Client

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
        self.assertEqual(u'sha1$7e4c2$b0921efc8462153d88a755436e3f371d67dadf1d',
                         admin.password)
        info = Person.objects.get(pk=1)
        self.assertEqual('Dmitry', info.name)

class AuthFormTestCase(TestCase):
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
                         [(u'http://testserver/login/', 302)],)
        self.assertEqual(response.context['user'].username, u'Anonymous')
        
        self.c.login(username='admin', password='admin')
        response = self.c.get('/form/', follow=True)
        self.assertEqual(response.context['name'], 'admin')
        response = self.c.get('/form/')
        self.assertEqual(response.status_code, 200)
        
    def test_form_func(self):
        '''functionality of the /form/ form
        '''
        self.c.post('/login/', {'username': 'admin', 'password': 'admin'})
        person_objects = Person.objects.get(pk=1).__dict__
        from copy import deepcopy
        person_objects_copy = deepcopy(person_objects)
        self.assertEqual(sorted(person_objects), sorted(person_objects_copy))
        for i in ('bio', 'last_name', 'name', 'contacts',
                  'other_contacts', 'skype', 'email', 'jabber'):
            self.assertEqual(person_objects[i], person_objects_copy[i])
            self.c.post('/form/', {'%s'%i: '1@1.com'})
            self.assertNotEqual(person_objects[i], person_objects_copy[i])
        
from os import path
from windmill.authoring import djangotest
 
wmtests = path.join(path.dirname(path.abspath(__file__)),"windmilltests")
for nm in os.listdir(wmtests):
    if nm.startswith("test") and nm.endswith(".py"):
        testnm = nm[:-3]
        class WindmillTest(djangotest.WindmillDjangoUnitTest):
            test_dir = path.join(wmtests, nm)
            browser = "firefox"
        WindmillTest.__name__ = testnm
        globals()[testnm] = WindmillTest
        del WindmillTest