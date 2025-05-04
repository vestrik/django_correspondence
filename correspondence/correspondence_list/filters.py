import django_filters

from accounts.models import Department
from .models import Correspondence

class CorrespondenceFilter(django_filters.FilterSet):

    department = django_filters.ModelChoiceFilter(queryset=Department.objects.all(), empty_label='')

    class Meta:
        model = Correspondence
        fields = ('outcoming_mail_number', 'outcoming_mail_receiver', 'department', 'category', 'header', 'date')