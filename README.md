# Attack-Tree-Generation

**Setting Up Environment**
- Install mrcl2 (Latest Release - 201808.0) in your machine using https://www.mcrl2.org/web/user_manual/download.html
- Install Graphviz to display graphs through https://graphviz.gitlab.io/_pages/Download/Download_windows.html
- Add below paths to your computer's user environment variables (If different installation is used, please change it to an appropriate one)
> C:\Program Files\mCRL2\bin

> C:\Program Files (x86)\Graphviz2.38\bin

- Make sure you've got Python3 version running(Python 3.7 or higher).  You can verify it by opening command prompt and givng 
> "python --version" command.
- Open command prompt and install necessary python libraries mentioned below using commands
> pip install antlr4-python3-runtime
> pip install numpy
> pip install graphviz

- Open "Terminal" or "Command Prompt" with administrative access, navigate to the "Test" directory and use the command "python FileParser.py" to run the application.
- Select the specification file needed from the "Test" directory. Two specification files were provided to test the application, you can select one from them. 
- Once you select the mcrl2 file, wait for the software to generate traces and visualize trees.
