from django.shortcuts import render, redirect
from .models import Kitchen, Review
from .forms import ReviewForm  # Если ты создавал форму отдельно

def kitchen_list(request):
    kitchens = Kitchen.objects.all()
    return render(request, 'kitchens/kitchen_list.html', {'kitchens': kitchens})

def catalog(request):
    kitchens = Kitchen.objects.all()
    return render(request, 'kitchens/catalog.html', {'kitchens': kitchens})

def about(request):
    return render(request, 'kitchens/about.html')

def contacts(request):
    return render(request, 'kitchens/contacts.html')

# Новый reviews
def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')  # После отправки обновляем страницу
    else:
        form = ReviewForm()

    reviews_list = Review.objects.all().order_by('-created_at')  # Выводим все отзывы
    return render(request, 'kitchens/reviews.html', {'form': form, 'reviews': reviews_list})
