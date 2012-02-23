from apps.personal_info.models import Person
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from apps.personal_info.forms import PersonChange


def main_page(request):
    '''View for the main page
       Create basic django-project with name,
       surname, date of birth, bio, contacts on the main page.
    '''
    person = Person.objects.get(pk=1)
    return render_to_response('personal_info/main_page.html',
                              {'object': person.__dict__},
                              context_instance=RequestContext(request))
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def main_page_form(request, val=None):
    ''' form that allows to edit data, presented on the main page
    '''
    person = Person.objects.get(pk=1)
    if request.method == 'POST':
        form = PersonChange(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PersonChange(instance=person)

    return render_to_response('personal_info/main_page_form.html',
                              {'form': form,
                               'object': person},
                              context_instance=RequestContext(request))
