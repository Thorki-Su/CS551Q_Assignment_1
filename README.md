# CS551Q_Assignment_1

### What is this?
This `README.md` file, showing the instructions for running this app.

# Use of <script> in Templates
Although the project brief states that "there should be no JavaScript in your submission," clarification was sought from the instructor, who confirmed that the restriction refers to the Java programming language, not the client-side scripting language JavaScript. As such, the use of <script> tags in HTML templates for basic front-end interactivity and data visualization is acceptable within the scope of this Python-based assignment.
In this project, JavaScript is only used to support the dynamic display of CO₂ emissions through charts and user-controlled filters (e.g., selecting countries or adjusting year ranges). This enhances the interpretability of open data and does not compromise the Python-focused nature of the assignment. All core logic, data processing, and database interactions are handled by Django and Python on the server side.

# How to run (with HEROKU)
please visit this url to get to our homepage: https://assignment1-da2a55867328.herokuapp.com
We've prepared two accounts. 
Ordinary Account [username: testman, password: test20250421]
Admin Account [username: codio, password: codio]
With admin account you can see the feedbacks from other users.

# How to run through codio (local version)
use this command:
```bash
source .venv/bin/activate
cd team_assignment
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

# Usage of Templates
All templates and their usage will be listed here:
'404.html' and '500.html' for error control. 'admin_dashboard.html' for the admin page. 'chart.html' for drawing the line chart in detail pages. 'country_info.html' and 'group_info.html' for showing country or group information in detail pages. 'country_list.html' is the sidebar of each pages. 'data.html' is the detail page for all countries and groups. 'feedback.html' for collecting feedback from users. 'homepage.html' is the homepage of our app. 'login.html' for log-in page. 'main.html' -- it is the parent template for other templates.

# Data sources
The emission data we use comes from CS551A (2024-25): Fundamentals Of Software Project Management. You can find the excel file in 'visual_emission/country_data/data_upload'.
The map feature uses open source data and tools. The open sourse data: https://github.com/datasets/geo-countries. The open source tool: https://leafletjs.com/.

# Cleaning the Dataset and Reasoning Behind Reducing our Dataset.
### What was done

Clean structure and ready for analysis.
Redundant metadata and empty rows were removed.
Proper headers were applied.
Retained global and country-level CO₂ emissions data across multiple years.

### Reasoning

To make data suitable and simpler for usability sake in Python.
To reduce our chances of analyzing wrong values or running into errors caused by blank or empty columns or mislabeled headers.
For smaller and more focused datasets run faster and took up less memory.
The cleaned data was easier to interpret for report and analysis sake.
It made it easier to create visuals like CO₂ trends across time and comparisons between countries.

# The name in git-log
Thorki Su is the username of Peiheng Su in github.
