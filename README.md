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

url: <http://localhost:8000>


### Open gates:
- PATH - REQUEST TYPE - RETURN
- user/<str:pk> - GET - LIST<USER>
- login - POST<email, password> - USER
- logout - GET - HTTP OK
- users - GET - LIST<USER>
- projects - GET - LIST<PROJECT>
- project/<str:pk> - GET - LIST<PROJECT>
- user_risks/<str:pk> - GET - LIST<RISK>
- project_risks/<str:pk> - GET - LIST<RISK>
- risk/<str:pk> - GET - LIST<RISK>
- create_project - POST<PROJECT> - LIST<PROJECT>
- create_risk - POST<RISK> - LIST<RISK> 
- update_risk - POST<RISK> - LIST<RISK>
- update_project - POST<PROJECT> - LIST<PROJECT>
- fake - ANY - LIST<USER> - creates new user with email "test" and password "test" to create normal user tou can use 
funcion create_fake_user in MPR-BE/app/views.py
- logged - ANY - 200 if user is logged 403 otherwise
