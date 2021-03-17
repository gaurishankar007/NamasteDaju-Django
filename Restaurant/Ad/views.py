from django.shortcuts import render, redirect
from django.contrib import messages
import os

from Nd.models import *
from Nd.forms import *

# =========================Admin=========================
def admin(request):
    return render(request, 'Ad/Admin.html')
# =========================Admin=========================

# =========================Menu=========================
def ad_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Food Added Successfully')
            return redirect('/Ad/ad_menu')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Add Food')
            dictionary = {'key': Menu.objects.all(), 'form': form, 'action': "Add"}
            return render(request, 'Ad/AdMenu.html', dictionary)
    dictionary = {'key': Menu.objects.all(), 'form': MenuForm, 'action': "Add"}
    return render(request, 'Ad/AdMenu.html', dictionary)

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
            return redirect('/Ad/ad_menu')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Update Food')
            dictionary = {'key': Menu.objects.all(), 'form': form, 'action': 'Update'}
            return render(request, 'Ad/AdMenu.html', dictionary)
    dictionary = {'key': Menu.objects.all(), 'form': MenuForm(instance=food), 'action': 'Update'}
    return render(request, 'Ad/AdMenu.html', dictionary)


def ad_menu_delete(request, food_id):
    food = Menu.objects.get(id=food_id)
    os.remove(food.image.path)
    food.delete()
    return redirect("/Ad/ad_menu")
# =========================Menu=========================

# =========================Gallery=========================
def ad_gallery(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Picture Added Successfully')
            return redirect('/Ad/ad_gallery')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Add Picture')
            dictionary = {'key': Gallery.objects.all(), 'form': form, 'action': 'Update'}
            return render(request, 'Ad/AdGallery.html', dictionary)
    dictionary = {'key': Gallery.objects.all(), 'form': GalleryForm, 'action': 'Add'}
    return render(request, 'Ad/AdGallery.html', dictionary)

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
            return redirect('/Ad/ad_gallery')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Update Picture')
            dictionary = {'key': Gallery.objects.all(), 'form': form, 'action': 'Update'}
            return render(request, 'Ad/AdGallery.html', dictionary)
    dictionary = {'key': Gallery.objects.all(), 'form': GalleryForm(instance=picture), 'action': 'Update'}
    return render(request, 'Ad/AdGallery.html', dictionary)


def ad_gallery_delete(request, picture_id):
    picture = Gallery.objects.get(id=picture_id)
    os.remove(picture.image.path)
    picture.delete()
    return redirect("/Ad/ad_gallery")
# =========================Gallery=========================

# =========================Stories=========================
def ad_stories(request):    
    if request.method == "POST":
        form = StoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Story Added Successfully')
            return redirect('/Ad/ad_stories')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Add Story')
            dictionary = {'key': Stories.objects.all(), 'form': form, 'action': 'Update'}
            return render(request, 'Ad/AdStories.html', dictionary)
    dictionary = {'key':Stories.objects.all(), 'form':StoriesForm, 'action':'Add'}
    return render(request, 'Ad/AdStories.html', dictionary)

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
            return redirect('/Ad/ad_stories')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Update Story')
            dictionary = {'key': Stories.objects.all(), 'form': form, 'action': 'Update'}
            return render(request, 'Ad/AdStories.html', dictionary)
    dictionary = {'key': Stories.objects.all(), 'form': StoriesForm(instance=story), 'action': 'Update'}
    return render(request, 'Ad/AdStories.html', dictionary)


def ad_stories_delete(request, story_id):
    story = Stories.objects.get(id=story_id)
    os.remove(story.image.path)
    story.delete()
    return redirect("/Ad/ad_stories")
# =========================Stories=========================


def ad_order(request):
    dictionary = {'order': 'selected'}
    return render(request, 'Ad/AdOrder.html', dictionary)

# =========================Reservation=========================
def ad_reservation(request):
    dictionary = {'key': Reservation.objects.all()}
    return render(request, 'Ad/AdReservation.html', dictionary)

def ad_reservation_complete(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    reservation.completion = True
    reservation.save()
    dictionary = {'key': Reservation.objects.all()}
    return render(request, 'Ad/AdReservation.html', dictionary)

def ad_reservation_delete(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    reservation.delete()
    dictionary = {'key': Reservation.objects.all()}
    return render(request, 'Ad/AdReservation.html', dictionary)
# =========================Reservation=========================

# =========================Catering=========================
def ad_catering(request):
    dictionary = {'key':Catering.objects.all()}
    return render(request, 'Ad/AdCatering.html', dictionary)

def ad_catering_complete(request, catering_id):
    catering = Catering.objects.get(id=catering_id)
    catering.completion = True
    catering.save()
    dictionary = {'key':Catering.objects.all()}
    return render(request, 'Ad/AdCatering.html', dictionary)

def ad_catering_delete(request, catering_id):
    catering = Catering.objects.get(id=catering_id)
    catering.delete()
    dictionary = {'key':Catering.objects.all()}
    return render(request, 'Ad/AdCatering.html', dictionary)
# =========================Catering=========================

def message(request):
    dictionary = {'message': 'selected'}
    return render(request, 'Ad/Message.html', dictionary)


def user(request):
    dictionary = {'user': 'selected'}
    return render(request, 'Ad/User.html', dictionary)
# =========================Back End=========================
