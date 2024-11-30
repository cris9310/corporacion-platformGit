from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import (TemplateView,
                                  FormView, CreateView, DeleteView, UpdateView,
                                  DetailView, ListView, View)
from django.urls import reverse_lazy
from django.db.models.functions import Coalesce
from django.db.models import Count
from django.contrib import messages


from applications.Programs.models import *
from .forms import *
from .models import *
from applications.User.mixins import *






# Vista ok, se encarga de listar docentes, filtra activos, inactivos y todos.
class Teacherlistview(ListView):
    model = Docente
    template_name = 'docentes/list_teacher.html'
    context_object_name = 'teacher'

    def get_queryset(self):
        data_teacher = []
        data_prin = Docente.objects.all()
        for i in data_prin:
            if Materias.objects.filter(docente__slug=i.slug).exists():
                data_json = {"pk": i.id, 'slug':i.slug, "codigo": i.codigo, "nombres": i.nombres,
                                "apellidos": i.apellidos, "estado": True, "is_active": i.is_active}
                data_teacher.append(data_json)
            else:
                data_json = {"pk": i.id, 'slug':i.slug, "codigo": i.codigo, "nombres": i.nombres,
                                "apellidos": i.apellidos, "estado": False, "is_active": i.is_active}
                data_teacher.append(data_json)
        queryset = data_teacher
        return queryset


# Vista que sirve crear docentes, se encuentra ok
class TeacherCreateView(CreateView):
    model = Docente
    form_class = TeacherForm
    template_name = 'docentes/register_teacher.html'
    success_url = reverse_lazy('teacher_app:teacher-list')

    def post(self, request, *args, **kwargs):

        formulario = TeacherForm(self.request.POST)
        if formulario.is_valid():
            formulario.save()
            # Generador de código para un nuevo docente
            codigo = User.objects.code_generator()
            crea_user = User.objects.create_user(
                tipe=CatalogsTypesRol.objects.get(rol="Docente"),
                codigo=codigo,
                username=formulario.cleaned_data.get('username'),
                email=formulario.cleaned_data.get('email'),
                password=Docente.objects.get_secret("RANDOM"),
                nombres=formulario.cleaned_data.get('nombres'),
                apellidos=formulario.cleaned_data.get('apellidos'),
                is_superuser=False,
                is_active=True,
                is_staff=False,
            )
            mensaje = f'{self.model.__name__} registrado correctamente'
            error = "No hay error!"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response
        else:
            mensaje1 =[]
            mensaje1.append(
                {"error": formulario.errors}
            )
            response = JsonResponse(mensaje1, safe=False)
            response.status_code = 400
            return response
        


# Vista para actualizar la información y el usuario del docente. Se encuentra ok.


class TeacherUpdateView(UpdateView):
    model = Docente
    template_name = 'docentes/update_teacher.html'
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teacher_app:teacher-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        cod_teacher = Docente.objects.get(pk=self.kwargs['pk']).codigo
        teacher_c = self.model.objects.get(codigo=cod_teacher)
        form = TeacherUpdateForm(request.POST, instance=teacher_c)
        if form.is_valid():

            form.save()
            crea_user = User.objects.filter(
                codigo=cod_teacher
            ).update(
                email=form.cleaned_data['email'],
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos'],
                updated_at=datetime.now()
            )
            mensaje = f'{self.model.__name__} actualizado correctamente'
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
        


# Vista ok, muestra el detalle del docente ok
class TeacherDetailView(DetailView):
    template_name = 'docentes/detail_teacher.html'
    model = Docente


# Esta vista se encuentra ok, muestra el detalle de las asignaturas que tiene el docente. ok
class TeacherTopicsListview(ListView):
    model = Docente
    second_model = Materias
    template_name = 'docentes/list_materias_teacher.html'
    context_object_name = 'teacherTp'

    def get_context_data(self, **kwargs):
        cod = self.kwargs['slug']
        context = super(TeacherTopicsListview, self).get_context_data(**kwargs)
        context['topics'] = Docente.objects.filter(slug=cod)
        context['Tmaterias'] = Materias.objects.filter(docente__slug=cod).count()
        return context

    def get_queryset(self):

        cod = self.kwargs['slug']
        data = []
        for i in Materias.objects.filter(docente__slug=cod):
            try:
                info = Banner.objects.values("materia__materia__codigo").annotate(
                    total=Coalesce(Count("materia"), 0)).filter(materia__materia__codigo=i.materia.codigo)
                info1 = {"pk": i.pk, 'slug':i.slug, "codigo": i.materia.codigo, "programa": i.materia.programa,
                            "materia": i.materia, "total": info[0]['total'], "periodo": i.periodo}
                data.append(info1)

            except:
                info1 = {"pk": i.pk, 'slug':i.slug, "codigo": i.materia.codigo, "programa": i.materia.programa,
                            "materia": i.materia, "total": 0, "periodo": i.periodo}
                data.append(info1)
        return data



# Vista que habilita o inhabilita docentes, se enceuntra ok

class TeacherHabilitView(UpdateView):
    model = Docente
    template_name = 'docentes/update_habilitar.html'
    fields = '__all__'
    success_url = reverse_lazy('teacher_app:teacher-list')

    def post(self, request, *args, **kwargs):
        accion = self.request.POST.get('accion')
        if accion == "inhabilitar":
            object1 = User.objects.filter(
                pk=Docente.objects.get(pk=self.kwargs['pk']).codigo
            ).update(is_active=False)

            object2 = Docente.objects.filter(
                pk=self.kwargs['pk']
            ).update(is_active=False)

            messages.success(
                self.request, 'El docente ha sido inhabilitado correctamente')
            return HttpResponseRedirect(self.success_url)

        else:
            object1 = User.objects.filter(
                pk=Docente.objects.get(pk=self.kwargs['pk']).codigo
            ).update(is_active=True)

            object2 = Docente.objects.filter(
                pk=self.kwargs['pk']
            ).update(is_active=True)

            messages.success(
                self.request, 'El docente ha sido habilitado correctamente')
            return HttpResponseRedirect(self.success_url)

#Vista que elimina docentes, ok
class TeacherDeleteView(DeleteView):
    template_name = 'docentes/delete_teacher.html'
    model = Docente
    success_url = reverse_lazy('teacher_app:teacher-list')

    def post(self, request, *args, **kwargs):

        data_delete = self.request.POST
        teacher_delete = Docente.objects.filter(
            codigo=data_delete["codigo"]).delete()
        user_delete = User.objects.filter(
            codigo=data_delete["codigo"]).delete()

        messages.success(
            self.request, 'El docente ha sido eliminado correctamente')
        return HttpResponseRedirect(reverse_lazy('teacher_app:teacher-list'))