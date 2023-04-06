from django.shortcuts import render, redirect
from .forms import CreateNewShortURL
from .models import ShortURL
import random, string
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError



def Home(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            validator = URLValidator()
            try:
                validator(original_website)
            except ValidationError:
                form.add_error('original_url', 'Invalid URL')
                context = {'form': form}
                return render(request, 'index.html', context)
            random_chars_list = list(string.ascii_letters)
            random_chars = ''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortURL.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            s = ShortURL(original_url=original_website, short_url=random_chars)
            s.save()
            return redirect(Redirect, url=s.short_url)
    else:
        form = CreateNewShortURL()
    context = {'form': form}
    return render(request, 'index.html', context)


def Redirect(request, url):
    current_obj = ShortURL.objects.filter(short_url=url)
    context = {'obj': current_obj[0], 'url': current_obj[0].short_url}
    return render(request, 'redirect.html', context)