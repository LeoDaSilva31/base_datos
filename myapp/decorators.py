from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_superuser,
        login_url='account_login'
    )(view_func)
    return decorated_view_func
