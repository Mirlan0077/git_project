from django.shortcuts import redirect, get_object_or_404, render
from .models import Pet
from .forms import InteractionForm, NameForm


def welcome(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pet = Pet.objects.create(name=name)
            return redirect('pet_info')
    else:
        form = NameForm()

    return render(request, 'welcome.html', {'form': form})


def pet_info(request):
    pet = get_object_or_404(Pet, pk=1)
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            if action == 'feed':
                pet.feed()
            elif action == 'play':
                pet.play()
            elif action == 'rest':
                pet.rest()
            return redirect('pet_info')
    else:
        form = InteractionForm()

    return render(request, 'pet_info.html', {'pet': pet, 'form': form})


def pet_info_redirect(request):
    return redirect('pet_info')
