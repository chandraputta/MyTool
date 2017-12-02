#Connect to Target DB
import pyodbc 
import datetime
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=LDW6ZSC2\SQL2012;PORT=1433;DATABASE=MyWork;UID=PythonUser;PWD=myP@ssword')
#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=LDW6ZSC2\SQL2012;PORT=1433;DATABASE=MyWork;UID=LDW6ZSC2\chan3069;Trusted_Connection=yes;')
cursor = cnxn.cursor()

#GetAPI
import requests
data = requests.get("https://www.googleapis.com/blogger/v3/blogs/3869481774856968139/posts/?key=AIzaSyA0UzzGOdG0wOWv7PSQZsrfeJQp4lVL2vk").json()
# posts = data.items[]
#print(data);

#loop through API, set values and insert data to DB
for i in data['items']:
   # print(i['title'])
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
	#strPostLabel1 = i['labels'][0]
	#strPostLabel2 = i['labels'][1]
	#strPostLabel3 = i['labels[2]']
	#strPostLabel4 = i['labels[3]']
	strKind = i['kind']
	# j=0
	# intLabelCount = len(i['labels'])
	# print('j is' + str(j))
	# print(intLabelCount)
	# while j <= intLabelCount: 
		# # print(i['title'])
		# print(i['labels'][j])
		# j=j+1
	j=0
	intLabelCount = len(i['labels'])
	while j < intLabelCount:
		strLabel = "" 
		#print(i['title'])
		#print(i['labels'][j])
		strLabel = i['labels'][j]
		print(strLabel)
		cursor.execute("insert into blogPostLabels ([blogPostID],[Label]) values (?,?)",strPostID,strLabel)
		j+=1
	cursor.execute("insert into blogPosts ([postURL],[updatedDate],[selfPostLink],[postCommentsCount],[postCommentsLink],[blogID],[postID],[postTitle],[postPubDate],[postContent],[Kind]) values (?,?,?,?,?,?,?,?,?,?,?)",strpostURL,strUpdatedDate,strSelfPostLink,strPostCommentsCount,strPostCommentsLink,bigintBlogID,strPostID,strPostTitle,dtPostPubDate,strPostContent,strKind)
	#you can move commit statement here as for loop should work only on indentation

# #insertdata
# #cursor.execute("insert into blogPosts (title) values (?)",blogTitle)

cursor.commit()

# #Fetchdata for testing only
# cursor.execute("select * from blogPosts")
# for row in cursor:
    # print('row = %r' % (row,))
    
    
