from django.forms.models import ModelForm
from apps.personal_info.models import Person
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout, Div, Fieldset, HTML

class PersonChange(ModelForm):
    ''' form that allows to edit data, presented on the main page
    '''
    def __init__(self, *args, **kw):
        super(ModelForm, self).__init__(*args, **kw)
        self.helper = FormHelper()
        self.helper.form_id = 'id-PersonChange'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '/form/'
        self.helper.form_style = 'inline'
                
        field_set = self.fields
        field_set1 = list(field_set)[:4]
        field_set1.append( HTML("""
        <div id='rovd'>
        <img style='width:100%' src='{{ object.photo }}' />
        </div>""") )
        field_set2 = list(field_set)[4:] 
        
        st=Fieldset('{% if form.errors %}<h1>Please correct the following errors</h1>{% else %}<h1>Submit</h1>{% endif %}',
                Div(*field_set1,
                    css_id = 'left'),
                Div(*field_set2,
                    css_id = 'right'),
                )
        self.helper.layout = Layout(
            st,
            ButtonHolder(
                Submit('submit', 'Submit', css_id = 'submit-save', css_class='button white'),
            )
        )
        super(PersonChange, self).__init__(*args, **kw)
    
    def save(self, commit=True, force_insert=False, force_update=False):
        instance = super(PersonChange, self).save(commit=False)
        
        person = Person.objects.get(pk=1)
        
        for key in instance.__dict__:
            value = instance.__dict__[key]
            instance.__dict__[key] = value if value else person.__dict__[key]
        
        try:
            instance.bio.split()
        except AttributeError:
            pass
        else:
            if not bool(instance.bio.split()):
                instance.bio = ''
        
        try:
            instance.other_contacts.split()
        except AttributeError:
            pass
        else:
            if not bool(instance.other_contacts.split()):
                instance.other_contacts = ''
        
        if commit:
            instance.save()
        return instance
        
    class Meta:
        model = Person
    