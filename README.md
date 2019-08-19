# ASTRO-3D
Code accompanying any science outreach activities developed or used at Curtin University, under ASTRO 3D. 

Escape the Cosmic Microwave Background Maze:
- histData.txt is where the user input should be stored - make sure histogram_building.py is reading that folder
- Open two Anaconda prompt windows. Navigate to this folder. Run addData.py first
- addData.py adds the user input to the histData.txt. Run it with the command exec(open("addData.py").read())
- Now run histogram_building.py. It will open an empty histogram plot and run with whatever data is in histData first, then give you a prompt to input data.
- Run with the command exec(open("histogram_building.py").read())
- To end the program, type "end" (without the quotation marks) into addData.py, and close others as appropriate. 
