# CS551Q_Assignment_1

### What is this?
This `README.md` file (version 2.0) shows some problems I met in the process of doing this Assignment. Hope this will help you.

### Use of <script> in Templates
Although the project brief states that "there should be no JavaScript in your submission," clarification was sought from the instructor, who confirmed that the restriction refers to the Java programming language, not the client-side scripting language JavaScript. As such, the use of <script> tags in HTML templates for basic front-end interactivity and data visualization is acceptable within the scope of this Python-based assignment.
In this project, JavaScript is only used to support the dynamic display of CO₂ emissions through charts and user-controlled filters (e.g., selecting countries or adjusting year ranges). This enhances the interpretability of open data and does not compromise the Python-focused nature of the assignment. All core logic, data processing, and database interactions are handled by Django and Python on the server side.

# How to run through codio (local version)
first start the virtual environment:
```bash
    source .venv/bin/activate
```
then you should go into the project file:
```bash
    cd team_assignment
```
now you can run the server:
```bash
    python3 manage.py runserver 0.0.0.0:8000
```
Finally you can visit this url to get to our homepage: https://randomevent-spenddemand-8000.codio-box.uk/co2

# Preparations in advance if you are going to edit the assignment files

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
This will download all the files into your codio as a new folder '*CS551Q_Assignment_1*'. To make edits and commits easier, please move all files out of the folder.
The filetree should look at: '.venv', 'team_assignment' and 'sqlite-autoconf-3490100' folders, and other four files.

### Get sqlite version 3.49.1
Please use this command to check your sqlite version:
```bash
    sqlite3 --version
```
If your version is 3.22, please update the version. In the files downloaded from github, there are prepared sqlite documents.
```bash
    cd sqlite-autoconf-3490100
    ./configure --prefix=$HOME/sqlite
    make
    make install
```
Then set environment variables so Python uses the new SQLite:
```bash
    export PATH="$HOME/sqlite/bin:$PATH"
    export LD_LIBRARY_PATH="$HOME/sqlite/lib"
```
Check version again and your sqlite should be 3.49.1

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
            try:
                book = load_workbook(book_path)
                sheet = book['Data']
            except FileNotFoundError:
                raise CommandError(f"File not found: {book_path}")
            except KeyError:
                raise CommandError("Worksheet named 'Data' not found in the Excel file.")
            print(sheet.title)
            max_row_num = sheet.max_row
            max_col_num = sheet.max_column
            print(f'Rows: {max_row_num}, Columns: {max_col_num}')

            start_year = 1990 # years are from 1990 to 2020
            data_start_col = 6 # data start at column F, which is the 6th

            for i in range(2, max_row_num + 1):
                try:
                    row_data = [sheet.cell(row=i, column=j).value for j in range(1, max_col_num + 1)] # get the data of one row
                    c_name = row_data[0]
                    c_code = row_data[1]
                    is_c = row_data[2]
                    reg = row_data[3] if row_data[3] else ''
                    income = row_data[4] if row_data[4] else ''

                    country = Country.objects.create(
                        country_name = c_name,
                        country_code = c_code,
                        is_country = is_c,
                        region = reg,
                        income_group = income,
                    )

                    data_objects = []
                    for j in range(data_start_col-1, max_col_num): # the index starts with 0, so the data_start_col should -1
                        year = start_year + (j-data_start_col+1)
                        emission = row_data[j]
                        if emission is not None:
                            data_objects.append(Data(country = country, year = year, emission = emission))
                        
                    Data.objects.bulk_create(data_objects)
                    print(f'{c_name} saved')
                except Exception as e:
                    print(f'Error processing row {i}: {e}')
            
            print('all data saved')
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
This makes sure it can find our templates.
For there are many templates in visual_emission, the process of creating each template will not be shown in detail.
All templates and their usage will be listed here:
_'404.html' and '500.html' -- for error control_
_'chart.html' -- for drawing the line chart in detail pages_
_'country_info.html' and 'group_info.html' -- for showing country or group information in detail pages_
_'country_list.html' -- it is the sidebar of each pages_
_'data.html' -- it is the detail page for all countries and groups_
_'feedback.html' -- for collecting feedback from users -- it is not done yet!_
_'homepage.html' -- it is the homepage of our app_
_'main.html' -- it is the parent template for other templates_
In this step, 'urls.py' and 'views.py' in 'visual_emission' folder are also edited.