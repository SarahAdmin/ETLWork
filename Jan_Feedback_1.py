import pandas as pd 
JanDF = pd.read_excel('Jan Feedback.xlsx')
columns_TakeitOff1 = ['Anonymized Contact ID', 'Posting ID','Current Stage ID','Survey Id', 'Survey Name',
       'Survey Location Type','Posting Hiring Manager', 'Candidate Selected Location',
       'Stage - New lead', 'Stage - Reached out', 'Stage - Responded',
       'Stage - New applicant', 'Stage - Under review',
       'Stage - Recruiter Screen', 'Stage - Hiring Manager Screen',
       'Stage - 1st Round', 'Stage - 2nd Round', 'Stage - Decision',
       'Stage - Offer',
       'How satisfied were you with the ease of the application process? - 513b2b55-b818-4f03-bf6f-e82b180c9e60',
       'How satisfied were you with the interview materials you received? - 4158aafc-ce92-4d35-930f-2f5451455a4d',
       'How satisfied are you with your interviews with the Hiring Manager and Team? - 605b085d-5bba-4668-babc-17dc8304e06c',
       'How satisfied were you with the interview feedback you received? - e30211c6-d32d-4f89-95fc-dfb91bb47033',
       'How satisfied are you with the way you were treated? - 05c18285-2750-479f-8afc-d560b66f552c',
       'What suggestions would you make to improve our interview process? - 21866cc4-7d8f-47da-97df-9efdfcbe083d',
       'Overall, how satisfied were you with your interviewing experience? - 693b0a81-d4e7-40a2-9135-7fc38fa43eaf',
       'Do you have any thoughts or comments that you would like to share? - a611bc41-fd5f-4f91-a277-3b0a260c7401',
       'How satisfied were you with your Screening call? - de09e7f8-4e8c-498d-9ccb-237788b735d0',
       'How satisfied were you with our communication during the recruiting process? - e8c5e9ae-38de-4acb-855c-8d18039b1f5c']
JanDF1 = JanDF.drop(columns_TakeitOff1,axis=1)
JanDF = JanDF1.where(JanDF1['Location']== 'United Kingdom').dropna()
print(JanDF.to_string())
