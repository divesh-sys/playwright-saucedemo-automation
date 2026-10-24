Listing key Git and Jenkins commands for quick reference.
Listing key Git and Jenkins commands for quick reference.
Git and GitHub commands
Command	Meaning	When to use it
git --version	Shows the installed Git version	To check that Git is installed
git config --global user.name "Divesh Jadhav"	Saves your name for commits	Once, on a new computer
git config --global user.email "diveshjadhav1193@gmail.com"	Saves your email for commits	Once, on a new computer
git init	Turns the folder into a Git project	Once, at the start of a project
git status	Shows which files changed	Any time you are unsure what state things are in
git add .	Selects all changed files (the dot matters)	Before every commit
git commit -m "message"	Saves a version with a short note	After git add .
git branch -M main	Names your branch main	Once, before the first push
git remote add origin <url>	Connects your folder to the GitHub repo	Once, after creating the repo
git remote -v	Shows which GitHub repo is connected	To check the link is correct
git remote set-url origin <url>	Changes the GitHub link	When origin already exists or the URL is wrong
git push -u origin main	Uploads your code to GitHub and remembers the link	The first push
git push	Uploads your new commits	Every time after the first push
git pull --no-edit	Downloads changes from GitHub without opening an editor	When you edited files on the GitHub website
Daily routine (the 3 you use most):

git add .
git commit -m "Describe what you changed"
git push
Jenkins commands
Command	Meaning	When to use it
java -version	Shows the Java version	To check that Java works before starting Jenkins
set "JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-25.0.4.101-hotspot"	Tells CMD where Java is	In each new CMD window, before starting Jenkins
set "PATH=%JAVA_HOME%\bin;%PATH%"	Lets CMD find java	Right after the line above
cd C:\jenkins	Goes into the Jenkins folder	Before starting Jenkins
java -jar jenkins.war --httpPort=8080	Starts the Jenkins server	Every time you want Jenkins running (keep the window open)
Ctrl+C	Stops the running program	To shut Jenkins down
type C:\Users\MUR90411\.jenkins\secrets\initialAdminPassword	Shows the first-time unlock password	Only on the first login
py -3.12 -c "import sys; print(sys.executable)"	Prints the path of Python 3.12	To fill in the PYTHON line in the Jenkinsfile
type nul > Jenkinsfile	Creates an empty Jenkinsfile with no .txt ending	When you create the file
C:\Windows\System32\notepad.exe Jenkinsfile	Opens the file in Notepad	To edit the pipeline
dir Jenkinsfile*	Lists matching files	To check the name is exactly Jenkinsfile
ren Jenkinsfile.txt Jenkinsfile	Renames the file	If Notepad added .txt
Commands inside the Jenkinsfile (Jenkins runs them for you):

Command	Meaning
python -m venv .venv	Creates the virtual environment
pip install -r requirements.txt	Installs the packages
playwright install	Downloads the browsers
ruff check .	Checks code style
pytest --browser chromium --browser firefox --browser webkit --junitxml=reports/junit.xml	Runs the tests on 3 browsers and saves results for Jenkins
Start Jenkins (the 4 lines you repeat):

set "JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-25.0.4.101-hotspot"
set "PATH=%JAVA_HOME%\bin;%PATH%"
cd C:\jenkins
java -jar jenkins.war --httpPort=8080
Then open http://localhost:8080 in your browser.

Remember: Jenkins reads the Jenkinsfile from GitHub, so every pipeline change needs git add ., git commit, git push before you click Build Now.

