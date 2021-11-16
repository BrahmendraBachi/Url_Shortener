# Url_Shortener
This is a simple flask app which takes an URL and shortens it. This shortened verion of the URL redirects to the user to the long URL.

For each long URL given by the user the application randomly generates an alphabetical combination which redirects to the long URL.

This executed flask app only works on local database server where you need to clone it to desktop pycharm application.

Create a new directory **templates** under the Project folder and save **base.html** under this **templates** directory

After completing above procedure, Run the **app.py** in the pycharm compiler which you will get a local IP adress **http://127.0.0.1:5000/** which remaining process will work under this IP adress by clicking on it.

This IP adress directly redirects to the **base.html** file and which we have already called this html file in our **home** function in **app.py**

There you can able to see a input box which you need to give your **long url** to shorten it

After Entering(or copying) your link to the input box click on **submit** button to generate a short url which genetares a **http://127.0.0.1:5000/{3 letter random code}**

This Generated short url you can directly click on it or you can copy it to paste on any other browser to run

This short url will directly redirects to the long url which we have already stored the information about this generated 3 digit random code in the local database(urls.db)

This redirection process executes in function in our app called **Redirection** and every time it redirects the count will be incremented and updated in the database to display the no of times it has been visited.

The data base for the long and short urls will create in the **Urls(db.Model)** function in the app.py

If the user gives the same long URL, then this app checks whether the long URL has already been there on the database and returns the same short URL.

If not then the database add the long URL and respected 3 letter random code.

