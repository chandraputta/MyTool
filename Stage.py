#loop through API, set values and insert data to DB
for i in data['items']:
   # print(i['title'])
	strpostURL = i['url']
	strUpdatedDate = i['updated']
	strSelfPostLink = i['selfLink']
	strPostCommentsCount = i['replies.totalItems']
	strPostCommentsLink = i['replies.selfLink']
	bigintBlogID = i['blog.id']
	strAuthorImage = i['author.image']
	intAuthorID = i['author.id']
	strAuthorDisplayName = i['author.displayName']
	strAuthorURL = i['author.url']
	strPostID = i['id']
	strPostTitle = i['title']
	dtPostPubDate = i['published']
	strPostContent = i['content']
	strPostLabel1 = i['labels[0]']
	strPostLabel2 = i['labels[1]']
	strPostLabel3 = i['labels[2]']
	strPostLabel4 = i['labels[3]']
	strKind = i['kind']
	
	cursor.execute("insert into blogPosts (pubDate,title) values (?,?)",pubDate,postTitle)
	#you can move commit statement here as for loop should work only on indentation
	
	
	[postURL] [varchar](500) NULL,
	[updatedDate] [datetime2](7) NULL,
	[selfPostLink] [varchar](100) NULL,
	postCommentsCount int,
	postCommentsLink varchar(100) NULL,
	blogID bigint null,
	authorImage varchar(200) null,
	authorID bigint null,
	authorDisplayName varchar(100),
	authorBloggerURL varchar(100),
	[postID] bigint not null,
	[postTitle] [varchar](200) NULL,
	[postPubDate] [datetime2](7) NULL,
	postContent nvarchar(max),
	postLabel1 varchar(50) null,
	postLabel2 varchar(50) null,
	postLabel3 varchar(50) null,
	postLabel4 varchar(50) null,
	Kind varchar(20) null,




CREATE TABLE [dbo].[blogPost](
   	[ID] [int] IDENTITY(1,1) NOT NULL,
	[postURL] [varchar](500) NULL,
	[updatedDate] [datetime2](7) NULL,
	[selfPostLink] [varchar](100) NULL,
	postCommentsCount int,
	postCommentsLink varchar(100) NULL,
	blogID bigint null,
	authorImage varchar(200) null,
	authorID bigint null,
	authorDisplayName varchar(100),
	authorBloggerURL varchar(100),
	[postID] bigint not null,
	[postTitle] [varchar](200) NULL,
	[postPubDate] [datetime2](7) NULL,
	postContent nvarchar(max),
	postLabel1 varchar(50) null,
	postLabel2 varchar(50) null,
	postLabel3 varchar(50) null,
	Kind varchar(20) null
	)
