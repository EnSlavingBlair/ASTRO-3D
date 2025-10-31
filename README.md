# ASTRO-3D
Code accompanying any science outreach activities developed or used at Curtin University, under ASTRO 3D. Assuming users will have minimal knowledge of coding, so some explanations may seem overly detailed.

Escape the Cosmic Microwave Background Maze:
- histData.txt is where the user input should be stored - make sure histogram_building.py is reading that folder
- Open two terminal windows and navigate to the folder this code has been saved in.
- Run addData.py first in one terminal (eg: python3 addData.py), this will open a tkinter window for the user to enter data into histData.txt. 
- Now run histogram_building.py in the other terminal. 
- It will open an empty histogram plot and run with whatever data is in histData.txt first, and live update with any new data added into the tkinter window.
