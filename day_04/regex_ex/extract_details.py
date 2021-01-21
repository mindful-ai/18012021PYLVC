import re
EOF = ''
# Read the file as a text

f = open(r"C:\Users\Purushotham\Desktop\oracle\day_05\regex_ex\resume.txt", "r")
content = f.read()
f.close()
# Patterns

jobid = r'#\d{6}'
email = r"(\w+[.-_]){,3}\w+@\w+\.(com|org|in)" # raj.kumar.avss.009@gmail.com, raj.kumar.009#gmail, raj.kumar@gmail.com, raj@gmail.com
phone = r"\d{3}-?\d{3}-?\d{4}"
linkedin = r"(linkedin.com)/\w+/(\w+[-_.]){,5}\w+"
name = r"(Sincerely,?)\n+(?P<Name>\w+\s\w+)"

ipaddr = r"([0-9]{1,3}\.){3}[0-9]{1,3}" # Deepika
experience = r"(?P<experience>[0-9]{,2}\+\s(years?|months?))[\w\s]*(experience)"

# Apply the patterns and store what ever is extracted



m = re.search(jobid, content)
if m:
    print('JOBID     : ', m.group())

m = re.search(email, content)
if m:
    print('EMAIL     : ', m.group())

m = re.search(phone, content)
if m:
    print('PHONE     : ', m.group())

m = re.search(linkedin, content)
if m:
    print('LINKEDIN  : ', m.group())

m = re.search(name, content)
if m:
    print('NAME      : ', m.groupdict()['Name'])

m = re.search(experience, content)
if m:
    print('EXPERIENCE      : ', m.groupdict()['experience'])

m = re.search(ipaddr, content)
if m:
    print('IP ADDRESS      : ', m.group())