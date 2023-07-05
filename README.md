# Web Server (Angular+Django+Postgresql)
<img src="https://bezkoder.com/wp-content/uploads/2020/12/django-angular-postgresql-example-crud-architecture.png" alt="Postgresql" width="400"  style="display:block; margin:auto;" /><img src="https://pretius.com/wp-content/uploads/2023/02/Keycloak.png" alt="Postgresql" width="250"/>

Environment:
1. Ubuntu 20.04 or 22.04
	If you have different OS, please download VirtualBox or other Virtual machines to mount a VM instance of Ubunut 20.04 or 22.04.
2. Docker
	You need to package all your source codes into the docker image.
3. Docker compose or docker swarm
	You need to use docker swarm or docker-compose to cluster your source code and database as a service.

## ORM/SQL Database(Postgresql):
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/1200px-Postgresql_elephant.svg.png" alt="Postgresql" width="250"/>

Basic:
* 1. Create model user with fields username/password/address.  The password should not be stored in plain-text.
* 2. Create functions to create, read, update, delete, and list the model user in database.

Bonus:
* 3. Use ORM instead of SQL statement to access the database.
* 4. Create model role with fields rolename/permission/description and many-to-many relation between user and role.
* 5. Implement Optimistic Lock on the user and the role.
* 6. Use transaction for the database operation.


## Backend(Django):
<img src="https://www.fullstackpython.com/img/logos/django.png" alt="Django" width="250"/>

Basic:
* 7. Create a Restful API with swagger ui testbed/auto-generated Restful API document.
* 8. Enable HTTPS for security.
* 9. Create an API for the user to sign up (enroll). There are 3 fields for the user: username/password/address.
* 10. Create an API for the user to login. After login, the client should receive a token. Except signup and login, all api requests should put the HTTP token in the header to verify the identity.
* 11. Create an API to read the user.
* 12. Create an API to update the user.
* 13. Create an API to delete the user.
* 14. Create an API to list the users on condition and use query parameter for paging, sorting, and searching.

Bonus:
* 15. Create APIs to create, read, update, delete, and list the role. There are 3 fields for the role: rolename/permission/description. Besides, the role will have 1 additional field (users) to describe the users who have this role. The user and the role are many-to-many relation. 
* 16. Modify APIs to create, read, update, delete, and list users. So the additional field (roles) is used.
* 17. Enable security for CSRF.
* 18. Enable security for XSS.
* 19. Create an websocket for the front-end to communicate bi-directionally to the backend. Every 1 minutes the backend will send a message "is still alive?" to the fronend and the frontend answer "alive" to backend.
* 20. Create an API to launch 10 processes simultaneously to update the field "description" in the role to test whether or not Optimistic Lock(5.) works. Collect the success and error messages and return as the log. 
* 21. Create an API to launch 10 processes simultaneously to update the fields in the user and the role to test whether or not Transaction works. Collect the success and error messages and return as the log.


## Frontend(Angular):
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Angular_full_color_logo.svg/1200px-Angular_full_color_logo.svg.png" alt="Angular" width="250"/>

Basic:
* 22. Create a form page to sign up (enroll).
* 23. Create a login page. User could login with username and password.
* 24. Create a menu on the left or on the top to access the first level page (25./27. for basic, and 30./31. for bonus).
* 25. Create a list page. User could see the list of user. The list should have paging, sorting, and searching. There 1 button to create the user and 2 buttons in each row to update and delete the user. 
* 26. Create a form page to create or update user. It could go back to the list page.

Bonus:
* 27. Create the form page and the list page for the role. In the role create/update form page, the user could be added to or deleted from the role. The role list page shows the users who own the roles.
* 28. Modify the form page and the list page for the role. In the user create/update form page, the role could be added to or deleted from the user. The user list page shows the roles belongs to users.
* 29. Create an websocket to communicate bi-directionally to the backend. Every 1 minutes the backend will send a message "is still alive?" to the fronend and the frontend answer "alive" to backend. It started after login and stopped after the login token is expired.
* 30. Create a page to test Optimistic Lock(20.). Provide a button to trigger the API and show the log on the page.
* 31. Create a page to test Transaction(21.). Provide a button to trigger the API and show the log on the page.


## Deployment:

Basic:
* 32. Build a Docker image to run your app.
* 33. Use Docker swarm or docker compose to cluster your app and database as a service.
* 34. The app should use https://localhost:8443/ to access and you should provide the url for swagger ui testbed and auto-generated Restful API document.
* 35. Use Makefile or shell script to build the image (32.) and run the app (34.). Write a document on how to use them.

Bonus:
* 35. Monut the HTTPS certificates on the host rather than package HTTPS certificates into the docker image.
* 36. Secure the docker image. Don't use root user.

