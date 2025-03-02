


from .models import *
from .forms import *
from .mixins import *
from applications.Teacher.models import *
from applications.Student.models import *


from django.views.generic import (CreateView, DeleteView, UpdateView,
                                  DetailView, ListView)
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.views import PasswordChangeView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

# Vista que crea usuarios, se encuentra ok
class UserCreateView(AdminRequiredMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'usuarios/register_user.html'
    success_url = reverse_lazy('user_app:create-user')
    
    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context["precodigo"] = User.objects.code_generator() 
        return context
    

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(self.request.POST)
        
        if form.is_valid():
            crea_user = User.objects.create_user(
                tipe=form.cleaned_data.get('tipe'),
                codigo = form.cleaned_data.get('codigo'),
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password1'),
                nombres=form.cleaned_data.get('nombres'),
                apellidos=form.cleaned_data.get('apellidos'),
                is_superuser=False,
                is_active=True,
                is_staff=False,

            )
            mensaje = f'{self.model.__name__} creado correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response
        else:
            mensaje1 =[]
            mensaje1.append(
                {"error": form.errors}
            )
            response = JsonResponse(mensaje1, safe=False)
            response.status_code = 400
            return response


# Muestra listado de usuarios creados, se encuentra ok
@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class UserListView(AdminRequiredMixin, ListView):
    model = User
    template_name = 'usuarios/list_users.html'
    context_object_name = 'users'

    def get_queryset(self):
        order = self.request.GET.get('order', '')
        if order:
            queryset = User.objects.filtrar(order).exclude(tipe_id__in=[4,5])
            return queryset

        else:
            queryset = User.objects.all().exclude(tipe_id__in=[4,5])
            return queryset

# Muestra el detalle de los usuarios creados, se encuentra ok
class UserDetailView(AdminRequiredMixin, DetailView):
    model = User
    template_name = 'usuarios/detail_users.html'

# Vista que actualiza los usuarios creados, se encuentra ok
class UserUpdateView(AdminRequiredMixin, UpdateView):
    template_name = 'usuarios/update_user.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('user_app:list-user')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        cod_user = User.objects.get(pk=self.kwargs['pk']).codigo
        user_c = self.model.objects.get(codigo=cod_user)
        form = UserUpdateForm(request.POST, instance=user_c)
        
        if form.is_valid():
            form.save()
            mensaje = f'{self.model.__name__} Actualizado correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response
        else:
            mensaje1 =[]
            mensaje1.append(
                {"error": form.errors}
            )
            response = JsonResponse(mensaje1, safe=False)
            response.status_code = 400
            return response

# Vista que elimina usuarios, se encuentra ok
class UserDeleteView(AdminRequiredMixin, DeleteView):
    template_name = 'usuarios/delete_user.html'
    model = User
    success_url = reverse_lazy('user_app:list-user')


# Vista que habilita o inhabilita usuarios, se encuentra ok
class UserEnableView(AdminRequiredMixin, UpdateView):
    model = User
    template_name = 'usuarios/update_enable.html'
    fields = '__all__'
    success_url = reverse_lazy('user_app:list-user')

    def post(self, request, *args, **kwargs):
        accion = self.request.POST.get('accion')
        if accion == "inhabilitar":
            object1 = User.objects.filter(
                pk=self.kwargs['pk']
            ).update(is_active=False)
            mensaje = f'{self.model.__name__} Actualizado correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response

        else:
            object1 = User.objects.filter(
                pk=self.kwargs['pk']
            ).update(is_active=True)
            mensaje = f'{self.model.__name__} Actualizado correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class UserProfileDetailView(AdminRequiredMixin, ListView):
    model = User
    template_name = 'usuarios/profile.html'
    context_object_name = 'consulta'

    def get_queryset(self):

        if self.request.user.tipe_id == 4 or self.request.user.tipe_id == 5:
            if self.request.user.tipe_id == 5:
                queryset = Docente.objects.filter(codigo=self.request.user.pk)
                return queryset
            else:
                queryset = Docente.objects.filter(
                    codigo=self.request.user.pk)
                return queryset
        else:
            queryset = User.objects.filter(codigo=self.request.user.pk)
            return queryset



class CambiarPasswordView(PasswordChangeView):
    template_name = 'homepage/LoginView_update.html'
    success_url = reverse_lazy('dashboard_app:dashboard-user')
    form_class = CustomPasswordChangeForm


    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        user.cambiar_contrasena = False
        user.save()
        return response