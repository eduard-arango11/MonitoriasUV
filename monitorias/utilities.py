from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

def verificar_rol(roles_permitidos): 
    def _method_wrapper(method):
        def _arguments_wrapper(request, *args, **kwargs):
            usuario = request.user
            if usuario.rol not in roles_permitidos:
                messages.error(request, 'Usted no cuenta con ninguno de los roles permitidos para acceder a está página.')
                #return redirect(reverse_lazy())
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper