# uk-life-tables-actuarial-pipeline
A personal project to help learn actuarial practices and techniques whilst studying CM1


# Set Up

## 1. Create the repo on GitHub
Go to github.com, click 'New repository'. Give it a clear name (e.g. uk-life-tables-actuarial-pipeline), add a short description, set it to Public (so you can link it on your CV/LinkedIn later), and tick 'Add a README file'. Don't add a .gitignore or license yet - you'll add a Python-specific .gitignore in the next step.

## 2. Clone it to laptop
Copy the repo's URL (the green 'Code' button), then in your terminal run: git clone <url>, then cd into the new folder. This gives you a local copy already connected to GitHub, so every commit you make can be pushed straight back up.

## 3. Set up virutal environment
Inside the project folder, run python -m venv venv, then activate it (source venv/bin/activate on Mac/Linux, venv\Scripts\activate on Windows). This keeps this project's Python packages (pandas, sqlite3 support, streamlit) separate from anything else on your laptop - good practice worth demonstrating.

## 4. Add a proper .gitignore
Create a .gitignore file and add entries for venv/, __pycache__/, *.pyc, and any raw data files you don't want committed (e.g. raw/*.xlsx if the files are large - GitHub isn't meant for big data files). You can copy a standard Python .gitignore template from gitignore.io or GitHub's own templates.

## 5. Set up folder structure before writing code
Create folders like: raw/ (untouched downloaded ONS files), scripts/ or src/ (your Python scripts), notebooks/ (if you want to explore data in Jupyter first), and app.py at the root for your eventual Streamlit app. A clear structure from day one makes the repo look organised to anyone reviewing it later.

## 6. Install your packages and freeze them
With the venv active, pip install pandas streamlit (add sqlalchemy too if you want a cleaner Python-to-SQL connection layer rather than raw sqlite3). Then run pip freeze > requirements.txt so anyone (including future-you) can recreate your environment with one command.

## 7. first commit
Write your README with a short project description (what it does, what data it uses, tech stack) even before the code exists - it's good practice and gives you a clear target. Then git add ., git commit -m "Initial project setup", and git push to send it to GitHub.