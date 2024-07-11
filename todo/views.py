from django.shortcuts import render,redirect

# Create your views here.

from .models import Todo
from .forms import TodoForm
from django.contrib import messages 

def index(request):
    item_list=Todo.objects.order_by('-date')
    if request.method=='POST':
            form =TodoForm(request.POST)
            if form.is_valid:
                  form.save()
                  return redirect('todo')
    form=TodoForm()
    page={
          "forms":form,
          "items":item_list,
          "title":"TODO LIST"
          
          
    }        


    return render("todo/index.html",page )

def remove(request, item_id):
      item=Todo.objects.get(id=item_id)
      item.delete()
      messages.info(request, f'{item}, removed successfully')

      return redirect('todo')




