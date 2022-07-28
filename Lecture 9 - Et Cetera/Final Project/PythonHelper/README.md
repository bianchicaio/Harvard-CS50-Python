 # PYTHON HELPER
    #### Video Demo:  <https://youtu.be/iGs63Jt2y5U>
    #### Description:
    My project was made with the idea of helping python developers to find good 
    libraries depending on what they need.

    ### Requirements:
        - python  version == 3.10.2
        - tkinter  version == 0.1.0
        - tkinter.ttk version == 0.1.0
        - webbrowser
        - colorama
        - setuptools
        - pytest == 7.1.2

    ### My project has 2 versions:
        ### - project1.py (first version):
        The first version prompt the user for a subject of python, such as:
            - Data Science
            - Web Application
            - Mobile App
            - Games
            - Automation
        
        Depending on the subject of choice, the program will now prompt the user the avaible libraries that he can choose from, for example if the user chooses 'Games Subject', the system will give back the options:
            - Pygame
            - Pykyra
            - Pyglet

        Now the user just have to type in the library of choice and the program will give back the link for it's documentation

        #### CODE:
            The code of the first version has one object called PythonHelper, that contains:
            
            - self.subjects: a dictionary with all subjects, libraries and documentation links
            
            - get_subject function: the function that prompt the user for a subject and verify that is a avaible choice

            - get_lib function: the function that prompt the user for a library and give back it's documentation

###########################################################################################################

        ### - project.py (second version):
        The second version will create a Graphic User Interface (GUI) that has the subjects and the libraries as TreeView, when you open one subject it shows the user all possible libraries.

        The only thing the user need to do is double-click the library of choice to open it's documentation.

        ### CODE:
            The code of the second version has two objects one is called PythonHelper and the other is called Screen:
            
            - The first object just like the first version, has a dictionary with all subjects, libraries and documentation links, but here it does not have the get_subject and get_lib functions.

            - The second object called Screen is an Tkinter object that gives the user a GUI.

            - The Screen object create one column and many rows in a TreeView style, to make rows with "child" rows

            - The rows access the PythonHelper object to get the libraries links

        This version is more user friendly!

