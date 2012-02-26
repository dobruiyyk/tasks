from django.forms.models import ModelForm
from apps.personal_info.models import Person
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout
from crispy_forms.layout import Div, Fieldset, HTML, Reset


class PersonChange(ModelForm):
    ''' form that allows to edit data, presented on the main page
    '''
    def __init__(self, *args, **kw):
        super(PersonChange, self).__init__(*args, **kw)
        self.helper = FormHelper()
        self.helper.form_id = 'id-PersonChange'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '/form/'
        self.helper.form_style = 'inline'

        field_set = self.fields
        field_set1 = list(field_set)[:4]
        field_set1.append(HTML("""
        <div id='rovd'>
        <img style='width:100%' src='{{ object.photo }}' />
        </div>"""))
        field_set2 = list(field_set)[4:]

        st = Fieldset('''
                      <h2>42 Coffee Cups Test Assignment</h2>''',
                Div(*field_set1,
                    css_id='left'),
                Div(*field_set2,
                    css_id='right'),
                )
        self.helper.layout = Layout(
            st,
            ButtonHolder(
                Submit('submit', 'Save',
                       css_id='submit-save',
                       css_class='button white'),
                Reset('reset', 'Cancel',
                       css_id='submit-save',
                       css_class='button white'),
            )
        )

    class Meta:
        model = Person
