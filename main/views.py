from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306256450',
        'name': 'Muhammad Raditya Indrastata Norman',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)
