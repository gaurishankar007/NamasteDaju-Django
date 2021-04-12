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

class OrderFilter(django_filters.FilterSet):
    username = django_filters.ModelChoiceFilter(field_name='username', lookup_expr='exact', queryset=User.objects.all())
    foodname = django_filters.ModelChoiceFilter(field_name='foodname', lookup_expr='exact', queryset=Menu.objects.all())

    class Meta:
        model = Order
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


class ReservationFilter(django_filters.FilterSet):
    firstname = CharFilter(field_name="firstname", lookup_expr="icontains")
    lastname = CharFilter(field_name="lastname", lookup_expr="icontains")
    email = CharFilter(field_name="email", lookup_expr="icontains")

    class Meta:
        model = Reservation
        fields = ""


class CateringFilter(django_filters.FilterSet):
    firstname = CharFilter(field_name="firstname", lookup_expr="icontains")
    lastname = CharFilter(field_name="lastname", lookup_expr="icontains")
    email = CharFilter(field_name="email", lookup_expr="icontains")


    class Meta:
        model = Catering
        fields = ""


class UserFilter(django_filters.FilterSet):
    username = CharFilter(field_name="username", lookup_expr="icontains")
    email= CharFilter(field_name="email", lookup_expr="icontains")

    class Meta:
        model = Profile
        fields = ""

class MessageFilter(django_filters.FilterSet):
    username = django_filters.ModelChoiceFilter(field_name='username', lookup_expr='exact', queryset=User.objects.all())
    subject= CharFilter(field_name="subject", lookup_expr="icontains")

    class Meta:
        model = Message
        fields = ""