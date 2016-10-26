# ReminderAPI
# Reminders API Project Spec


## Overview
This project tasks you with building a reminders application that synchronizes its data in the cloud. The goal is to create a useful application that combines everything you’ve learned in the Back-end Web: API Services course. Feel free to comment on anything here for clarification. (Highlight text and then access Insert => Comment in the Google Docs menu.)


This document specifies the API for a back-end web service with enough detail for a developer to build the API service to spec and allow other developers to build front-end web and mobile client applications that connect to the back-end. It is structured into several milestones to allow for and promote iterative test-driven development to ensure the API service follows the spec. Data should be persisted to disk using the database of your choice.


### Requests and Responses
HTTP request and response body data should be serialized in JSON format and specify the Content-Type and Accept headers as "application/json". The service should respond with appropriate HTTP status codes, as well as appropriate error messages as necessary. All fields are required in POST and PUT request body data unless otherwise indicated as optional. Fields should be validated appropriately (no empty strings, dates should be formatted correctly).


### Milestone 1: Tasks
Features
..* Tasks can be created, listed, and destroyed.
..* Completed tasks are destroyed instead of stored.


Data Models
Tasks have 2 fields: id and text


Routes and Actions
POST   /tasks
create new task with text field from request body
GET    /tasks
list all tasks
GET    /tasks/<id>
show task with id
DELETE /tasks/<id>
destroy task with id



### Milestone 2: Task Lists
Features
Tasks now have a completed flag.
Tasks are now organized into lists.
Lists can be created, listed, and destroyed.


Data Models
Lists have 2 fields: id and title
Tasks now have 4 fields: id, list_id, text, and completed


Routes and Actions
POST   /lists
create new list with title field from request body
GET    /lists
list all lists (do not show tasks within each list)
GET    /lists/<list_id>
show list with list_id
PUT    /lists/<list_id>
update list with list_id with title field from request body
DELETE /lists/<list_id>
destroy list with list_id
POST   /lists/<list_id>/tasks
create new task with text field from request body in list with list_id
tasks are incomplete by default (completed is set to false)
GET    /lists/<list_id>/tasks
list all tasks in list with list_id
GET    /lists/<list_id>/tasks/<task_id>
show task with task_id
PUT    /lists/<list_id>/tasks/<task_id>
update task with task_id with text and completed fields from request body
DELETE /lists/<idlist_idtasks/<task_id>
destroy task with task_id



### Milestone 3: Users and Authentication
Features
Tasks and lists now have a user account associated with each.
Users can be created and destroyed.
Most routes require user authentication.


Data Models
Users have 2 fields: id and name
Lists now have 3 fields: id, user_id, and title
Tasks now have 5 fields: id, user_id, list_id, text, and completed


Routes and Actions
POST   /users
create new user with name field from request body
does not require authentication (anyone can create a new account)
DELETE /users/<user_id>
destroy user with user_id
requires authentication (only the owner can destroy their account)
All other routes are unchanged except that they all now require user authentication and should only access or modify tasks and lists associated with the authenticated user.


Authentication and Authorization
If the request does not contain any user authentication info or user authentication fails, respond with HTTP status code 401 Unauthorized.
If user authentication succeeds but the request is to access another user’s tasks or lists, respond with HTTP status code 403 Forbidden.



### Milestone 4: Due Dates and Text Messages
Features
Tasks now have an optional due date. User are sent text message reminders to alert them of tasks when their due dates pass.


Data Models
Users now have 3 fields: id, name, and phone_number
Tasks now have 6 fields: id, user_id, list_id, text, completed, and date_due


Routes and Actions
POST   /lists/<list_id>/tasks
create new task with text and (optional) date_due fields from request body in list with list_id
PUT    /lists/<list_id>/tasks/<task_id>
update task with task_id with text, completed, and (optional) date_due fields from request body
All other routes are unchanged.
