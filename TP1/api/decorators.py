from django.shortcuts import redirect

def unauthorized_user(view_func):
    def wrapper_func (request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('usuario:Perfil')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func