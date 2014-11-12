from JIRAQueryRest import JIRAQueryRest

############################################################
# main
############################################################

jira = JIRAQueryRest()

jiraField2Query = 'issuekey,status,priority'
jiraQuery = '<replace with your own query>'
results = jira.query(jiraQuery, jiraField2Query)

for entry in results:
    print (entry.key + ": status= " + entry.fields.status.name + ", priority= " + entry.fields.priority.name)



