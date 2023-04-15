# MPR-BE

Install Python and Django. Then you can run the server application:

```
python manage.py runserver
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
