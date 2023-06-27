from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')




# def reverse_pgm(request):
#     if request.method=="POST":
#         get_input=request.POST.get('input')
#         print(get_input)
#         output=get_input[::-1]
#         print(output)
#         context={"get_input": get_input,"output":output}

#     return render(request,'about.html')