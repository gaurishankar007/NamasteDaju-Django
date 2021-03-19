import django_filters
from django_filters import CharFilter
from Nd.models import *
from Ac.models import Profile
from django.contrib.auth.models import User


class MenuFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")
    price = CharFilter(field_name="price", lookup_expr="icontains")

    class Meta:
        model = Menu
        fields = ""

class GalleryFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Gallery
        fields = ""


class StoriesFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Stories
        fields = ""

class UserFilter(django_filters.FilterSet):
    username = CharFilter(field_name="username", lookup_expr="icontains")
    email= CharFilter(field_name="email", lookup_expr="icontains")

    class Meta:
        model = Profile
        fields = ""