from django.shortcuts import render, redirect

from . models import Menu, Gallery, Stories, Reservation, Catering
from . forms import MenuForm, GalleryForm, StoriesForm, ReservationForm, CateringForm

from django.contrib import messages
import os

# =========================Back End=========================
def admin(request):
    return render(request, 'Nd/Admin.html')

# =========================Menu=========================
def ad_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Food Added Successfully')
            return redirect('/Nd/ad_menu')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Add Food')
            return render(request, 'Nd/AdMenu.html', {'form': form})
    dictionary = {'key': Menu.objects.all(), 'form': MenuForm, 'action': "Add"}
    return render(request, 'Nd/AdMenu.html', dictionary)

def ad_menu_update(request, food_id):
    food = Menu.objects.get(id=food_id)
    prev_image = food.image.path
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            new_image = food.image.path
            if prev_image != new_image:
                os.remove(prev_image)
            messages.add_message(request, messages.SUCCESS, 'Food Updated Successfully')
            return redirect('/Nd/ad_menu')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Update Food')
            dictionary = {'key': Menu.objects.all(), 'form': form, 'action': 'Update'}
            return render(request, 'Nd/AdMenu.html', dictionary)
    dictionary = {'key': Menu.objects.all(), 'form': MenuForm(instance=food), 'action': 'Update'}
    return render(request, 'Nd/AdMenu.html', dictionary)


def ad_menu_delete(request, food_id):
    food = Menu.objects.get(id=food_id)
    os.remove(food.image.path)
    food.delete()
    return redirect("/Nd/ad_menu")
# =========================Menu=========================

# =========================Gallery=========================
def ad_gallery(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Picture Added Successfully')
            return redirect('/Nd/ad_gallery')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Add Picture')
            return render(request, 'Nd/AdGallery.html', {'form': form})
    dictionary = {'key': Gallery.objects.all(), 'form': GalleryForm, 'action': 'Add'}
    return render(request, 'Nd/AdGallery.html', dictionary)

def ad_gallery_update(request, picture_id):
    picture = Gallery.objects.get(id=picture_id)
    prev_image = picture.image.path
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES, instance=picture)
        if form.is_valid():
            form.save()
            new_image = picture.image.path
            if prev_image != new_image:
                os.remove(prev_image)
            messages.add_message(request, messages.SUCCESS, 'Picture Updated Successfully')
            return redirect('/Nd/ad_gallery')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Update Picture')
            dictionary = {'key': Gallery.objects.all(), 'form': form, 'action': 'Update'}
            return render(request, 'Nd/AdGallery.html', dictionary)
    dictionary = {'key': Gallery.objects.all(), 'form': GalleryForm(instance=picture), 'action': 'Update'}
    return render(request, 'Nd/AdGallery.html', dictionary)


def ad_gallery_delete(request, picture_id):
    picture = Gallery.objects.get(id=picture_id)
    os.remove(picture.image.path)
    picture.delete()
    return redirect("/Nd/ad_gallery")
# =========================Gallery=========================

# =========================Stories=========================
def ad_stories(request):    
    if request.method == "POST":
        form = StoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Story Added Successfully')
            return redirect('/Nd/ad_stories')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Add Story')
            return render(request, 'Nd/AdStories.html', {'form': form})
    dictionary = {'key':Stories.objects.all(), 'form':StoriesForm, 'action':'Add'}
    return render(request, 'Nd/AdStories.html', dictionary)

def ad_stories_update(request, story_id):
    story = Stories.objects.get(id=story_id)
    prev_image = story.image.path
    if request.method == "POST":
        form = StoriesForm(request.POST, request.FILES, instance=story)
        if form.is_valid():
            form.save()
            new_image = story.image.path
            if prev_image != new_image:
                os.remove(prev_image)
            messages.add_message(request, messages.SUCCESS, 'Story Updated Successfully')
            return redirect('/Nd/ad_stories')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Update Story')
            dictionary = {'key': Stories.objects.all(), 'form': form, 'action': 'Update'}
            return render(request, 'Nd/AdStories.html', dictionary)
    dictionary = {'key': Stories.objects.all(), 'form': StoriesForm(instance=story), 'action': 'Update'}
    return render(request, 'Nd/AdStories.html', dictionary)


def ad_stories_delete(request, story_id):
    story = Stories.objects.get(id=story_id)
    os.remove(story.image.path)
    story.delete()
    return redirect("/Nd/ad_stories")
# =========================Stories=========================


def ad_order(request):
    dictionary = {'order': 'selected'}
    return render(request, 'Nd/AdOrder.html', dictionary)


def ad_reservation(request):
    dictionary = {'reservation': 'selected'}
    return render(request, 'Nd/AdReservation.html', dictionary)


def ad_catering(request):
    dictionary = {'catering': 'selected'}
    return render(request, 'Nd/AdCatering.html', dictionary)


def message(request):
    dictionary = {'message': 'selected'}
    return render(request, 'Nd/Message.html', dictionary)


def user(request):
    dictionary = {'user': 'selected'}
    return render(request, 'Nd/User.html', dictionary)
# =========================Back End=========================


# =========================Front End=========================
def home(request):
    dictionary = {'home': 'selected'}
    return render(request, 'Nd/Home.html', dictionary)


def menu(request):
    dictionary = {'key': Menu.objects.all(), 'menu': 'selected'}
    return render(request, 'Nd/Menu.html', dictionary)


def gallery(request):
    dictionary = {'key': Gallery.objects.all(), 'gallery': 'selected'}
    return render(request, 'Nd/Gallery.html', dictionary)


def stories(request):
    dictionary = {'key': Stories.objects.all(), 'stories': 'selected'}
    return render(request, 'Nd/Stories.html', dictionary)


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You have booked table successfully')
            return redirect('/Nd/reservation')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to book table')
            return render(request, 'Nd/Reservation.html', {'form': form})
    dictionary = {'form':ReservationForm, 'reservation': 'selected'}
    return render(request, 'Nd/Reservation.html', dictionary)


def catering(request):
    if request.method == 'POST':
        form = CateringForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You have ordered catering successfully')
            return redirect('/Nd/reservation')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to order catering')
            return render(request, 'Nd/Reservation.html', {'form': form})
    dictionary = {'form':CateringForm ,'catering': 'selected'}
    return render(request, 'Nd/Catering.html', dictionary)


def contact(request):
    dictionary = {'contact': 'selected'}
    return render(request, 'Nd/Contact.html', dictionary)
# =========================Front End=========================
