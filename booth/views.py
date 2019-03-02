from django.shortcuts import render
from .models import Image, Category, Location


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def gallery(request):
    images = Image.objects.all()
    return render(request, 'categories/all-images.html', {"images" : images})


def search_results(request):
    all_categories = Category.objects.all()
    if 'category' in request.GET and request.GET["category"]:
        parameter = request.GET.get("category")
        img = Image.search_image(parameter)
        message = f"{parameter}"
        return render(request, 'categories/search.html',{"message":message,"category": img, "all_categories":all_categories})

    else:
        message = "You haven't searched for any image category"
        return render(request, 'categories/search.html',{"message":message, "all_categories":all_categories})

def locations_filter(request):
    all_locations = Location.objects.all()
    return render(request, 'categories/location.html', {"all_locations": all_locations})



