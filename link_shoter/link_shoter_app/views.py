from django.shortcuts import render, redirect
from random import choice
from string import ascii_uppercase
from .forms import LinkForm
from .models import Link


def gen_link():
    glink  = ''.join(choice(ascii_uppercase) for i in range(12))
    return glink

def input_link(request):
    form = LinkForm()
    shot_link = Link.objects.all()
    if request.method == 'POST':
        in_link = LinkForm(request.POST)
        if in_link.is_valid():
            link = in_link.cleaned_data.get('input_link')
            true_link = gen_link()
            if Link.objects.filter(output_link = true_link) != []:
                true_link = gen_link()

            li = Link(input_link = link, output_link = true_link)
            li.save()
            return render(request, 'link_shorter.html', {'form': form, })
        else:
            return render(request, 'link_shorter.html', {'error': 'Data is not valid'})
    else:
        return render(request, 'link_shorter.html', {'form': form,'links':shot_link})

def relink(request, data):

    obj = Link.objects.get(output_link = data)
    link = obj.input_link


    return redirect(link)

