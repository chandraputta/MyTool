
#Modification History
#v0.1 -- Added labels check condition for posts without label
import pyodbc 
import datetime
import Config
import requests
from Config import getDatabaseInfo
from Config import getTestAPIDetails
from Config import getJSeekerDetails

#Get SQL and Key details
SQLConnString,key= getDatabaseInfo()
cnxn = pyodbc.connect(SQLConnString)
cursor = cnxn.cursor()

#get APITest details
strAPITestBlogID,strApiTestPostsUrl= getTestAPIDetails()

#get Jseeker details
strJSeekerBlogID,strJSeekerPostsUrl=getJSeekerDetails()

#getdata from APITest
data = requests.get(strApiTestPostsUrl).json()

#get data from JSeeker
#data = requests.get(strJSeekerPostsUrl).json()

#loop through API, set values and insert data to DB
for i in data['items']:
	strpostURL = i['url']
	strUpdatedDate = i['updated']
	strSelfPostLink = i['selfLink']
	strPostCommentsCount = i['replies']['totalItems']
	strPostCommentsLink = i['replies']['selfLink']
	bigintBlogID = i['blog']['id']
	strAuthorImage = i['author']['image']
	intAuthorID = i['author']['id']
	strAuthorDisplayName = i['author']['displayName']
	strAuthorURL = i['author']['url']
	strPostID = i['id']
	strPostTitle = i['title']
	dtPostPubDate = i['published']
	strPostContent = i['content']
	strKind = i['kind']
	if 'labels' in i:
		j=0
		intLabelCount = len(i['labels'])
		#print(i['title'])
		#print("Label count is" + str(intLabelCount))
		while j < intLabelCount:
			strLabel = "" 
			strLabel = i['labels'][j]
			#print(strLabel)
			cursor.execute("insert into blogPostLabels ([blogPostID],[Label]) values (?,?)",strPostID,strLabel)
			cursor.commit()
			j+=1
	else:
		cursor.execute("insert into blogPostLabels ([blogPostID],[Label]) values (?,?)",strPostID,"")
		cursor.commit()

	cursor.execute("insert into blogPosts ([postURL],[updatedDate],[selfPostLink],[postCommentsCount],[postCommentsLink],[blogID],[postID],[postTitle],[postPubDate],[postContent],[Kind]) values (?,?,?,?,?,?,?,?,?,?,?)",strpostURL,strUpdatedDate,strSelfPostLink,strPostCommentsCount,strPostCommentsLink,bigintBlogID,strPostID,strPostTitle,dtPostPubDate,strPostContent,strKind)

cursor.commit()

# #Fetchdata for testing only
# cursor.execute("select * from blogPosts")
# for row in cursor:
    # print('row = %r' % (row,))
    
    
