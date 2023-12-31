import django_filters
from django_filters import CharFilter
from .models import Menu, Stories


class MenuFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")
    price = CharFilter(field_name="price", lookup_expr="icontains")

    class Meta:
        model = Menu
        fields = ""


class StoriesFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Stories
        fields = ""