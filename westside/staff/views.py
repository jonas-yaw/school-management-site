from django.shortcuts import render
from .models import Staff 
from users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import StaffCreationForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator 

def staff_list_and_create(request):
    form = StaffCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    # notice this comes after saving the form to pick up new objects
    objects = Staff.objects.all()

    p = Paginator(Staff.objects.all(),10)
    page = request.GET.get('page')
    staff_list = p.get_page(page)

    nums = "a" * staff_list.paginator.num_pages

    return render(request, 'staff_list.html', {'objects': objects,
    'staff_list':staff_list,
    'nums':nums, 
    'form': form
    })


class StaffUpdateView(UpdateView):
    model = Staff
    template_name = 'staff_update.html'
    fields = ['first_name','last_name',
    'role','department','date_of_birth','staff_contact','place_of_residence','ssnit_number']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != CustomUser.objects.get(username="jonas"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'staff_delete.html'
    success_url = reverse_lazy('staff')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != CustomUser.objects.get(username="jonas"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
