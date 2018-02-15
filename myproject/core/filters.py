from django.contrib.auth.models import User
import django_filters


class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    year_joined = django_filters.NumberFilter(
        name='date_joined',
        lookup_expr='year'
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]
