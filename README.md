## FLASK BOILERPLATE CODE v0.0.1


This is a basic flask boilerplate to get started

All the basic packages with the implementation of security is installed and ready to go

``STEPS TO USE THE BOILERPLATE``

1.Create a virtual environment

2.Install all the dependencies 

3.Initialize the database(by default sqlite is given.But you can change it.For configuration you can browse the sqlalchemy website)

4.Do the migrations using the following commands

``flask db init``



```flask db migrate -m "__your message here__"```

``flask db upgrade``


5.Run the application using the command

``flask run``

The application will run on the default port 5000