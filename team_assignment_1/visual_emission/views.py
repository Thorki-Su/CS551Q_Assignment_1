from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .models import Country, Data, Feedback
from .forms import SearchForm, UserRegisterForm
from django.contrib import messages
import random
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import json
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)

@login_required(login_url='co2:login')
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

    quotes = [
        '"The greatest threat to our planet is the belief that someone else will save it." -- Robert Swan',
        '"What we do today, right now, will have an accumulated effect on all our tomorrows." -- Alexandra Stoddard',
        '"We will not have a society if we destroy the environment." -- Margaret Mead',
        '"The Earth is what we all have in common." -- Wendell Berry',
        '"There is no planet B." -- Emmanuel Macron',
        '"Act as if what you do makes a difference. It does." -- William James',
        '"Sustainability is no longer about doing less harm. It is about doing more good." -- Jochen Zeitz',
    ]
    random_quote = random.choice(quotes)

    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            input = form.cleaned_data['input']
            country = Country.objects.filter(country_name__iexact=input).first()
            if not country:
                country = Country.objects.filter(country_code__iexact=input).first()
            if country:
                if country.is_country:
                    return redirect('co2:country_detail', country_id=country.id)
                else:
                    return redirect('co2:group_detail', group_id=country.id)
            else:
                messages.warning(request, 'Cannot find the country!')

    context = {
        'countries': countries,
        'groups': groups,
        'eco_tip': random_tip,
        'quote': random_quote,
        'form': form,
    }
    return render(request, 'homepage.html', context=context)

@login_required(login_url='co2:login')
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

@login_required(login_url='co2:login')
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
        return JsonResponse({'error': 'Country Not Found'}, status=404)

@login_required(login_url='co2:login')
def feedback(request):
    countries = Country.objects.filter(is_country=True)
    groups = Country.objects.filter(is_country=False)

    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('feedback')
        Feedback.objects.create(email=email, message=message)
        messages.success(request, "Thank you for your feedback!")
        return redirect('co2:feedback')

    context = {
        'countries': countries,
        'groups': groups,
    }
    return render(request, 'feedback.html', context=context)





@login_required(login_url='co2:login')
def generate_bar_chart(data):
    # Example data for the bar chart
    labels = [item['label'] for item in data]
    values = [item['value'] for item in data]

    # Generate bar chart
    plt.bar(labels, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart Example')

    # Save the chart to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the chart in base64
    bar_chart_base64 = base64.b64encode(image_png).decode('utf-8')
    return bar_chart_base64

@login_required(login_url='co2:login')
def chart_view(request):
    # Fetch or generate your chart data
    chart_data = [{'label': 'A', 'value': 10}, {'label': 'B', 'value': 15}, {'label': 'C', 'value': 7}]

    bar_chart = generate_bar_chart(chart_data)
    existing_chart = generate_existing_chart(chart_data)  # Assuming you have a function for the existing chart

    return render(request, 'your_template.html', {
        'bar_chart': bar_chart,
        'existing_chart': existing_chart
    })




@login_required(login_url='co2:login')
def map(request):
    countries = Country.objects.filter(is_country=True)
    groups = Country.objects.filter(is_country=False)
    country_code_to_id = {country.country_code: country.id for country in countries}
    country_name_to_code = {country.country_name: country.country_code for country in countries}
    context = {
        'countries': countries,
        'groups': groups,
        'country_code_to_id': json.dumps(country_code_to_id),
        'country_name_to_code': json.dumps(country_name_to_code),
    }
    return render(request, 'map.html', context=context)

@login_required(login_url='co2:login')
def export_country_chart_png(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    datas = Data.objects.filter(country=country).order_by('year')
    years = [data.year for data in datas]
    emissions = [data.emission for data in datas]

    fig, ax = plt.subplots()
    ax.plot(years, emissions, marker='o', color='#2a7ae2')
    ax.set_title(f"CO₂ Emissions - {country.country_name}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Emissions (MtCO₂)")
    ax.grid(True)

    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    return HttpResponse(buffer, content_type='image/png')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('co2:homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('co2:homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('co2:login')

@login_required(login_url='co2:login')
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    users = User.objects.all().order_by('date_joined')
    feedbacks = Feedback.objects.all().order_by('-submitted_at')
    return render(request, 'admin_dashboard.html', {
        'users': users,
        'feedbacks': feedbacks
    })

def filtered_chart_view(request):
    filter_category = request.GET.get('category', 'default')
    if filter_category == 'default':
        data = [{'label': 'A', 'value': 10}, {'label': 'B', 'value': 15}, {'label': 'C', 'value': 7}]
    else:
        data = filter_data_by_category(filter_category)  # Replace with your own logic

    bar_chart = generate_bar_chart(data)

    return render(request, 'barchart.html', {
        'bar_chart': bar_chart,
        'filter_category': filter_category
    })


 	
