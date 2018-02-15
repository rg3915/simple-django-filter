from django.contrib.auth.models import User
from django.shortcuts import render
from django_filters.views import FilterView
from .filters import UserFilter


def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'core/user_list.html', {'filter': user_filter})


search_cbv = FilterView.as_view(
    filterset_class=UserFilter,
    template_name='core/user_list.html',
)
