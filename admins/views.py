from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.models import User

from admins.forms import UserAdminRegistrationForm


def index(request):
    context = {
        'title': 'Geekshop - Admin panel',
    }
    return render(request, 'admins/index.html', context)


# Create
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()

    context = {
        'title': 'Geekshop - Create users',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


# Read
def admin_users(request):
    context = {
        'title': 'Geekshop - Users',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


# Update
def admin_users_update(request, id):
    context = {
        'title': 'Geekshop - Updates users',
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


# Delete
def admin_users_delete(request):
    pass
