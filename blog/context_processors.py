def auth_check(request):
    if request.user.is_authenticated:
        return {'is_login':True}
    else:
        return {'is_login':False}
