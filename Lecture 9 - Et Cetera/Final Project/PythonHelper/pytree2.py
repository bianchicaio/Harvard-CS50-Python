# Python Helper, show best libraries per subject and give documentation url
# Object Python Helper
class PythonHelper:
    def __init__(self):
        self.subjects = {'Data Science': ['Pandas', 'Scikitlearn', 'Matplotlib', 'Seaborn','Pytorch',
                                          'Keras', 'Tensorflow'],
                         'Web Applcation': ['Django', 'Flask', 'Cherrypy'],
                         'Mobile App': ['Kivy', 'Tkinter'],
                         'Games': ['Pygame', 'Pykyra', 'Pyglet'],
                         'Automation': ['Urllib', 'Requests', 'Webbot', 'Beautifulsoup', 'Scrapy',  
                                        'Selenium']
                        }

    # Prompt user for a subject
    def get_subject(self):
        sub = 's'
        while sub not in self.subjects:
            sub = input('Choose a subject of Python: Data Science/Web Application/Mobile App/Games/Automation:   ').title()
            if sub in self.subjects:
                return sub

    # Gets the subject and return a choosen library
    def get_lib(self, sub):
        lib = 's'
        while lib not in self.subjects:
            if sub == 'Data Science':
                lib = input('Choose a library for Data Science: Pandas/Scikitlearn/Matplotlib/Seaborn/Pytorch/Keras/Tensorflow:  ').title()
                if lib in self.subjects['Data Science']:
                    return lib

            elif sub == 'Web Application':
                lib = input('Choose a library for Web Development: Djando/Flask/Cherrypy:  ').title()
                if lib in self.subjects['Web Application']:
                    return lib

            elif sub == 'Mobile Application':
                lib = input('Choose a library for Mobile Development: Kivy/Tkinter:  ').title()
                if lib in self.subjects['Mobile App']:
                    return lib

            elif sub == 'Games':
                lib = input('Choose a library for Game Development: Pygame/Pykyra/Pyglet:  ').title()
                if lib in self.subjects['Games']:
                    return lib

            elif sub == 'Automation':
                lib = input('Choose a library for Automation: Urllib/Requests/Webbot/Beatifulsoup/Scrapy/Selenium:  ').title()
                if lib in self.subjects['Automation']:
                    return lib

    # Gets the library and return it´s documentation
    def get_doc(self, lib):
        # Data Science Libs
        if lib == 'Pandas':
            return 'https://pandas.pydata.org/docs/#'
        elif lib == 'Scikitlearn':
            return 'https://scikit-learn.org/stable/'
        elif lib == 'Matplotlib':
            return 'https://matplotlib.org/'
        elif lib == 'Seaborn':
            return 'https://seaborn.pydata.org/tutorial.html'
        elif lib == 'Pytorch':
            return 'https://pytorch.org/'
        elif lib == 'Keras':
            return 'https://keras.io/'
        elif lib == 'Tensorflow':
            return 'https://www.tensorflow.org/'

        # Web App Libs
        elif lib == 'Django':
            return 'https://docs.djangoproject.com/en/4.0/'
        elif lib == 'Flask':
            return 'https://flask.palletsprojects.com/en/2.1.x/'
        elif lib == 'Cherrypy':
            return 'https://docs.cherrypy.dev/en/latest/'

        # Mobile App Libs
        elif lib == 'Kivy':
            return 'https://kivy.org/doc/stable/'
        elif lib == 'Tkinter':
            return 'https://docs.python.org/3/library/tk.html'

        # Games Libs
        elif lib == 'Pygame':
            return 'https://www.pygame.org/news'
        elif lib == 'Pykyra':
            return 'https://pypi.org/project/pykira/'
        elif lib == 'Pyglet':
            return 'https://pyglet.readthedocs.io/en/latest/'

        # Automation Libs
        elif lib == 'Urllib':
            return 'https://docs.python.org/3/library/urllib.html'
        elif lib == 'Requests':
            return 'https://requests.readthedocs.io/en/latest/'
        elif lib == 'Webbot':
            return 'https://webbot.readthedocs.io/en/latest/'
        elif lib == 'Beatifulsoup':
            return 'https://beautiful-soup-4.readthedocs.io/en/latest/'
        elif lib == 'Scrapy':
            return 'https://docs.scrapy.org/en/latest/'
        elif lib == 'Selenium':
            return 'https://selenium-python.readthedocs.io/'


def main():
    try:
        pyhelper = PythonHelper()
        sub = pyhelper.get_subject()
        lib = pyhelper.get_lib(sub)
        doc = pyhelper.get_doc(lib)
        print(doc)
    except ValueError:
        main()

main()
