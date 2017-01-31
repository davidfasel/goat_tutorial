from django.shortcuts import render
#from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        #item.text = request.POST.get('item_text', '')
        #item.save()
        #easier way without having to save()
        Item.objects.create(text = new_item_text)
    else:
        new_item_text = ''

    return render(request, 'home.html', {
        'new_item_text': new_item_text, 
    })
    

