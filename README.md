# GIZ Task 2 - Headless CMS

Task resolution process:

* Fork the repo
* Clone the forked repo to your local machine
* Resolve the task
* Commit your solution
* Push to GitHub
* create a pull request


# Task 2:

## create the following API endpoints

This is a Headless CMS, where you have to CRUD (Create, Read, Update, and Delete)
blog posts, you have to implement the task using files instead of database access.

Each endpoint should serve only one method, please read the note below and follow
the instructions.

You can use any of the methods in utils.py, however you should implement the 
endpoint on your own.

You have to set up NinjaAPI object, add routers to controllers.py, and 
as a bonus for extra points, you should implement the DELETE method.

'posts' directory is where you should save/update and create posts, each file
is a markdown file where the filename is the title of the post and the file content
is the content of the post. Each file represents a single post. A sample of two files
(two blog posts) are there for your reference.

```bash
# to list all posts
GET /posts

# to retrieve a certain post
GET /posts/{title}

# to create a new post
POST /posts

# to update a certain post
PUT /posts/{title}
```

bonus:

```bash
# to delete a certain post
DELETE /posts/{title}
```


### Note
* you can utilize any third party library or package
* and you should use the included utils.py
