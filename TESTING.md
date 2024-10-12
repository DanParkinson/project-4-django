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

## Connecting CSS and JS