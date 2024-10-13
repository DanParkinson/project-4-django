# TESTING

A variety of exploratory tests were performed throughout the project.

## MANUAL TESTING

Getting the live deployed site working. This is well documented in the latter sections of [DEPLOYMENT.md](DEPLOYMENT.md)

## Checking website loads hompage

<details>
<summary>Click me</summary>

Add the following code to the home/views.py file. This tells the server to display "This is the homepage"

![01](docs/testing/01-load-home-page.png)

Add the following code to the elite_cuisine/urls.py file.

![env secret key](docs/testing/02-load-home-page.png)

Add the following code to the elite_cuisine/settings.py file to installed apps.

![env secret key](docs/testing/03-load-home-page.png)

Use command python3 manage.py runserver to check the home app is linked correctly.

![env secret key](docs/testing/04-load-home-page.png)

</details>

## Super User

<details>
<summary>Click me</summary>

When i originally tried to login as a superuser i recieved this error.

![Error](docs/testing/admin-test-01.png)

After using code institute support i had forgotten to add.

![CSFR](docs/testing/admin-test-02.png)

Admin login now functions correctly.

![Admin Page](docs/testing/admin-test-03.png)

</details>

## Creating Templates 

<details>
<summary>Click me</summary>

Create a top level directory to include your templates 

![Templates](docs/testing/templates-01.png)

connect the templates directory to *elite/settings.py*

![Templates](docs/testing/templates-02.png)

![Templates](docs/testing/templates-03.png)

Once the templates partials are populated. The server looks like this

![Templates](docs/testing/templates-04.png)

</details>

## Connecting CSS and JS

<details>
<summary>Click me</summary>

Connect the static directory to *elite/settings.py*.

![CSS](docs/testing/style01.png)

Create you style.css as shown at the top level.

![CSS](docs/testing/style02.png)

Edit head.html to load sytle sheet.

![CSS](docs/testing/style03.png)

I initally recieved the error below. After chaging *STATIC_URL = '/static/'* in elite/setting.py the style sheet connected.

![CSS](docs/testing/style04.png)

Server with backgorund colour.

![CSS](docs/testing/style05.png)

Create script.js in static directory.

![JS](docs/heroku_deployment/24-js.png)

Connect script.js to base.html.

![JS](docs/heroku_deployment/25-base.html.png)

Check server loads message in developer tools.

![JS](docs/heroku_deployment/26-jsmessage.png)

</details>

## Reservations app 

<details>
<summary>Click me</summary>

First I created the form to be able to submit a reservation and a success page

![Reservation form](docs/testing/reservations01.png)

![Success page](docs/testing/reservations02.png)

Now to create the link to the database. 

![Reservations in Admin page](docs/testing/reservations03.png)

And to style the admin display so it is clearer

![Saved reservation](docs/testing/reservations04.png)

</details>