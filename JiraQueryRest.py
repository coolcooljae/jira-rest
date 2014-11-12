from jira.client import JIRA

class JiraQueryRest:

    jira = None  # JIRA instance to use
    JIRA_SERVER_URL = "<your JIRA server URL>"
    JIRA_USER = "<valid user name for the JIRA server>"
    JIRA_PWD  = "<valid password for the JIRA server>"


    ############################################################
    def __init__(self):
        self.connect()


    ############################################################
    # open a connection to the JIRA server
    ############################################################
    def connect(self):
        # return if connection is already made
        if self.jira:
            return

        # make a new connection
        self.jira = JIRA ({'server':self.JIRA_SERVER_URL}, basic_auth=(self.JIRA_USER, self.JIRA_PWD))


    ############################################################
    # query JIRA with a given query string and field list
    # fixed max result size as 999
    # return results
    #
    # look at http://jira-python.readthedocs.org/en/latest/ for all fields
    ############################################################
    def query(self, queryString, fieldList):
        return self.jira.search_issues(queryString, fields=fieldList, maxResults=999)
