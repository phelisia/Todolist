from django.shortcuts import render,redirect,get_object_or_404
# from .models import todo
# from .forms import todoForm


# Create your views here.
def index(request):
    return render (request,'todolist.html')

# def create(request):
#     if request.method ==  'POST':
#         form=todoForm(request.POST,request.FILES)
#         if form.is_valid():
#             todo=form.save(commit=False)
#             todo.save()
#         return redirect('/')
#     else:
#         form=todoForm()
#         return render (request,'form.html')   
               


