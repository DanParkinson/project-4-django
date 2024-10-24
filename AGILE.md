# AGILE

This is where I will document my agile approach. It will be set into phases to help me organise my work. After a few false starts where i found myself getting lost, this will help me document my thoughts. Because of the fault starts my README.md has already been created. 

## Phase 1

<details>
<summary>Click me</summary>

- Setup repo.
- Create Django project.
- Install basic dependencies and add to requirements.
- Create procfile to deploy to Heroku.
- Create app on Heroku.
- Link GitHub repo to Heroku app.
- Test to deploy working project ASAP.
- Document project creation and deployment.
- Perform design thinking exercise for features to include in project.
- Add user stories to readme.
- Add wireframes to readme.
- Mock up initial database design and document in readme.
- List and link technologies used in readme.
- Learn to use GitHub projects. Create user stories.

Still to do:
- Identify a colour schema to use in the site

![Phase1](docs/agile/phase1.png)

</details>

## Phase 2

<details>
<summary>Click me</summary>

Focus for the next session is to do with setting up templates to have a view of the home page. As well as this I will create my user stories in github projects for Phase 1, phase 2 and my overall User Stories to outline the project. 

- Setup base.html.
- create separate components for site such as head, header, navbar, footer in a subfolder to inject into base.html.
- Setup index page in home app.
- Build navigation.
- Set up styling basics and check with deployed Heroku app.

![Phase2](docs/agile/phase2.png)

With the templates linked, CSS and JS loading in the deployed version its time to make some models. Reservations will be first. 

</details>

## Phase 3

<details>
<summary>Click me</summary>

Focus for Phase 3 is creating a reservations model. I need a form for users to submit their reservations times. This needs to be saved to the database. I would like to create authentication but I need to research this a bit more as my understanding isnt quite where I would like it to be.

- forms needed for reservation submited
- model 
- views
- urls 

Now that I have a form to submit, a database to save the information and the admin panel is styled nicely. We need to add validation to the submittable form.

- Opening hours and 15 minute intervals
- Date that hasnt happened yet
- Number of people capped at 8 
- Phone numnber is a number 

The next step is to make sure that users cant double book. I will have to create a model for tables and connected them to bookings. This will be done at a later phase.

![Phase3](docs/agile/phase3.png)
</details>

## Phase 4

<details>
<summary>Click me</summary>

Now that users can submit a reservation and it is saved to the database. I think navigation around the website will speed up processes. Time to fix the nav bar to include *Home, Make a Reservation, Login, Logout, SignUp, menu, about us.

I havent decided if logging in is actually necessary for this project as users can just get email confirmation of the booking. If users dont need to login then a cancellation/alteration page will be added for users to engage with. This means that the reservations will need a unique code for users to edit their information. 

The navbar has been set up with links to the homepage, make a reservation, about us and menu. Now for the social media icons to be linked to social accounts. 

I have decided to implement a login user function so the navbar will be updated with these once it is done. At this point the social media icons will be implemented into the footer. 

![Phase4](docs/agile/phase4.png)

</details>

## phase 5 

<details>
<summary>Click me</summary>

This will be about user authentication using django AllAuth.

- Install `allauth` package.
- Add allauth to installed applications in settings.py.
- Add login/logout redirects back to index page.
- Perform migrations.
- Adapt navigation bar using Django Templates to to give registered/unregistered site users different menu options
- reservations can only be made by authenticated users. 
- Now the user needs to be linked with any reservation they make. simple edit to reservation model and views.
- This caused problems with the database so changed to sqlite3 adn remigrated.
- now to create users, reservation(That are hopefully linked to users) and create html that shows a logged in users reservations.
- Now to link the my_reservations page into the nav bar for authenticated users.

![Phase5](docs/agile/phase5.png)

Now that users can authories themselves and they are connected to their reservations. Users now need to be able to updated or cancel a reservation if necessary. 

</details>

## Phase 6

<details>
<summary>Click me</summary>

- Logged in users can access their reservations using my_reservations.
- Next to the reservations should be a button called edit that brings them to an edit reservations form.
- Another button called delete reservation should be next to that which removes the reservations entirely.
- Users need access to only their reservations.

After creating the edit form reponse an error was thrown. Apparently i need a modelform to handle the data instead of a normal form as i am accessing the database. modelforms need a meta class. 

- Now that users can edit their reservations they need to be able to delete them.

- Users need to be able to see their reservations in date/time order on their reservation page
This was a simple edit to my_reservations view. I ran into trouble understanding the difference between the models and the variables as i had called them similar things. Time to start planning names a bit more clearly. 

- Users can view their next reservation on the homepage if logged in. 

![Phase6](docs/agile/phase6.png)

This phase was a great way to manipulate database models and display data in html pages.

- I also need to check that the reservations update when their latest reservation time is passed. 

</details>

## Phase 7 

This will be about account management. users will be able to edit their details, delete the account and any reservations belonging to them, change their passwords.

I might bring in google/facebook sign in as well. 

- new app to handle accounts
- add accounts link to django all auth
- then link templates as django does all the hard work

- account_update view needs creating.
- import a form model to allow users to submit their new details
- Users can change their passwords.
- users can delete their account

- an error has occured with my_reservations where it is filtering by the current time and filtering out any reservation that is before that time, regardless of date. This needs fixing before progessing. If its the issue that i think it is I should be able to see the reservations in the morning. lets hope because its end of session. TO BE FIXED!!!!!!!!!!!!!!


Now that it was decided that users have to log in to access reservations. The Reservation model is now inefficient.

Reservations should require 
- User 
- Name 
- Phone number
- Date
- Time
- Number of people
- Special Occasion

Email is used in logging in so is already aquired. Time to update it. 

## Phase 8

Now that the bulk of the backend is working correctly i want to style my webiste. My bootstrap is a bit rusty so I need to relearn how to use it. 

## Final tests to remember 

1. Users can create account.

- Users can sign out  
- Users can sign in (with google?)
- Users can edit details and they are updated to databse(relogin)  
- Users can change password  
- Users can delete their account and any reservations made  
- Users can see wh*o they are logged in as  

2. Users can create reservations 

- Users can edit reservations
- Users can delete reservations
- Users can view their next reservation
- Users can view all reservations 
- Expired reservations do not show

3. Users can navigate

- Users can access Home, Account, About us, My reservations, Make reservation, Menu, Social media

4. All pages have correct information

-  Page titles are correct
-  All page views are similar
-  Home has links to Book, about us, menu
-  Accounts has details, edit, change password, delete with warning messages
-  About us has location and opening hours 
-  My reservations show all reservations in future. They can edit and delete.
-  make reservation has form to submit
-  menu has all food. 

5. Reservation functionaltiy
- Users cant double book
- Users can access reservation booking with information on how many tables are available
- Reservation deletion updateds prior
- Messages reinforce all of the above

6. Code checkers 
- All of the code checkers 

7. 