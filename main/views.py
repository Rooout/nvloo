from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'apk' : 'nvloo',
        'name': 'Farrel',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)