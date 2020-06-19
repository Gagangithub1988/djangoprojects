from django.shortcuts import render
from testApp.forms import AddItemForm
# Create your views here.
def add_item_view(request):
    form=AddItemForm()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(120)
    return render(request,'testApp/additem.html',{'form':form})
def display_item_view(request):
    return render(request,'testApp/displayitems.html')
