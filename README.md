# MPR-BE

Install Python and Django. It should be possible to open this project in PyCharm, just open it and add python3
interpreter that has Django installed within. Then you can run the server application:

```
python manage.py runserver
```

For creating database use:
```
python manage.py makemigrations
python manage.py migrate 
```

-

For inserting example data to local db use:
```
python3 manage.py insert_data
```
It creates user (email=user1, pass=Password1) and project with risks

For inserting data in beta version use:
```
python3 manage.py beta
```
It creates users (admin@mpr.cz, dvorak@mpr.cz, jirasek@mpr.cz), password is same: "Password1"

To delete all data in the database use:
```
python3 manage.py clear
```

To create users use:
```
python3 manage.py create_users
```
It creates users (admin@mpr.cz, dvorak@mpr.cz, jirasek@mpr.cz, dan@mpr.cz), password is same: "Password1"

app is running at <http://localhost:8000>


### Open gates:
- PATH - REQUEST TYPE - RETURN
- user/<str:pk> - GET - LIST<USER>
- login - POST<email, password> - USER
- logout - GET - HTTP OK
- users - GET - LIST<USER>
- projects - GET - LIST<PROJECT>
- risk_categories - GET - LIST<RISK_CATEGORY>
- project/<str:pk> - GET - LIST<PROJECT>
- project_roles/<str:pk> - GET - LIST<USER_PROJECT>
- user_risks/<str:pk> - GET - LIST<RISK>
- project_risks/<str:pk> - GET - LIST<RISK>
- risk/<str:pk> - GET - LIST<RISK>
- create_project - POST<PROJECT> - LIST<PROJECT>
- create_project_role - POST<USER_PROJECT> - LIST<USER_PROJECT>
- create_risk - POST<RISK> - LIST<RISK> 
- update_risk - POST<RISK> - LIST<RISK>
- update_project - POST<PROJECT> - LIST<PROJECT>
- update_project_role - POST<USER_PROJECT> - LIST<USER_PROJECT>

- fake - ANY - LIST<USER> - creates new user with email "test" and password "test" to create normal user tou can use 
funcion create_fake_user in MPR-BE/app/views.py
- logged - ANY - 200 if user is logged 403 otherwise
- create_risk_category - POST<RISK_CATEGORY> - LIST<RISK_CATEGORY>
- update_risk_category - POST<RISK_CATEGORY> - LIST<RISK_CATEGORY>
- delete_risk_category/<str:pk> - GET - OK
- delete_project/<str:pk> - GET - OK
- delete_risk/<str:pk> - GET - OK
- update_user - POST<USER> - LIST<USER>
- delete_user/<str:pk>/ - GET - OK
- all_risks - GET - LIST<RISK>
- project_user_role - POST<user_pk,project_pk> - List<UserProject>
