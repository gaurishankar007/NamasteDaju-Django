from django.shortcuts import render, redirect
from django.contrib import messages
import os

from Nd.models import *
from Nd.forms import *
from .filters import *

from Ac.auth import *
from Ac.models import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# =========================Admin=========================
@login_required
@admin_only
def admin(request):
    menu=Menu.objects.all()
    menu_count = menu.count()

    order=Order.objects.all()
    order_count = order.count()

    gallery=Gallery.objects.all()
    gallery_count = gallery.count()

    stories=Stories.objects.all()
    stories_count = stories.count()

    reservation=Reservation.objects.all()
    reservation_count = reservation.count()

    catering=Catering.objects.all()
    catering_count = catering.count()

    message=Message.objects.all()
    message_count = message.count()

    users=User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()

    dictionary={
        "menu":menu_count, 
        "order":order_count,
        "gallery":gallery_count, 
        "stories":stories_count, 
        "reservation":reservation_count,
        "catering":catering_count,
        "message":message_count,
        "user":user_count,
        "admin":admin_count
        }
    return render(request, 'Ad/Admin.html', dictionary)
# =========================Admin=========================


# =========================Register=========================
@login_required
@admin_only
def ad_register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username)
            messages.add_message(request, messages.SUCCESS, 'New User have been registered Successfully')
            return redirect('/Ad/ad_register')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to Register New User')
            return render(request, 'Ad/AdRegister.html', {'form': form})
    dictionary = {'form': UserCreationForm}
    return render(request, 'Ad/AdRegister.html', dictionary)
# =========================Register=========================


# =========================Menu=========================
@login_required
@admin_only
def ad_menu(request):
    menu = Menu.objects.all()
    menu_filter = MenuFilter(request.GET, queryset=menu)
    menu_final = menu_filter.qs

    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Food Added Successfully')
            return redirect('/Ad/ad_menu')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Add Food')
            dictionary = {'key': menu_final, 'menu_filter':menu_filter, 'form': form, 'action': "Add"}
            return render(request, 'Ad/AdMenu.html', dictionary)
    dictionary = {'key': menu_final, 'menu_filter':menu_filter, 'form': MenuForm, 'action': "Add"}
    return render(request, 'Ad/AdMenu.html', dictionary)


@login_required
@admin_only
def ad_menu_update(request, food_id):
    menu = Menu.objects.all()
    menu_filter = MenuFilter(request.GET, queryset=menu)
    menu_final = menu_filter.qs

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
            dictionary = {'key': menu_final, 'menu_filter':menu_filter, 'form': form, 'action': 'Update'}
            return render(request, 'Ad/AdMenu.html', dictionary)
    dictionary = {'key': menu_final, 'menu_filter':menu_filter, 'form': MenuForm(instance=food), 'action': 'Update'}
    return render(request, 'Ad/AdMenu.html', dictionary)


@login_required
@admin_only
def ad_menu_delete(request, food_id):
    food = Menu.objects.get(id=food_id)
    os.remove(food.image.path)
    food.delete()
    return redirect("/Ad/ad_menu")
# =========================Menu=========================

# =========================Gallery=========================
@login_required
@admin_only
def ad_gallery(request):
    gallery = Gallery.objects.all()
    gallery_filter = GalleryFilter(request.GET, queryset=gallery)
    gallery_final = gallery_filter.qs

    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Picture Added Successfully')
            return redirect('/Ad/ad_gallery')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Add Picture')
            dictionary = {'key': gallery_final, 'gallery_filter':gallery_filter, 'form': form, 'action': 'Update'}
            return render(request, 'Ad/AdGallery.html', dictionary)
    dictionary = {'key': gallery_final, 'gallery_filter':gallery_filter, 'form': GalleryForm, 'action': 'Add'}
    return render(request, 'Ad/AdGallery.html', dictionary)


@login_required
@admin_only
def ad_gallery_update(request, picture_id):
    gallery = Gallery.objects.all()
    gallery_filter = GalleryFilter(request.GET, queryset=gallery)
    gallery_final = gallery_filter.qs

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
            dictionary = {'key': gallery_final, 'gallery_filter':gallery_filter, 'form': form, 'action': 'Update'}
            return render(request, 'Ad/AdGallery.html', dictionary)
    dictionary = {'key': gallery_final, 'gallery_filter':gallery_filter, 'form': GalleryForm(instance=picture), 'action': 'Update'}
    return render(request, 'Ad/AdGallery.html', dictionary)


@login_required
@admin_only
def ad_gallery_delete(request, picture_id):
    picture = Gallery.objects.get(id=picture_id)
    os.remove(picture.image.path)
    picture.delete()
    return redirect("/Ad/ad_gallery")
# =========================Gallery=========================

# =========================Stories=========================
@login_required
@admin_only
def ad_stories(request):   
    stories = Stories.objects.all()
    stories_filter = StoriesFilter(request.GET, queryset=stories)
    stories_final = stories_filter.qs 

    if request.method == "POST":
        form = StoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Story Added Successfully')
            return redirect('/Ad/ad_stories')
        else: 
            messages.add_message(request, messages.ERROR, 'Failed to Add Story')
            dictionary = {'key': stories_final, 'stories_filter':stories_filter, 'form': form, 'action': 'Update'}
            return render(request, 'Ad/AdStories.html', dictionary)
    dictionary = {'key': stories_final, 'stories_filter':stories_filter, 'form':StoriesForm, 'action':'Add'}
    return render(request, 'Ad/AdStories.html', dictionary)
    

@login_required
@admin_only    
def ad_stories_update(request, story_id):
    stories = Stories.objects.all()
    stories_filter = StoriesFilter(request.GET, queryset=stories)
    stories_final = stories_filter.qs 

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
            dictionary = {'key': stories_final, 'stories_filter':stories_filter, 'form': form, 'action': 'Update'}
            return render(request, 'Ad/AdStories.html', dictionary)
    dictionary = {'key': stories_final, 'stories_filter':stories_filter, 'form': StoriesForm(instance=story), 'action': 'Update'}
    return render(request, 'Ad/AdStories.html', dictionary)


@login_required
@admin_only
def ad_stories_delete(request, story_id):
    story = Stories.objects.get(id=story_id)
    os.remove(story.image.path)
    story.delete()
    return redirect("/Ad/ad_stories")
# =========================Stories=========================

# =========================Order=========================
@login_required
@admin_only
def ad_order(request):
    order = Order.objects.all()
    order_filter = OrderFilter(request.GET, queryset=order)
    order_final = order_filter.qs 
    dictionary = {'key': order_final, 'order_filter':order_filter}
    return render(request, 'Ad/AdOrder.html', dictionary)

@login_required
@admin_only
def ad_order_complete(request, order_id):
    order = Order.objects.all()
    order_filter = OrderFilter(request.GET, queryset=order)
    order_final = order_filter.qs 

    order1 = Order.objects.get(id=order_id)
    order1.completion = True
    order1.save()    
    dictionary = {'key': order_final, 'order_filter':order_filter}
    return render(request, 'Ad/AdOrder.html', dictionary)


@login_required
@admin_only
def ad_order_delete(request, order_id):
    order = Order.objects.all()
    order_filter = OrderFilter(request.GET, queryset=order)
    order_final = order_filter.qs 

    order1 = Order.objects.get(id=order_id)
    order1.delete()   
    dictionary = {'key': order_final, 'order_filter':order_filter}
    return render(request, 'Ad/AdOrder.html', dictionary)
# =========================Order=========================

# =========================Reservation=========================

@login_required
@admin_only
def ad_reservation(request):
    reservation = Reservation.objects.all()
    reservation_filter = ReservationFilter(request.GET, queryset=reservation)
    reservation_final = reservation_filter.qs
    dictionary = {'key': reservation_final, 'reservation_filter': reservation_filter}
    return render(request, 'Ad/AdReservation.html', dictionary)


@login_required
@admin_only
def ad_reservation_complete(request, reservation_id):
    reservation = Reservation.objects.all()
    reservation_filter = ReservationFilter(request.GET, queryset=reservation)
    reservation_final = reservation_filter.qs

    reservation1 = Reservation.objects.get(id=reservation_id)
    reservation1.completion = True
    reservation1.save()    
    dictionary = {'key': reservation_final, 'reservation_filter': reservation_filter}
    return render(request, 'Ad/AdReservation.html', dictionary)


@login_required
@admin_only
def ad_reservation_delete(request, reservation_id):
    reservation = Reservation.objects.all()
    reservation_filter = ReservationFilter(request.GET, queryset=reservation)
    reservation_final = reservation_filter.qs

    reservation1 = Reservation.objects.get(id=reservation_id)
    reservation1.delete()
    dictionary = {'key': reservation_final, 'reservation_filter': reservation_filter}
    return render(request, 'Ad/AdReservation.html', dictionary)
# =========================Reservation=========================

# =========================Catering=========================
@login_required
@admin_only
def ad_catering(request): 
    catering = Catering.objects.all()
    catering_filter = CateringFilter(request.GET, queryset=catering)
    catering_final = catering_filter.qs
    dictionary = {'key': catering_final, 'catering_filter': catering_filter}
    return render(request, 'Ad/AdCatering.html', dictionary)


@login_required
@admin_only
def ad_catering_complete(request, catering_id):
    catering = Catering.objects.all()
    catering_filter = CateringFilter(request.GET, queryset=catering)
    catering_final = catering_filter.qs

    catering1 = Catering.objects.get(id=catering_id)
    catering1.completion = True
    catering1.save()
    dictionary = {'key': catering_final, 'catering_filter': catering_filter}
    return render(request, 'Ad/AdCatering.html', dictionary)


@login_required
@admin_only
def ad_catering_delete(request, catering_id):
    catering = Catering.objects.all()
    catering_filter = CateringFilter(request.GET, queryset=catering)
    catering_final = catering_filter.qs

    catering = Catering.objects.get(id=catering_id)
    catering.delete()
    dictionary = {'key': catering_final, 'catering_filter': catering_filter}
    return render(request, 'Ad/AdCatering.html', dictionary)
# =========================Catering=========================

# =========================Message=========================
@login_required
@admin_only
def message(request):
    message = Message.objects.all()
    message_filter = MessageFilter(request.GET, queryset=message)
    message_final = message_filter.qs

    dictionary = {'key': message_final, 'message_filter': message_filter}
    return render(request, 'Ad/Message.html', dictionary)


@login_required
@admin_only
def message_delete(request, message_id):
    message = Message.objects.all()
    message_filter = MessageFilter(request.GET, queryset=message)
    message_final = message_filter.qs

    message1 = Message.objects.get(id=message_id)
    message1.delete()

    dictionary = {'key': message_final, 'message_filter': message_filter}
    return render(request, 'Ad/Message.html', dictionary)
# =========================Message=========================

# =========================User=========================
@login_required
@admin_only
def user(request):
    users = Profile.objects.all()
    user_filter = UserFilter(request.GET, queryset=users)
    user_final = user_filter.qs

    dictionary = {'key': user_final, 'user_filter': user_filter}
    return render(request, 'Ad/User.html', dictionary)

@login_required
@admin_only
def update_user(request, user_id):
    userprofile = Profile.objects.get(id=user_id)
    userprofile.staff = True
    userprofile.save()

    user = User.objects.get(username=userprofile.username)
    user.is_staff = True
    user.save()
    
    messages.add_message(request, messages.SUCCESS, 'User has been updated to Admin')
    return redirect('/Ad/user')
# =========================User=========================
