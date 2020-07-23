# remember the name

# the goal of this project is to see if there is some factor that makes police 
# shooting victims more likely to be remembered by the media.  The simple questions
# this notebook seeks to answer are: are police shootings of black Amerians less
# reported on than other racial groups?  How much?  Is this a case where a few are
# over-reported, and most under-reported?

# Step 1: Add a priority system for creating the data
#    We can only create a few inquiries at a time, so we are going to create a priority system
#    so that we can get the data we are most interested in doing first, and then move on to the other data.
#    Actually...let's do this first part in R...
# Step 2: Add columns based on the number of hits.  It may also be useful to get these numbers grouped by date.
#   Raw hits to date is easy.  More difficult would be that grouping.
#   If the articles come with their own date tags, we don't need to do repeated searches... Somewhat easier
#   How should we do these?  We could do first week, first month, first season, first year, and to-date
#   We'd also want a new feature on the number of days since the incident
#   One last option: if we save the responses from each incident,
#     then we can go back and do whatever kind of further analyses we want on the data.
#   For getting the data, we need for-loops with a try-catch for when we can no longer run the search.
#   If we are saving all of these in a folder, we can also check the folder for where we left off.
#       Concrete Steps:
#           1.  Add new feature for "UPDATED" so we can see when the last time the check was done
#           2.  Setup folder for incident .json files
#           3.  Setup algorithm to create unique file names.... actually, we have ID, so we can just use that
#           4.  Setup for-loop specifically for unarmed cases
#           5.  Setup for-loop for all other cases
# Step 3: Analysis
#   Will probably move to R for this part

import requests
import pandas as pd
import os

this_dir = os.path.dirname(os.path.realpath('__file__') )
target = os.path.join(this_dir, 'fatal_police_shootings.csv')
df = pd.read_csv(target, delimiter=',')

update_if_less_than = pd.to_datetime('2020-07-21')
today = pd.to_datetime('today')

df['UPDATED']   = ['1900-01-01'] * len(df)
df.UPDATED      = pd.to_datetime(df.UPDATED)


#df['ARMED_BIN'] =='unarmed'
#print(df)
## GOAL:  Get this working with dates for update
for i, ID in enumerate(df['ID']):
    fname   = 'cases/case_' + str(ID) + '.json'
    target  =  os.path.join(this_dir, fname)
    if df.UPDATED[i] < update_if_less_than:
        df.loc(i, 'UPDATED') = today
#    print(df.UPDATED > pd.to_datetime('1901-01-01') )
#    print(target)
#    print(df.loc[i,'UPDATED'])
#    print(df.loc[i,'ARMED_BIN'])

#print(df['UPDATED'][1])