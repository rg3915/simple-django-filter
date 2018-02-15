from django import forms
from django.contrib.auth.models import User, Group
import django_filters


class UserFilter(django_filters.FilterSet):
    groups = django_filters.ModelMultipleChoiceFilter(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = {
            'username': ['exact', ],
            'first_name': ['icontains', ],
            'last_name': ['exact', ],
            'date_joined': ['year', 'year__gt', 'year__lt', ],
            'groups': ['exact', ]
        }
