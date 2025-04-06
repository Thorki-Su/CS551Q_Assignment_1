from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import Country, Data
import random

# Create your views here.
def homepage(request):
    countries = Country.objects.filter(is_country=True)
    groups = Country.objects.filter(is_country=False)
    eco_tips = [
        'Swap the car, take a bike, save the planet one ride at a time!',
        'Turn off the light, keep it tight, energy savings feel just right!',
        'Meatless days, green vibes stay, carbon footprints fade away!',
        "Reuse, recycle, don't delay, make the earth smile every day!",
        "Short showers win, less water's in, a cleaner world begins within!",
        "Plant a tree, let it grow, carbon's got nowhere to go!",
        'Unplug the gear, have no fear, energy waste disappears!',
        "Walk the block, skip the clock, eco-friendly's how we rock!",
        'Local food, oh so good, cuts the miles and lifts the mood!',
        "Clothesline dry, wave bye-bye, to the dryer's energy high!",
    ]
    random_tip = random.choice(eco_tips)
    context = {
        'countries': countries,
        'groups': groups,
        'eco_tip':random_tip
    }
    return render(request, 'homepage.html', context=context)

def country_detail_view(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    datas = Data.objects.filter(country=country).order_by('year')
    years = [data.year for data in datas]
    emissions = [data.emission for data in datas]
    countries = Country.objects.filter(is_country=True)
    groups = Country.objects.filter(is_country=False)
    all_countries = Country.objects.all()
    context = {
        'countries': countries,
        'groups': groups,
        'country': country,
        'years': years,
        'emissions': emissions,
        'all_countries': all_countries
    }
    return render(request, 'data.html', context=context)

def group_detail_view(request, group_id):
    group = get_object_or_404(Country, id=group_id)
    datas = Data.objects.filter(country=group).order_by('year')
    years = [data.year for data in datas]
    emissions = [data.emission for data in datas]
    countries = Country.objects.filter(is_country=True)
    groups = Country.objects.filter(is_country=False)
    all_countries = Country.objects.all()
    context = {
        'countries': countries,
        'groups': groups,
        'country': group,
        'years': years,
        'emissions': emissions,
        'all_countries': all_countries
    }
    return render(request, 'data.html', context=context)

def country_emissions_api(request, country_id):
    try:
        country = Country.objects.get(id=country_id)
        datas = Data.objects.filter(country=country).order_by('year')
        years = [data.year for data in datas]
        emissions = [data.emission for data in datas]
        return JsonResponse({'years': years, 'emissions': emissions})
    except Country.DoesNotExist:
        return JsonResponse({'error':'Country Not Found'}, status=404)
