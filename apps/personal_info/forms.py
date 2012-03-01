from django.forms.models import ModelForm
from apps.personal_info.models import Person
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.layout import Div, Fieldset, HTML, Reset
from django import forms
from django.conf import settings
from crispy_forms.bootstrap import FormActions


class StolenDateWidget(forms.DateInput):
    class Media:
        js = (settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
              "/static/js/DateTimeShortcuts.js"
              )

        def __init__(self, attrs={}, format=None):
            super(StolenDateWidget, self).__init__(
                                            attrs={'class': 'vDateField',
                                                   'size': '10'},
                                                   format=format)


class PersonChange(ModelForm):
    ''' form that allows to edit data, presented on the main page
    '''
    birth = forms.DateField(required=False,
                            widget=StolenDateWidget
                            )

    def __init__(self, *args, **kw):
        super(PersonChange, self).__init__(*args, **kw)
        self.helper = FormHelper()
        self.helper.form_id = 'id-PersonChange'
        self.helper.form_class = 'PersonChangeForm'
        self.helper.form_method = 'post'
        self.helper.form_action = '/form/'
        self.helper.form_style = 'inline'

        self.fields.pop('contacts')
        self.fields.pop('photo')

        field_set = self.fields
        field_set1 = list(field_set)[:4]
        field_set1.append(HTML("""
        <div id='rovd'>
        <img style='width:100%' src='{{ object.photo }}' />
        </div>"""))
        field_set2 = list(field_set)[4:]

        field_set1.reverse()
        field_set2.reverse()

        st = Fieldset('''
                        <h3>42 Coffee Cups Test Assignment</h3>''',
                Div(*field_set1,
                    css_id='left'),
                Div(*field_set2,
                    css_id='right'),
                )
        self.helper.layout = Layout(
            st,
            FormActions(
            Submit('save_changes', 'Save', css_class="btn-primary"),
            Reset('cancel', 'Cancel', css_class="btn"),
            )
        )
        super(PersonChange, self).__init__(*args, **kw)

    class Meta:
        model = Person
