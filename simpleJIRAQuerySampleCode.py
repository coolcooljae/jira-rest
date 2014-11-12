from jira.client import JIRA

JIRA_URL = "<your JIRA server URL>"
JIRA_USER = "<valid user name for the JIRA server>"
JIRA_PWD  = "<valid password for the JIRA server>"

# 1) first connect to JIRA server which requires a valid user name and a password
jira = JIRA({'server': JIRA_URL}, basic_auth=(JIRA_USER, JIRA_PWD))

# 2) execute a JIRA query
queryString = "<your JIRA query>" # this should run on regular browser
fieldListStr = 'issuekey,assignee'
queryResult = jira.search_issues(queryString, fields=fieldListStr, maxResults=100)

# 3) print query result
print("JIRA query returned ", len(queryResult), " entries")
for index, entry in enumerate(queryResult):
    print(entry.key + ": " + entry.fields.assignee.name)



