from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


def login_redirect(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'role') and request.user.role == 'admin':
            return redirect('/admin/')
        return redirect('base_page')
    return redirect('account_login')


@login_required
def base_page(request):
    return render(request, 'base_page.html')
