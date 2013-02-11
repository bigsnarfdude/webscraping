#!/usr/bin/env python

'''
Scrape the public profiles of linkedIn users
'''


import requests
from BeautifulSoup import BeautifulSoup


resume = {}
links  = []
link   = "http://www.linkedin.com/pub/vincent-ohprecio/39/a60/59a"
link1  = "http://ca.linkedin.com/in/lhildebrandt"


def _collect(hashkey, domnode, htmlclass):
    '''
    Collect fields
    '''
    resume[hashkey] = soup.find(domnode, {"class":htmlclass}).getText()

def _collect_multiple(domnode, htmlclass, hashkey, subnode, *at):
    '''
    Collect fields with multiple attributes
    '''
    section = soup.find(domnode, {"class":htmlclass})
    if section:
        counter = 0
        resume[hashkey] = dict()
        for subsection in section.findAll(subnode):
            counter += 1
            if at:
                resume[hashkey][counter] = str(subsection.getText()).replace('at', ' at ')
            else:
                resume[hashkey][counter] = subsection.getText()

def scrape():
 
    _collect('fname', 'span', 'given-name')
    _collect('lname', 'span', 'family-name')
    _collect('locality', 'span', 'locality')
    _collect('industry', 'dd', 'industry')
    resume['current'] = str(soup.find("ul", {"class":"current"}).findAll("li")[0].getText()).replace('at', ' at ') 
    _collect_multiple('dd', 'summary-past', 'past', 'li', 'at')
    _collect_multiple('dd', 'summary-education', 'education', 'li')
    _collect_multiple('ol', 'skills', 'skills', 'li')
    projects = soup.find(id="profile-projects")
    if projects:
        counter = 0
        resume['project-descriptions'] = {}
        for project in projects.findAll('p'):
            counter += 1
            resume['project-descriptions'][counter] = project.getText()

page = requests.get(link)
soup = BeautifulSoup(page.content, convertEntities=BeautifulSoup.HTML_ENTITIES)
soup_main = soup.find(id="main")
soup_summary = soup.find(id="profile-summary")
resume['profile_summary'] = {}
count = 0
try:
    for item in soup_summary.findAll('p'):
        count += 1
        resume['profile_summary'][count] = soup_summary.getText()
except:
    pass


scrape()
print resume








import redisco
import redis
import cPickle as pickle
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)

vincent = pickle.dumps(resume)
print vincent
print "****************************************************************"
r.set("vincent", vincent)
print "saved vincent"
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print pickle.loads(r.get("lisa"))
print pickle.loads(r.get("vincent"))

