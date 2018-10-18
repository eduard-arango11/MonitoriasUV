from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from OfertaMonitorias.models import OfertaMonitoria

def verificar_rol(roles_permitidos): 
    def _method_wrapper(method):
        def _arguments_wrapper(request, *args, **kwargs):
            usuario = request.user
            if usuario.rol not in roles_permitidos:
                return render(request, '404.html')
                #messages.error(request, 'Usted no cuenta con ninguno de los roles permitidos para acceder a está página.')
                #return redirect(reverse_lazy())
                #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

def verificar_operario_propietario_de_oferta():
    def _method_wrapper(method):
        def _arguments_wrapper(request, *args, **kwargs):
            operario = request.user
            oferta = get_object_or_404(OfertaMonitoria, pk=kwargs.get('pk'))
            print(oferta.id)
            if oferta.operario_registra.id != operario.id:
                return render(request, '404.html')
            return method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper