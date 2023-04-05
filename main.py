from bs4 import BeautifulSoup
import requests

web = requests.get ('https://realpython.github.io/fake-jobs/')
#This is the link we use to retrieve the data

soup = BeautifulSoup(web.content, 'html.parser')

job = []
company = []
date = []
print("Available Jobs:\n")

for link in soup.find_all('h2'): 
  print(link.text)
  job.append(link.text)


print("\n\nCompany:\n")
for link in soup.find_all('h3'): 
  print(link.text)
  company.append(link.text)

# print("Job Location:")
# for link in soup.find_all('p'): 
#   print(link.text)

print("\n\nDate Posted:\n")
  
for link in soup.find_all('time'): 
  print(link.text)
  date.append(link.text)

for j in company:
  i = 0
  print("Job Title: " + job[i] + " Company: " +company[i] + " Date Posted: " + date[i] )
  i+=1

print("\n\nSorted Jobs!")
job.sort()
for i in job:
  print(i)