# CS551Q_Assignment_1


### What is this?
This `README.md` file (version 1.0) shows some problems I met in the process of doing this Assignment. Hope this will help you.

### Get python version 3.10.7
When open your codio link for this Assignment, firstly checking the python version is necessary. Try with this code:
```bash 
    python --version
```
If your python version is 2.7.17, you should download 3.10.7 version. Type the following command:
```bash
    pyenv install 3.10.7
```
If you meet an error like '*python-build: definition not found: 3.10.7*', then you should upload your pyenv. Try this:
```bash
    cd ~/.pyenv
    git pull
```
Then, go back to your working directory:
```bash
    cd -
```
Now you should be able to download the version 3.10.7:
```bash
    pyenv install 3.10.7
```
After downloading, remember to check the version again. If it's still 2.7.17, try this command:
```bash
    pyenv rehash
```

### Download files from github repository
I have created a repository on github for this Assignment, you can download files from it.
Firstly, make sure you've received my invitation and selected consent. Only if you do this will you have the permission to follow up.
Then, you can use this commend to download.
```bash
    git clone https://github.com/Thorki-Su/CS551Q_Assignment_1.git
```
This will download all the files into your codio as a new folder '*CS551Q_Assignment_1*'.
Remember to change your path before do any testings or changes:
```bash
    cd CS551Q_Assignment_1
```


# The process of this Assignment

### Build Basic Django Framework
After making sure your python version is correct, you can use these commands to start the virtual environment and install some modules:
```bash
    pyenv local 3.10.7 # this sets the local version of python to 3.10.7
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip # this installs pip, and upgrades it if required.
```
Then we install django:
```bash
    pip install django
```
The first step of this assignment is to create a project for it. We use '*team_assignment*' as the name of project.
```bash
    django-admin startproject team_assignment
```
It will create a folder named team_assignment. Remember to change path into this project:
```bash
    cd team_assignment
```
Then we create an app named '*visual_emission*', cause our data is about CO2 emissions.
```bash
    python manage.py startapp visual_emission
```
This command will create a new folder inside our project folder.
Open the file *settings.py* and add the app into *INSTALLED_APPS*, remember the ',' at the end.
```python
    'visual_emission',
```
Then open the file *urls.py* and change it like this:
```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('co2/', include('visual_emission.urls', namespace='co2')),
    ]
```
*include* makes sure it can use urls in app folder, and all these urls begin with '*co2/*'.
Next create a new file named *urls.py* in the *visual_emission* folder, it should look like this:
```python
    from django.urls import path
    from . import views

    app_name = 'co2'

    urlpatterns = [
        path('', views.homepage, name='homepage'),
    ]
```
This ensures that when the '/co2' path is accessed, the server calls the homepage function in views.
Then we write the homepage function. Open the file *views.py* in the *visual_emission* folder, and change it like this:
```python
    from django.shortcuts import render, HttpResponse

    # Create your views here.
    def homepage(request):
        return HttpResponse('This is the home page!')
```
The function will return a string '*This is the home page!*'.
In Terminal, use this command to run the server firstly:
```bash
    python manage.py runserver
```
After the server is running, use 'Box URL' to open a website. Change the '3000' to '8000' and copy the url after 'https://'. Everyone's url is different. For example, mine is '*randomevent-spenddemand-8000.codio-box.uk*'
In '*settings.py*', paste your url into '*ALLOWED_HOSTS*', just like this:(remember use your own url)
```python
    ALLOWED_HOSTS = ['randomevent-spenddemand-8000.codio-box.uk']
```
Then stop the server by CTRl+C, save all the files and run the server again. This time we use this command:
```bash
    python3 manage.py runserver 0.0.0.0:8000
```
Again, open a website by 'Box URL', change the url from 3000 to 8000 and add '/co2' at the end.
If everything is correct, you can see '*This is the home page!*' in the new page.

### Create Models for Database
Open the file '*models.py*', we will create two models in it:
```python
    class Country(models.Model):
        country_name = models.CharField(max_length=100, unique=True)
        country_code = models.CharField(max_length=10, unique=True)
        region = models.CharField(max_length=100, null=True)
        income_group = models.CharField(max_length=50, null=True)
        is_country = models.BooleanField(default=True)

    class Data(models.Model):
        country = models.ForeignKey(Country, on_delete=models.CASCADE)
        year = models.IntegerField()
        emission = models.FloatField()

        class Meta:
            unique_together = ('country', 'year')
```
Then we ask Django to generate the migration file with the command:
```python
    python3 manage.py makemigrations
```
After that, we run the generated migration with the command:
```python
    python3 manage.py migrate
```
In the future, anytime that you edit the model, you need to run makemigration, and then migrate commands to have the database changes happen.

### Load Data from the Excel File
Under the 'visual_emission' app create a folder 'management' and inside that create another one named 'commands'. Then create a file parse_cities.py in that folder. We use the openpyxl library to parse the excel spreadsheet, so you need to install that with the command:
```bash
    pip install openpyxl
```
In the 'visual_emission' folder, create a folder named 'country_data', then upload the excel file in it. Make sure the file is end with '.xlsx' cause the openpyxl library can only be used to deal with xlsx files.
Open file parse_cities.py, we will write some commands to load data from our excel file:
```python
    import os
    from pathlib import Path
    from django.db import models
    from django.core.management.base import BaseCommand, CommandError
    from openpyxl import load_workbook

    from visual_emission.models import Country, Data # load the models

    class Command(BaseCommand):
        help = 'Load data from csv'

        def handle(self, *args, **options):
            Country.objects.all().delete()
            Data.objects.all().delete()
            print('table dropped')

            base_dir = Path(__file__).resolve().parent.parent.parent.parent
            book_path = os.path.join(base_dir, 'visual_emission/country_data/data_upload.xlsx')
            book = load_workbook(book_path)
            sheet = book['Data']
            print(sheet.title)
            max_row_num = sheet.max_row
            max_col_num = sheet.max_column
            print(max_row_num)
            print(max_col_num)

            # placeholder variables for objects
            c_name = 'country_name'
            c_code = 'code'
            is_c = True
            reg = ''
            income = ''
            year_90 = 0.0
            year_91 = 0.0
            year_92 = 0.0
            year_93 = 0.0
            year_94 = 0.0
            year_95 = 0.0
            year_96 = 0.0
            year_97 = 0.0
            year_98 = 0.0
            year_99 = 0.0
            year_00 = 0.0
            year_01 = 0.0
            year_02 = 0.0
            year_03 = 0.0
            year_04 = 0.0
            year_05 = 0.0
            year_06 = 0.0
            year_07 = 0.0
            year_08 = 0.0
            year_09 = 0.0
            year_10 = 0.0
            year_11 = 0.0
            year_12 = 0.0
            year_13 = 0.0
            year_14 = 0.0
            year_15 = 0.0
            year_16 = 0.0
            year_17 = 0.0
            year_18 = 0.0
            year_19 = 0.0
            year_20 = 0.0

            for i in range(2, max_row_num+1):
                for j in range(1, max_col_num+1):
                    cell_obj = sheet.cell(row=i, column=j)

                    if cell_obj.column_letter == 'A':
                        c_name = cell_obj.value
                    if cell_obj.column_letter == 'B':
                        c_code = cell_obj.value
                    if cell_obj.column_letter == 'C':
                        is_c = cell_obj.value
                    if cell_obj.column_letter == 'D':
                        if cell_obj.value is not None:
                            reg = cell_obj.value
                    if cell_obj.column_letter == 'E':
                        if cell_obj.value is not None:
                            income = cell_obj.value
                    if cell_obj.column_letter == 'F':
                        if cell_obj.value is not None:
                            year_90 = cell_obj.value
                    if cell_obj.column_letter == 'G':
                        if cell_obj.value is not None:
                            year_91 = cell_obj.value
                    if cell_obj.column_letter == 'H':
                        if cell_obj.value is not None:
                            year_92 = cell_obj.value
                    if cell_obj.column_letter == 'I':
                        if cell_obj.value is not None:
                            year_93 = cell_obj.value
                    if cell_obj.column_letter == 'J':
                        if cell_obj.value is not None:
                            year_94 = cell_obj.value
                    if cell_obj.column_letter == 'K':
                        if cell_obj.value is not None:
                            year_95 = cell_obj.value
                    if cell_obj.column_letter == 'L':
                        if cell_obj.value is not None:
                            year_96 = cell_obj.value
                    if cell_obj.column_letter == 'M':
                        if cell_obj.value is not None:
                            year_97 = cell_obj.value
                    if cell_obj.column_letter == 'N':
                        if cell_obj.value is not None:
                            year_98 = cell_obj.value
                    if cell_obj.column_letter == 'O':
                        if cell_obj.value is not None:
                            year_99 = cell_obj.value
                    if cell_obj.column_letter == 'P':
                        if cell_obj.value is not None:
                            year_00 = cell_obj.value
                    if cell_obj.column_letter == 'Q':
                        if cell_obj.value is not None:
                            year_01 = cell_obj.value
                    if cell_obj.column_letter == 'R':
                        if cell_obj.value is not None:
                            year_02 = cell_obj.value
                    if cell_obj.column_letter == 'S':
                        if cell_obj.value is not None:
                            year_03 = cell_obj.value
                    if cell_obj.column_letter == 'T':
                        if cell_obj.value is not None:
                            year_04 = cell_obj.value
                    if cell_obj.column_letter == 'U':
                        if cell_obj.value is not None:
                            year_05 = cell_obj.value
                    if cell_obj.column_letter == 'V':
                        if cell_obj.value is not None:
                            year_06 = cell_obj.value
                    if cell_obj.column_letter == 'W':
                        if cell_obj.value is not None:
                            year_07 = cell_obj.value
                    if cell_obj.column_letter == 'X':
                        if cell_obj.value is not None:
                            year_08 = cell_obj.value
                    if cell_obj.column_letter == 'Y':
                        if cell_obj.value is not None:
                            year_09 = cell_obj.value
                    if cell_obj.column_letter == 'Z':
                        if cell_obj.value is not None:
                            year_10 = cell_obj.value
                    if cell_obj.column_letter == 'AA':
                        if cell_obj.value is not None:
                            year_11 = cell_obj.value
                    if cell_obj.column_letter == 'AB':
                        if cell_obj.value is not None:
                            year_12 = cell_obj.value
                    if cell_obj.column_letter == 'AC':
                        if cell_obj.value is not None:
                            year_13 = cell_obj.value
                    if cell_obj.column_letter == 'AD':
                        if cell_obj.value is not None:
                            year_14 = cell_obj.value
                    if cell_obj.column_letter == 'AE':
                        if cell_obj.value is not None:
                            year_15 = cell_obj.value
                    if cell_obj.column_letter == 'AF':
                        if cell_obj.value is not None:
                            year_16 = cell_obj.value
                    if cell_obj.column_letter == 'AG':
                        if cell_obj.value is not None:
                            year_17 = cell_obj.value
                    if cell_obj.column_letter == 'AH':
                        if cell_obj.value is not None:
                            year_18 = cell_obj.value
                    if cell_obj.column_letter == 'AI':
                        if cell_obj.value is not None:
                            year_19 = cell_obj.value
                    if cell_obj.column_letter == 'AJ':
                        if cell_obj.value is not None:
                            year_20 = cell_obj.value
                    
                    print(cell_obj.value, end='|')
                #finish getting values in one row
                country = Country.objects.create(
                    country_name = c_name,
                    country_code = c_code,
                    is_country = is_c,
                    region = reg,
                    income_group = income,
                )
                
                data_1 = Data.objects.create(country = country, year = 1990, emission = year_90)
                data_2 = Data.objects.create(country = country, year = 1991, emission = year_91)
                data_3 = Data.objects.create(country = country, year = 1992, emission = year_92)
                data_4 = Data.objects.create(country = country, year = 1993, emission = year_93)
                data_5 = Data.objects.create(country = country, year = 1994, emission = year_94)
                data_6 = Data.objects.create(country = country, year = 1995, emission = year_95)
                data_7 = Data.objects.create(country = country, year = 1996, emission = year_96)
                data_8 = Data.objects.create(country = country, year = 1997, emission = year_97)
                data_9 = Data.objects.create(country = country, year = 1998, emission = year_98)
                data_10 = Data.objects.create(country = country, year = 1999, emission = year_99)
                data_11 = Data.objects.create(country = country, year = 2000, emission = year_00)
                data_12 = Data.objects.create(country = country, year = 2001, emission = year_01)
                data_13 = Data.objects.create(country = country, year = 2002, emission = year_02)
                data_14 = Data.objects.create(country = country, year = 2003, emission = year_03)
                data_15 = Data.objects.create(country = country, year = 2004, emission = year_04)
                data_16 = Data.objects.create(country = country, year = 2005, emission = year_05)
                data_17 = Data.objects.create(country = country, year = 2006, emission = year_06)
                data_18 = Data.objects.create(country = country, year = 2007, emission = year_07)
                data_19 = Data.objects.create(country = country, year = 2008, emission = year_08)
                data_20 = Data.objects.create(country = country, year = 2009, emission = year_09)
                data_21 = Data.objects.create(country = country, year = 2010, emission = year_10)
                data_22 = Data.objects.create(country = country, year = 2011, emission = year_11)
                data_23 = Data.objects.create(country = country, year = 2012, emission = year_12)
                data_24 = Data.objects.create(country = country, year = 2013, emission = year_13)
                data_25 = Data.objects.create(country = country, year = 2014, emission = year_14)
                data_26 = Data.objects.create(country = country, year = 2015, emission = year_15)
                data_27 = Data.objects.create(country = country, year = 2016, emission = year_16)
                data_28 = Data.objects.create(country = country, year = 2017, emission = year_17)
                data_29 = Data.objects.create(country = country, year = 2018, emission = year_18)
                data_30 = Data.objects.create(country = country, year = 2019, emission = year_19)
                data_31 = Data.objects.create(country = country, year = 2020, emission = year_20)
                print(' saved ')
                print('\n')
```
With this we can drop the data from the table, and then load it in, as required. Run the file with the command:
```bash
    python3 manage.py parse_cities
```
This will run for a little time.

When loading finished, we can test whether the data is in the database. Use this command to open a shell to query the sqlite database:
```bash
    python3 manage.py dbshell
```
Then try this command or other commands you want to use:
```bash
    select * from visual_emission_country where income_group='High income';
```
This command will show all countries whose income_group is 'High income'.

### Create Templates
Now we will create templates for our app. Create a new folder named 'templates' under 'visual_emission', inside this folder we will place all templates.
In settings.py, change this line in TEMPLATES:
```python
    'DIRS': [BASE_DIR/'templates'],
```
