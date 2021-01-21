import re
EOF = ''
# Read the file as a text

f = open( "resume.txt", "r" )
content = f.read()
f.close()
# Patterns

jobid = r"#\d{6}"
email = r"(\w+[.-_]){0,}\w+@\w+\.(com|in|org)"
phone = r"\b\d{3}-\d{3}-\d{4}\b"
linkedin = r"linkedin.com(/\w+)(/(\w+-)+)\w+"
name = r"([Ff]aithfully|[Ss]incerely)(,)?\s(?P<Name>\w+\s\w+)"

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