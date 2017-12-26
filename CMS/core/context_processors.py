from django.conf import settings
from entries.models import Category


def entries__categories(request):
    context = {
        'entries__categories': Category.objects.all()
    }
    return context
