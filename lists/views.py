from django.shortcuts import render, redirect
#from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
#       new_item_text = request.POST['item_text']
#       item.text = request.POST.get('item_text', '')
#       item.save()
#       easier way without having to save()
        Item.objects.create(text = request.POST['item_text'])
        return redirect('/')



    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
    

