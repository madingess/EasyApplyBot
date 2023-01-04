# LinkedIn Easy Apply Bot
Automatically apply to LinkedIn Easy Apply jobs. This bot answers the application questions as well!

This is for educational purposes only. I am not responsible if your LinkedIn account gets suspended or for anything else.

This bot is written in Python using Selenium.

## Fork Notes

The original code was failing and no longer maintained. This was forked for the purpose of patching and sharing with new features added.

By Michael Dingess

## Setup & Startup

To run the bot, open the command line in the cloned repository directory. Activate the virtual environment and start the bot using these commands:
```bash
source venv/bin/activate
python3 main.py
```

Next, you need to fill out the config.yaml file. Most of this is self-explanatory but if you need explanations please see the end of this README.

```yaml
email: email@domain.com
password: yourpassword

disableAntiLock: False

remote: True

experienceLevel:
 internship: False
 entry: True
 associate: False
 mid-senior level: False
 director: False
 executive: False

jobTypes:
 full-time: True
 contract: True
 part-time: False
 temporary: True
 internship: False
 other: False
 volunteer: False

date:
 all time: True
 month: False
 week: False
 24 hours: False

positions:
 #- First position
 #- A second position
 #- A third position
 #- ...
locations:
 #- First location
 #- A second location
 #- A third location
 #- ...
 - Remote
distance: 25

outputFileDirectory: ~/Documents/Applications/EasyApplyBot/EasyApplyBot/

companyBlacklist:
 #- company
 #- company2

titleBlacklist:
 #- word1
 #- word2

posterBlacklist:
 #- name1
 #- name2

uploads:
 resume: C:\Users\myDirectory\Resume.pdf
 # Cover letter is optional
 #coverLetter: C:\Users\myDirectory\CoverLettter.pdf


# ------------ QA section -------------------

# ------------ Additional parameters: checkboxes ---------------
checkboxes:
 # Do you have a valid driver's license? (yes/no checkbox)
 driversLicence: True
 # Will you now, or in the future, require sponsorship for employment visa status (e.g. H-1B visa status)? (yes/no checkbox)
 # This is relative to the location and your citizenship applying above, and same with legallyAuthorized.
 requireVisa: False
 # Are you legally authorized to work in COUNTRY? (yes/no checkbox)
 legallyAuthorized: True
 # We must fill this position urgently. Can you start immediately? (yes/no checkbox)
 urgentFill: True
 # Are you comfortable commuting to this job's location? (yes/no checkbox)
 commute: False
 # Are you comfortable working in a remote environment? (yes/no checkbox)
 remote: True
 # Are you comfortable taking a drug in accordance with local/state laws? (yes/no checkbox)
 drugTest: True
 # Are you willing to complete an assessment? (yes/no checkbox)
 assessment: True
 # Have you completed the following level of education: DEGREE TYPE? (yes/no checkbox)
 degreeCompleted:
  - High School Diploma
  - Bachelor's Degree
  # - Associate's Degree
  - Master's Degree
  # - Master of Business Administration
  # - Doctor of Philosophy
  # - Doctor of Medicine
  # - Doctor of Law
 # Are you willing to undergo a background check, in accordance with local law/regulations?
 backgroundCheck: True

# ------------ Additional parameters: universityGpa ---------------
universityGpa: 4.0

# ------------ Additional parameters: salaryMinimum ---------------
salaryMinimum: 106000

# ------------ Additional parameters: languages ---------------
languages:
 english: Native or bilingual # None, Conversational, Professional, Native or bilingual

# ------------ Additional parameters: years of experience ---------------
# How many years of work experience do you have ...? (whole numbers only)
experience:
 # normal ones
 Accounting/Auditing: 0
 Administrative : 0
 Advertising : 0
 Analyst : 0
 Art/Creative: 0
 Business Development: 0
 Consulting: 0
 Customer Service: 0
 Distribution Design: 0
 Education: 0
 Engineering: 0
 Finance: 0
 General Business: 0
 Health Care Provider: 0
 Human Resources: 0
 Information Technology: 0
 Legal: 0
 Management: 0
 Manufacturing: 0
 Marketing: 0
 Public Relations: 0
 Purchasing: 0
 Product Management: 0
 Project Management: 0
 Production: 0
 Quality Assurance: 0
 Research: 0
 Sales: 0
 Science: 0
 Strategy/Planning: 0
 Supply Chain: 0
 Training: 0
 Writing/Editing: 0
 #python: 0
 #selenium: 0
 # default to put for any industry/skill that you did not list
 default: 0
 
# ------------ Additional parameters: personal info ---------------
personalInfo:
 First Name: FirstName
 Last Name: LastName
 Phone Country Code: Canada (+1) # See linkedin for your country code, must be exact
 Mobile Phone Number: 1234567890
 Street address: 123 Fake Street
 City: Red Deer, Alberta # Include the state/province as well!
 State: YourState
 Zip: YourZip/Postal
 Linkedin: https://www.linkedin.com/in/my-linkedin-profile
 Website: https://www.my-website.com # github/website is interchangeable here

# ------------ Additional parameters: USA employment crap ---------------
eeo:
 gender: None
 race: None
 vetran: None
 disability: None
 citizenship: yes
 clearance: no
```


## Execute

To run the bot, run the following in the command line:
```
python3 main.py
```

## Config.yaml Explanations
Just fill in your email and password for linkedin.
```yaml
email: email@domain.com
password: yourpassword
```

This prevents your computer from going to sleep so the bot can keep running when you are not using it. Set this to True if you want this disabled.
```yaml
disableAntiLock: False
```

Set this to True if you want to look for remote jobs only.
```yaml
remote: False
```

This is for what level of jobs you want the search to contain. You must choose at least one.
```yaml
experienceLevel:
 internship: False
 entry: True
 associate: False
 mid-senior level: False
 director: False
 executive: False
```

This is for what type of job you are looking for. You must choose at least one.
```yaml
jobTypes:
 full-time: True
 contract: False
 part-time: False
 temporary: False
 internship: False
 other: False
 volunteer: False
```

How far back you want to search. You must choose only one.
```yaml
date:
 all time: True
 month: False
 week: False
 24 hours: False
 ```

A list of positions you want to apply for. You must include at least one.
```yaml
positions:
 #- First position
 #- A second position
 #- A third position
 #- ...
 ```

A list of locations you are applying to. You must include at least one.
```yaml
locations:
 #- First location
 #- A second location
 #- A third location
 #- ...
 - Remote
 ```

How far out of the location you want your search to go. You can only input 0, 5, 10, 25, 50, 100 miles.
```yaml
distance: 25
 ```

This is the directory where all the job application stats will go to.
```yaml
outputFileDirectory: C:\Users\myDirectory\
 ```

A list of companies to not apply to.
```yaml
companyBlacklist:
 #- company
 #- company2
 ```

A list of words that will be used to skip over jobs with any of these words in there.
```yaml
titleBlacklist:
 #- word1
 #- word2
 ```

A path to your resume and cover letter.
```yaml
uploads:
 resume: C:\Users\myDirectory\Resume.pdf
 # Cover letter is optional
 #coverLetter: C:\Users\myDirectory\CoverLettter.pdf
 ```

Answer these questions with regards to the company you are applying to. 
For the degrees part uncomment which degrees you have, and do not add other ones since the linkedin questions are generic.
```yaml
# ------------ Additional parameters: checkboxes ---------------
checkboxes:
 # Do you have a valid driver's license? (yes/no checkbox)
 driversLicence: True
 # Will you now, or in the future, require sponsorship for employment visa status (e.g. H-1B visa status)? (yes/no checkbox)
 # This is relative to the location and your citizenship applying above, and same with legallyAuthorized.
 requireVisa: False
 # Are you legally authorized to work in COUNTRY? (yes/no checkbox)
 legallyAuthorized: True
 # We must fill this position urgently. Can you start immediately? (yes/no checkbox)
 urgentFill: True
 # Are you comfortable commuting to this job's location? (yes/no checkbox)
 commute: False
 # Are you comfortable working in a remote environment? (yes/no checkbox)
 remote: True
 # Are you comfortable taking a drug in accordance with local/state laws? (yes/no checkbox)
 drugTest: True
 # Are you willing to complete an assessment? (yes/no checkbox)
 assessment: True
 # Have you completed the following level of education: DEGREE TYPE? (yes/no checkbox)
 degreeCompleted:
  - High School Diploma
  - Bachelor's Degree
  #- Associate's Degree
  #- Master's Degree
  #- Master of Business Administration
  #- Doctor of Philosophy
  #- Doctor of Medicine
  #- Doctor of Law
 # Are you willing to undergo a background check, in accordance with local law/regulations?
 backgroundCheck: True
 ```

Input your university gpa. Must be a decimal value to one decimal point.
```yaml
# ------------ Additional parameters: universityGpa ---------------
universityGpa: 4.0
 ```

Input your minimum desired salary. Must be an integer (no decimal, comma, or currency symbol).
```yaml
# ------------ Additional parameters: salaryMinimum ---------------
salaryMinimum: 106000
 ```

List all your languages. You must put the proficiency as either: None, Conversational, Professional, Native or bilingual
```yaml
# ------------ Additional parameters: languages ---------------
languages:
 english: Native or bilingual # None, Conversational, Professional, Native or bilingual
 ```

Answer the following question for your experience in industries, tools and technologies. 
Things like programming languages, frameworks, etc.
The years of experience must be a whole number.
Fill in the default for experience you did not list (keep in mind if it's not zero, you will get your application seen more often).

CAVEAT: This is based on keywords in questions. If you put 'R' for experience with the programming language R, this will match all questions with the character 'r'.
```yaml
# ------------ Additional parameters: years of experience ---------------
# How many years of work experience do you have ...? (whole numbers only)
experience:
 # normal ones
 Accounting/Auditing: 0
 Administrative : 0
 Advertising : 0
 Analyst : 0
 Art/Creative: 0
 Business Development: 0
 Consulting: 0
 Customer Service: 0
 Distribution Design: 0
 Education: 0
 Engineering: 0
 Finance: 0
 General Business: 0
 Health Care Provider: 0
 Human Resources: 0
 Information Technology: 0
 Legal: 0
 Management: 0
 Manufacturing: 0
 Marketing: 0
 Public Relations: 0
 Purchasing: 0
 Product Management: 0
 Project Management: 0
 Production: 0
 Quality Assurance: 0
 Research: 0
 Sales: 0
 Science: 0
 Strategy/Planning: 0
 Supply Chain: 0
 Training: 0
 Writing/Editing: 0
 #python: 0
 #selenium: 0
 # default to put for any industry/skill that you did not list
 default: 0
  ```
Input your personal info. Include the state/province in the city name to not get the wrong city when choosing from a dropdown.
The phone country code needs to be exact for the one that is on linkedin.
The website is interchangeable for github/portfolio/website.
```yaml
# ------------ Additional parameters: personal info ---------------
personalInfo:
 First Name: FirstName
 Last Name: LastName
 Phone Country Code: Canada (+1) # See linkedin for your country code, must be exact according to the international platform, i.e. Italy (+39) not Italia (+39)
 Mobile Phone Number: 1234567890
 Street address: 123 Fake Street
 City: Red Deer, Alberta # Include the state/province as well!
 State: YourState
 Zip: YourZip/Postal
 Linkedin: https://www.linkedin.com/in/my-linkedin-profile
 Website: https://www.my-website.com # github/website is interchangeable here
  ```
This is unused at the moment. For the EEO the bot will try to decline to answer for everything.
```yaml
# ------------ Additional parameters: USA employment crap ---------------
eeo:
 gender: None
 race: None
 vetran: None
 disability: None
 citizenship: yes
 clearance: no
```

## Troubleshooting

If you are receiving 'file or directory' found errors, create a blank file with the specified name. For example:
```
touch unprepared_questions.csv
```
