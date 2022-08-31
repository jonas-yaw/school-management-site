from django.shortcuts import render
from students.models import Student
from .forms import ReceiptsForm
from .models import Receipts ,FeesCatalogue

def receipts_list_and_create(request):
    form = ReceiptsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)

        querySet = Student.objects.filter(id=instance.student_id,first_name=instance.first_name,last_name=instance.last_name)
        
        if querySet is not None:        
            def get_balance():
                return Receipts.objects.filter(id=instance.student_id,
                student_class=instance.student_class ,
                academic_year=instance.academic_year,
                term =instance.term)[:1]
            
            def get_default_balance():
                return FeesCatalogue.objects.filter(student_class=instance.student_class ,
                academic_year=instance.academic_year,
                term =instance.term)[:1]
    
            balance_result_1 = get_balance()
            previous_balance = balance_result_1['Balance']

            balance_result_2 = get_default_balance()
            default_balance = balance_result_2['Balance']

            if previous_balance is None:
                previous_balance = default_balance


            instance.balance = previous_balance - instance.amount_paid 
            instance.save()

    


    # notice this comes after saving the form to pick up new objects
    objects = Receipts.objects.all()
    return render(request, 'receipt_list.html', {'objects': objects, 'form': form})

