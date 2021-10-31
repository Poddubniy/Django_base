from django.shortcuts import render


def index(request):
    context = {
        'title': 'Geekshop - Admin panel',
    }
    return render(request, 'admins/index.html', context)


# Create
def admin_users_create(request):
    context = {
        'title': 'Geekshop - Create users',
    }
    return render(request, 'admins/admin-users-create.html', context)


# Read
def admin_users(request):
    context = {
        'title': 'Geekshop - Users',
    }
    return render(request, 'admins/admin-users-read.html', context)


# Update
def admin_users_update(request):
    context = {
        'title': 'Geekshop - Updates users',
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


# Delete
def admin_users_delete(request):
    pass
