from django.shortcuts import render,redirect
from .models import Clients_List
from .forms import ClientLeadForm

# Create your views here.
def homepage(request):

    if request.method == 'POST':
        form = ClientLeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ClientLeadForm()

    all_leads = Clients_List.objects.all().order_by('-created_at')

    context = {
        'leads' : all_leads,
        'form' : form
    }

    return render(request, 'clientlists/lists.html',context)