from django.shortcuts import render
from students.models import Student
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import ReceiptsForm,FeesCatalogueForm
from .models import Receipt,FeesCatalogue
from users.models import CustomUser
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView

#data pagination modules 
from django.core.paginator import Paginator 

def receipts_list_and_create(request):
    form = ReceiptsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)

        querySet = Student.objects.filter(student_id=instance.student_id,first_name=instance.first_name,last_name=instance.last_name)
        
        if querySet is not None:  
            print('Student validated')      
            def get_balance():
                return Receipt.objects.filter(student_id=instance.student_id,
                student_class=instance.student_class ,
                academic_year=instance.academic_year,
                fee_type = instance.fee_type ,
                term =instance.term)[:1]
            
            def get_default_balance():
                return FeesCatalogue.objects.filter(student_class=instance.student_class ,
                academic_year=instance.academic_year,
                term =instance.term,
                fee_type = instance.fee_type
                )
    
            balance_result_1 = get_balance()
            for x in balance_result_1:
                previous_balance = x.balance

            default_balance = 0

            balance_result_2 = get_default_balance()
            for y in balance_result_2:
                default_balance = y.total_fees

            if not balance_result_1:
                instance.balance = default_balance - instance.amount_paid 
            else:
                instance.balance = previous_balance - instance.amount_paid 

            instance.receipient = request.user

            instance.save()


            url = reverse('dashboard')
            return render(request, 'receipt.html', {'objects': instance})
        


    # notice this comes after saving the form to pick up new objects
    objects = Receipt.objects.all()

    p = Paginator(Receipt.objects.all(),10)
    page = request.GET.get('page')
    fees_list = p.get_page(page)

    nums = "a" * fees_list.paginator.num_pages


    return render(request, 'receipt_list.html', {'objects': objects,
    'fees_list':fees_list,
    'nums':nums, 
    'form': form
    })



def fees_catalogue_list_and_create(request):
    form = FeesCatalogueForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    # notice this comes after saving the form to pick up new objects
    p = Paginator(FeesCatalogue.objects.all(),10)
    page = request.GET.get('page')
    fees_catalogue_list = p.get_page(page)

    nums = "a" * fees_catalogue_list.paginator.num_pages

    return render(request, 'fees_catalogue_list.html', {
    'fees_catalogue_list':fees_catalogue_list,
    'nums':nums, 
    'form': form
    })


class FeesCatalogueUpdateView(LoginRequiredMixin,UpdateView):
    model = FeesCatalogue
    template_name = 'fees_catalogue_update.html'
    fields = ['student_class','term','academic_year','total_fees','fee_type']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != CustomUser.objects.get(username="jonas"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class FeesCatalogueDeleteView(LoginRequiredMixin,DeleteView):
    model = FeesCatalogue
    template_name = 'fees_catalogue_delete.html'
    success_url = reverse_lazy('fees_catalogue')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != CustomUser.objects.get(username="jonas"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
