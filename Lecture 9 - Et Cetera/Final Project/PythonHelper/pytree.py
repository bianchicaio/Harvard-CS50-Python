# Python Helper, show best libraries per subject and give documentation url
# Lists of subjects and libraries
subjects = ['Data Science', 'Web Application', 'Mobile App', 'Games', 'Automation']
data_science = ['Pandas', 'Scikitlearn', 'Matplotlib', 'Seaborn', 'Pytorch', 'Keras',
                 'Tensorflow']
web_app = ['Django', 'Flask', 'Cherrypy']
mobile_app = ['Kivy', 'Tkinter']
pygames = ['Pygame', 'Pykyra', 'Pyglet']
automation = ['Urllib', 'Requests', 'Webbot', 'Beautifulsoup', 'Scrapy', 'Selenium']

# Chosse the subject and give back the library documentation url
def choose_subject():
    subj = input('Choose a subject of Python: Data Science/Web Application/Mobile App/Games/Automation:   ').title()
    if subj == 'Data Science':
        lib = choose_data()
        return get_doc(lib)

    elif subj == 'Web Application':
        lib = choose_web()
        return get_doc(lib)

    elif subj == 'Mobile App':
        lib = choose_mobile()
        return get_doc(lib)

    elif subj == 'Games':
        lib = choose_games()
        return get_doc(lib)

    elif subj == 'Automation':
        lib = choose_aut()
        return get_doc(lib)

    else:
        main()

# Choose a Data Science Lib
def choose_data():
    i = 's'
    while i not in data_science:
        i = input('Choose a library for Data Science: Pandas/Scikitlearn/Matplotlib/Seaborn/Pytorch/Keras/Tensorflow:  ').title()
    if i in data_science:
        return i

# Choose a Web App Lib
def choose_web():
    i = 's'
    while i not in web_app:
        i = input('Choose a library for Web Development: Djando/Flask/Cherrypy:  ').title()
    if i in web_app:
        return i

# Choose a Mobile App Lib
def choose_mobile():
    i = 's'
    while i not in mobile_app:
        i = input('Choose a library for Mobile Development: Kivy/Tkinter:  ').title()
    if i in mobile_app:
        return i

# Choose a Game Lib
def choose_games():
    i = 's'
    while i not in pygames:
        i = input('Choose a library for Game Development: Pygame/Pykyra/Pyglet:  ').title()
    if i in pygames:
        return i

# Choose a Automation Lib
def choose_aut():
    i = 's'
    while i not in automation:
        i = input('Choose a library for Web Develop: Urllib/Requests/Webbot/Beatifulsoup/Scrapy/Selenium:  ').title()
    if i in automation:
        return i

# Get Documentation
def get_doc(lib):
    # Data Science Libs
    if lib == 'Pandas':
        print('https://pandas.pydata.org/docs/#')
    elif lib == 'Scikitlearn':
        print('https://scikit-learn.org/stable/')
    elif lib == 'Matplotlib':
        print('https://matplotlib.org/')
    elif lib == 'Seaborn':
        print('https://seaborn.pydata.org/tutorial.html')
    elif lib == 'Pytorch':
        print('https://pytorch.org/')
    elif lib == 'Keras':
        print('https://keras.io/')
    elif lib == 'Tensorflow':
        print('https://www.tensorflow.org/')

    # Web App Libs
    elif lib == 'Django':
        print('https://docs.djangoproject.com/en/4.0/')
    elif lib == 'Flask':
        print('https://flask.palletsprojects.com/en/2.1.x/')
    elif lib == 'Cherrypy':
        print('https://docs.cherrypy.dev/en/latest/')

    # Mobile App Libs
    elif lib == 'Kivy':
        print('https://kivy.org/doc/stable/')
    elif lib == 'Tkinter':
        print('https://docs.python.org/3/library/tk.html')

    # Games Libs
    elif lib == 'Pygame':
        print('https://www.pygame.org/news')
    elif lib == 'Pykyra':
        print('https://pypi.org/project/pykira/')
    elif lib == 'Pyglet':
        print('https://pyglet.readthedocs.io/en/latest/')

    # Automation Libs
    elif lib == 'Urllib':
        print('https://docs.python.org/3/library/urllib.html')
    elif lib == 'Requests':
        print('https://requests.readthedocs.io/en/latest/')
    elif lib == 'Webbot':
        print('https://webbot.readthedocs.io/en/latest/')
    elif lib == 'Beatifulsoup':
        print('https://beautiful-soup-4.readthedocs.io/en/latest/')
    elif lib == 'Scrapy':
        print('https://docs.scrapy.org/en/latest/')
    elif lib == 'Selenium':
        print('https://selenium-python.readthedocs.io/')


def main():
    choose_subject()

main()