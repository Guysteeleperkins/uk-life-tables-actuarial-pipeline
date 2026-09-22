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


Next steps:

created extract code to extract data from all the sheets and combine them, added columns etc


ran some quick visual tests to see if the data was looking clean before tranforming anything 

print(combined.shape)
print(combined["time_period"].nunique())
print(combined["sex"].value_counts()) 

(8686, 8)
43
sex
male      4343
female    4343
Name: count, dtype: int64

print(combined.head(10))
print(combined.tail(10))
print(combined.sample(10))
print(combined.isnull().sum())
print(combined.describe())
print(combined[
    (combined["time_period"] =="2022-2024")
    & (combined["sex"] == "male")].head())

 age        mx        qx        lx     dx     ex   sex time_period
0    0  0.004612  0.004602  100000.0  460.2  79.12  male   2022-2024
1    1  0.000247  0.000247   99539.8   24.6  78.49  male   2022-2024
2    2  0.000177  0.000177   99515.3   17.6  77.51  male   2022-2024
3    3  0.000115  0.000115   99497.6   11.4  76.52  male   2022-2024
4    4  0.000100  0.000100   99486.2    9.9  75.53  male   2022-2024
5    5  0.000097  0.000097   99476.3    9.6  74.54  male   2022-2024
6    6  0.000080  0.000080   99466.7    7.9  73.54  male   2022-2024
7    7  0.000080  0.000080   99458.7    8.0  72.55  male   2022-2024
8    8  0.000079  0.000079   99450.7    7.8  71.56  male   2022-2024
9    9  0.000091  0.000091   99442.9    9.1  70.56  male   2022-2024
      age        mx        qx       lx      dx    ex     sex time_period
8676   91  0.213316  0.192757  11778.3  2270.4  3.71  female   1980-1982
8677   92  0.235470  0.210667   9508.0  2003.0  3.48  female   1980-1982
8678   93  0.251662  0.223535   7505.0  1677.6  3.28  female   1980-1982
8679   94  0.273758  0.240797   5827.3  1403.2  3.08  female   1980-1982
8680   95  0.297353  0.258866   4424.1  1145.3  2.89  female   1980-1982
8681   96  0.319205  0.275271   3278.9   902.6  2.73  female   1980-1982
8682   97  0.341109  0.291408   2376.3   692.5  2.57  female   1980-1982
8683   98  0.365451  0.308990   1683.8   520.3  2.43  female   1980-1982
8684   99  0.361933  0.306472   1163.5   356.6  2.29  female   1980-1982
8685  100  0.439885  0.360578    806.9   291.0  2.08  female   1980-1982
      age        mx        qx       lx      dx     ex     sex time_period
2110   90  0.182000  0.166819  20154.7  3362.2   4.00    male   2012-2014
5704   48  0.003353  0.003348  94752.6   317.2  28.55    male   1994-1996
8162   82  0.139433  0.130346  23286.7  3035.3   5.25    male   1982-1984
7303   31  0.000945  0.000945  97257.0    91.9  42.85    male   1986-1988
5819   62  0.009275  0.009232  90643.8   836.9  20.62  female   1994-1996
138    37  0.000717  0.000717  98832.6    70.8  46.79  female   2022-2024
7572   98  0.419453  0.346734    462.5   160.4   2.32    male   1985-1987
6213   52  0.003670  0.003663  95751.4   350.8  29.01  female   1992-1994
4288   46  0.002799  0.002795  95601.7   267.2  32.05    male   2001-2003
1687   71  0.021839  0.021603  78972.5  1706.0  13.99    male   2014-2016
age            0
mx             0
qx             0
lx             0
dx             0
ex             0
sex            0
time_period    0
dtype: int64
               age           mx           qx             lx           dx           ex
count  8686.000000  8686.000000  8686.000000    8686.000000  8686.000000  8686.000000
mean     50.000000     0.051446     0.045858   77796.863746   982.982535    33.417611
std      29.156438     0.101669     0.086852   31464.433532  1245.330798    24.083406
min       0.000000     0.000046     0.000046     151.900000     4.600000     1.720000
25%      25.000000     0.000559     0.000559   67835.225000    55.225000    10.450000
50%      50.000000     0.003539     0.003533   95575.350000   309.600000    30.240000
75%      75.000000     0.040481     0.039677   98777.100000  1644.175000    54.200000
max     100.000000     0.527839     0.417621  100000.000000  4487.000000    83.020000
   age        mx        qx        lx     dx     ex   sex time_period
0    0  0.004612  0.004602  100000.0  460.2  79.12  male   2022-2024
1    1  0.000247  0.000247   99539.8   24.6  78.49  male   2022-2024
2    2  0.000177  0.000177   99515.3   17.6  77.51  male   2022-2024
3    3  0.000115  0.000115   99497.6   11.4  76.52  male   2022-2024
4    4  0.000100  0.000100   99486.2    9.9  75.53  male   2022-2024

Zero nulls across every column — no missing data to handle, which simplifies your transform step considerably
qx and mx values sit sensibly between 0 and ~0.53 — since these are probabilities/rates, they should never exceed 1, and they don't
lx decreases correctly within each group — starts at 100,000 (the standard actuarial starting cohort) and falls as age increases, which is exactly the expected pattern
The random sample shows a good mix of different sexes and time periods scattered through the table — confirms your data isn't accidentally grouped or ordered strangely
describe() produced numeric stats for every column — this is actually a quiet confirmation that age, mx, qx, lx, dx, ex all came in as proper numbers, not text — if any had been read as strings, describe() wouldn't have been able to calculate a mean/std for them at all

checking about age as it maxes out at 100. Real life tables often stop at a specific age by grouping everyone older into a single "x and over" row. 

print(combined[combined["age"] == 100][["age", "lx", "ex", "sex", "time_period"]].head())

What this shows: at age 100, lx (survivors) is still a meaningful number
(993.1 males, 2,638.6 females out of the original 100,000 cohort) and ex
(life expectancy) is a small but real number (1.79, 2.11 years) — not zero,
not a rounding artifact. This is completely consistent with age 100 being an
"100 and over" aggregate row rather than a precise single age. In other words,
everyone who reached 100 or older in that cohort is bucketed into this one
row, and the ex value represents their average remaining life expectancy from
that point.

