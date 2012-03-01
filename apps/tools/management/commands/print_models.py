from django.db.models import get_app, get_models
from django.core.management.base import NoArgsCommand
from django.conf import settings


class Command(NoArgsCommand):
    help = "Print all models to the console."

    def handle_noargs(self, **options):
        apps = []
        for app in settings.INSTALLED_APPS:
            apps.append(app.split('.')[-1])

        for app in apps:
            models = get_models(get_app(app))

            if models:
#                self.stdout.write('\nApplication : %s\n' % app)
                for model in models:
                    model.count = model.objects.all().count()
                    model = 'Model : %s, count : % s\n' % (model.__name__,
                                                               model.count)
                    self.stdout.write(model)
                    self.stderr.write('error: %s\n' % model)
#            else:
#                self.stdout.write(' /--No Models\n')
