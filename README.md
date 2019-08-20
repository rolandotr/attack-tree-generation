# Attack-Tree-Generation

**Setting Up Environment**
- Download and install Apache Server or XAMPP package (if it's not installed).
- Open your public_html folder (or htdocs for XAMPP) and place the whole repository.
- Install mrcl2 (Latest Release - 201808.0) in your machine using https://www.mcrl2.org/web/user_manual/download.html
- Install Graphviz to display graphs through https://graphviz.gitlab.io/_pages/Download/Download_windows.html
- Add below paths to your computer's user environment variables (If different installation is used, please change it to an appropriate one)
> C:\Program Files\mCRL2\bin

> C:\Program Files (x86)\Graphviz2.38\bin

- Make sure you've got Python3 version (Python 3.6 or higher)
- Open command prompt and install python library for graphviz using
> pip install graphviz

- Go to "Test" directory and edit "FileParser.py"
- Change the code on line 21 from:
> os.chdir("C:/Users/dnagumot/xampp/htdocs/attack_trees/Test")

to

> os.chdir("Drive:/"Path to public_html folder"/attack_tree-generation/Test") 

- Get the server running.
- Access it through http://localhost/attack-tree-generation/

**Web Interface Instructions**
- Navigate to http://localhost/attack-tree-generation/.
- Copy and paste the mCRL2 code.
- Click on Generate trees button and wait for the trees to display.
