"""
Cases to test navigation from page to page
"""
from bs4 import BeautifulSoup
from django.test import TestCase

baseUrl = '/manager/'

_testCases = (
    ('Homepage', baseUrl, baseUrl + 'spaces/add/'),
    ('Homepage', baseUrl, baseUrl + 'spaces/5070/'),
    ('Homepage', baseUrl, '/detai/1/'),
    ('Homepage', baseUrl, 'mailto:help@uw.edu'),
    ('Add page', 'spaces/add/', baseUrl),
    ('Edit page', 'spaces/5070/', baseUrl)
)

def _makeTestFunc(name, path, reference, issue=None):
    """Returns a function that tests that each page necessary
        navigation links as specified in spec"""

    def _testFunc(self):
        #Makes the soup of the HTML of the desired page to be parsed through
        soup = self.makeSoup(path)       
        self.assertElementExists(soup, 'a', href=reference)

    # Makes a test function, with the page passed as the name.
    _testFunc.__name__ = 'test_page_' + name.replace(' ', '_').lower()

    # Makes a help comment about the url status
    doc = 'Page "%s" should contain %s' % (name, reference)

    # Connects the help comment with an issue number in JIRA
    if issue is not None:
        doc += ' (%s)' % issue
    _testFunc.__doc__ = doc

    return _testFunc

class NavigationTests(TestCase):
    """Use a list of URLs and expected status codes to ensure every
        page returns the expected code."""

    def makeSoup(self, link):
        webResponse = self.client.get(link)
        soup = BeautifulSoup(webResponse.content, "html.parser")
        return soup

    # Runs all test cases
    for case in _testCases:
        # Takes all the arguments and make test functions
        _testFunc = _makeTestFunc(*case)
        # Sets the names for the test functions
        name = _testFunc.__name__
        vars()[name] = _testFunc
    
    # Deletes variables so they don't leak into help documentation
    del case, name, _testFunc