from apps.personal_info.models import Person
from django.shortcuts import render_to_response
from django.template import RequestContext

def main_page(request):
    '''View for the main page
        
        Create basic django-project with name,
        surname, date of birth, bio, contacts on the main page.
    
    '''
    person = Person.objects.get(pk=1)
    return render_to_response('personal_info/main_page.html',
                              {'object': person.__dict__}, 
                              context_instance=RequestContext(request))