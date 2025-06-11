from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from .models import Event


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    form = ContactForm()
    events = Event.objects.all().order_by('start_date')
    return render(request, "index.html", {'form': form, 'events': events})
