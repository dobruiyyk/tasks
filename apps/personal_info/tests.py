from django.test import TestCase
import os
from django.contrib.auth.models import User
from apps.personal_info.models import Person

class FilesTestCase(TestCase):
    def testFiles(self):
        '''Files existance check -*-.gitignore, Makefile, requrements.txt -*-
        '''
        current_dir = os.getcwd()
        current_dir_list = current_dir.split('/')
        task_num = current_dir_list.index('tasks') + 1
        project_dir_list = current_dir_list[:task_num]
        project_dir = '/'.join(project_dir_list)
        is_file=os.path.isfile
        self.assertEqual(True, is_file(project_dir + '/.gitignore'))
        self.assertEqual(True, is_file(project_dir + '/Makefile'))
        self.assertEqual(True, is_file(project_dir + '/requrements.txt'))
        

    def testFixture(self):
        '''Fixture check -*- default admin@admin user presence + info-*-
        '''
        admin=User.objects.get(username='admin')
        self.assertEqual('admin', admin.username)
        self.assertEqual(u'sha1$7e4c2$b0921efc8462153d88a755436e3f371d67dadf1d',
                         admin.password)
        info = Person.objects.get(pk=1)
        self.assertEqual('Dmitry', info.name)
        
from os import path
from windmill.authoring import djangotest
 
wmtests = path.join(path.dirname(path.abspath(__file__)),"windmilltests")
for nm in os.listdir(wmtests):
    if nm.startswith("test") and nm.endswith(".py"):
        testnm = nm[:-3]
        class WindmillTest(djangotest.WindmillDjangoUnitTest):
            test_dir = path.join(wmtests,nm)
            browser = "firefox"
        WindmillTest.__name__ = testnm
        globals()[testnm] = WindmillTest
        del WindmillTest