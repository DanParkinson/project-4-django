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

### Testing reservation inputs 

multiple tests have been performed to check the reservations form works correctly.

- Phone number has to be numeric *The letter e can be entered into the IntergerField fo some reason. Maybe because e is a number *
- Date starts at todays date.
- time intervals are set to every 15 minutes
- Number of people is capped betweeen 1-8
- Email has to be an email because of EmailField

### Testing double booking 

THIS WILL BE DONE AT A LATER DATE.

</details>

## Authentication 

<details>
<summary>Click me</summary>

Check allauth working with nav links. Allauth did the hard work for signup/login/logout. Just had to configure navbar.html with Django templates to check authentication. A test account was created to check it worked.

 Not logged in shows this view:

![Not authenticated view](docs/testing/authentication01.png)

 signing up shows:

![Not authenticated view sign up](docs/testing/authentication02.png)

 Logged in shows:

![authenticated view](docs/testing/authentication03.png)

To make users log in before making a reservation. The following code was added:

![reservations/views.py](docs/testing/authentication04.png)

![elite/settings.py](docs/testing/authentication05.png)

Now when a non authenticated user trys to reserve they are redirected to log in page

</details>

## Linking reservations to user accounts.

<details>
<summary>Click me</summary>

This didn't go very well. I updated code to link the reservations:

![model code](docs/testing/authenticating_reservations01.png)

![view code](docs/testing/authenticating_reservations02.png)

After this i tried to migrate but forgot that now there are empty fields. I dropped my reservation database and created a new version. this threw an error when accessing the reservation model from the admin page:

![error code](docs/testing/authenticating_reservations03.png)

I contacted student support who advised me to change to the sqlite3 database from now on and remigrate to a postgreSQL databse later on when my models are finished.

To test that the users are connected to the reservation I now need to create some users, reservations and a html page called user_reservations to be able to view them. 

![user reservations displaying](docs/testing/authenticating_reservations04.png)

</details>

## Edit a reservation

<details>
<summary>Click me</summary>

Users can now edit reservations. 

![reservation in admin page](docs/testing/edit_reservation01.png)

![reservation in logged in user view](docs/testing/edit_reservation02.png)

![reservation edited using the edit function](docs/testing/edit_reservation03.png)

To allow me to edit the reservation I had to:

- Create an edit_reservation view to handle the request
- Update my reservation form to a ModelForm which allows it access the database. It needs to this because of the instance in the edit_reservation view that pre populates the information in the form. ModelForms need a class meta.
- Edit the my_reservation.html for loop that loads reservations to have an edit button that links to the unique reservation_id that django creates. 

</details>

## Delete reservation 

<details>
<summary>Click me</summary>

Users can now delete reservations 

Multiple reservation for one user

![reservation in my reservations](docs/testing/delete_reservation01.png)

When pressing delete user is linked to delete confirmation page 

![reservation delete page](docs/testing/delete_reservation02.png)

When pressing confirm user is redirected to my_reservations and the reervations is deleted.

![reservation deleted](docs/testing/delete_reservation03.png)

The admin page shows the reservation was successfully deleted form the database

![reservation deleted in admin page](docs/testing/delete_reservation04.png)

</details>

## Reservations to show in time order on my_reservations

<details>
<summary>Click me</summary>

Reservations now show in time order

![my reservations in time order](docs/testing/reservation_order01.png)

</details>

## Homepage shows the latest reservation

<details>
<summary>Click me</summary>

logged in users without next reservation see:

![hompepage blank reservation](docs/testing/homepage_reservations01.png)

logged in users with a reservation see: 

![hompepage next reservation](docs/testing/homepage_reservations02.png)

Non logged in users see:

![non logged in user homepage](docs/testing/homepage_reservations03.png)

</details>

## reservations update display when reservation passed booking time.

<details>
<summary>Click me</summary>

A user has this booking. I need to wait and see if their booking updates to their next reservation after the time slot has passed.

![near expiration booking](docs/testing/expired_reservations01.png)

- The reservation does not remove when the time is passed. this will be the next thing to focus on. 

- my_reservations updated for deleting expired reservations. 

![expired reservation deleted](docs/testing/expired_reservations02.png)

This took a long time because I was over complicating the code. simple plans are always best!

</details>