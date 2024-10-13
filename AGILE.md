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

Now that users can submit a reservation and it is saved to the database. I think navigation around the website will speed up processes. Time to fix the nav bar to include *Home, Make a Reservation, Login, Logout, SignUp. 

I havent decided if logging in is actually necessary for this project as users can just get email confirmation of the booking. If users dont need to login then a cancellation/alteration page will be added for users to engage with.
