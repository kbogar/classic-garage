# CLASSIC GARAGE
Classic Garage is a full-stack, responsive, mobile-first website built for fictional motorcycle shop. It is compatible with all current major browsers.

The business offers its customers an easy way to access its services through an online booking system. Users can create an account, view, edit, and delete bookings, and learn more about the business and its services.

- [Link to the website](https://classic-garage.herokuapp.com/)
- [Git Repository](https://github.com/kbogar/classic-garage)

![](/documentation/mockup.png)

# Table of Contents
* [Entity Relationship Model](#entity-relationship-model)
* [Agile Methodology](#agile-methodology)
* [User Experience (UX)](#user-experience-ux)
    * [Site Goals](#site-goals)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Color Scheme](#color-scheme)
    * [Typography](#typography)
    * [Icons](#icons)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Technologies and Tools Used](#technologies-and-tools-used)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)

# Entity Relationship Model
Before beginning this project, I researched the data models necessary to construct the desired application. This research included defining the entities and the relationships between them, creating a comprehensive list of fields and data points, and outlining the necessary actions for the application to function correctly. With this information in hand, I was able to construct the necessary models for the project and ensure that the application would be able to meet its goals.

![](/documentation/erm.png)
# Agile Methodology
This project was developed using the agile methodology and version control on GitHub. Tasks were tracked and managed through Github's issue-tracking system, allowing for rapid progress and continued progress tracking.
## [User Stories Board](https://github.com/users/kbogar/projects/4/views/1)
![](/documentation/userstories.png)

## [Issues](https://github.com/kbogar/classic-garage/issues)
![](/documentation/issues.png)
I found the Agile Methodology to be an extremely useful tool for organizing and managing the development of my project. By breaking down the project into smaller tasks, I was able to better track my progress and ensure that I stayed on schedule. Additionally, I was able to make adjustments to my plan as needed, allowing me to make the most of my time and resources. The satisfaction of ticking off a completed User Story and placing it in the 'Done' column was also a great motivator.

[Back to top](#table-of-contents)

# User Experience (UX)
## Site Goals
The goal of this custom motorcycle website is to provide customers with an easy-to-use, comprehensive resource for researching and servicing their motorcycles, and to ensure that the customers have access to the highest quality products and services and that their experiences are positive and enjoyable.

The target audience for this custom motorcycle website is motorcycle enthusiasts and owners who are looking for high-quality parts, accessories, and services for their motorcycles.

## User Stories
Every User Story was recorded in GitHub Issues, and the goal is to establish what user would expect from interacting with the website.
### As a Business Owner
- As a Business Owner I would like users visiting our site to land on the homepage so that they can learn about us and the services we provide.
### As a User
- As a User I would like to view the site on different screen sizes so that I can view the site on mobile devices.
- As a User I can see the website links and logo at the top of the page so that I can easily navigate on the page.
- As a User I can see contact details and social links on the bottom of the page so that I can contact and follow the company and the website creator.
- As a User I can easily navigate to the About page and learn about the company so that I can decide if I need their service.
- As a User I can easily navigate to Our Services page so that I can find information about the companies services.
- As a User I can use my username and password so that I can log in to my user account.
- As a User I can log out of my account so that I can keep my details secure.
- As a user I can login to my My Bookings page so that I can access and update my information, details of booking.
### As Admin
- As a Site Admin I have access to the database so that I can manage customer's details and bookings.
### As a Developer
- As a Developer I can provide profile creation functionality so that user can create/read/update or delete their bookings.
- As a Developer I can provide registration functionality so that users can make bookings with the company.
- As a Developer I can add a favicon to the websites tab and title so that it gives better visual feedback to the user.
- As a Developer I can automate user creation upon registration so that the admin doesn't have to do it manually.
- As a Developer I can add alert messages so that the user is notified if their form has been submitted or an error has occurred.
- As a Developer I can have a placeholder text in the register form so that users have a better experience filling in their forms.
- As a Developer I can add an empty default choice so that the user is alerted when trying to submit a booking without selecting the type.
- As a Developer I can add validations on the date field so that users can only pick days 3 days in advance.

[Back to top](#table-of-contents)

## Wireframes
Wireframes were initially created on paper to help deciding the most important aspects of the website, and getting a sense of the overall website. Afterward, Balsamiq was utilized to create wireframes with a more accurate representation of the design.

The wireframe for this project could differ from the final design due to modifications made during the development process.

<details>

<summary>Wireframes</summary>

**Mobile Wireframes Home, About, Our Services**

![Mobile Home, About, Our Services](/documentation/mobile_wireframe1.png)

**Mobile Wireframes Register, Login**

![Mobile Register, Login](/documentation/mobile_vireframe2.png)

**Desktop Wireframes Home, About**

![Desktop Home, About](/documentation/desktop_wireframe1.png)

**Desktop Wireframes Our Services, Register**

![Desktop Our Services, Register](/documentation/desktop_wireframe2.png)

**Desktop Wireframes Login, My Bookings**

![Desktop Login, My Bookings](/documentation/desktop_wireframe3.png)

</details>


___

## Color Scheme
Using [ColorSpace](https://mycolor.space/), I decided to use Random Shades palette for this website, to achieve a simple, understated look with minimalistic design elements.

![](/documentation/ColorSpace.png)

## Typography
[Google Fonts](https://fonts.google.com/) Prompt and Sans Serif were used to create this website

## Icons
[Font Awesome](https://fontawesome.com/) social media icons were used for the Footer and throughout the website.

[Back to top](#table-of-contents)

# Features
## Existing Features

### Header & Navigation

Logo with a link which brings the user to the home page. Navigation menu consisting of links to other pages, available to both visitors and logged-in users, that are optimized for various devices.

<details>

<summary>Click to view screenshots of Navigation features</summary>

**Navigation closed Mobile**

![Nav mobile closed](/documentation/navbar2.png)

**Navigation open Mobile**

![Nav mobile open](/documentation/navbar2a.png)

**Navigation open logged in Mobile**

![Nav mobile logged in open](/documentation/navbar_signedin2.png)

**Navigation Desktop**

![Nav desktop](/documentation/navbar1.png)

**Navigation logged in Desktop**

![Nav desktop logged in](/documentation/navbar_signedin.png)

</details>

<br>

### Footer
All the users will have access to the footer section of the page. They can find contact information with the phone number, and social media links.

<details>

<summary>Click to view screenshots of Footer features</summary>

**Footer Mobile**

![Footer Mobile](/documentation/footer2.png)

**Footer Desktop**

![Footer Desktop](/documentation/footer1.png)

</details>

<br>

### Home Page
The homepage welcomes the user and there are two sections, the first with a brief description of the business, a background image, and a button that takes the user directly to the contact page, and the second section with a button that takes the user to the register page.

<details>

<summary>Click to view screenshots of the Home Page</summary>

**Home Page Mobile**

![Home Page Mobile](/documentation/homepage_mobile.png)

**Home Page Desktop**

![Home Page Desktop](/documentation/homepage.png)

</details>

<br>

### About Page
The About page provides more information about the family business, and it's reachable via the About link in the navigation bar. There are two sections, the first with a background image, the company name, and the meme, and the second section with information about the business and a Contact Us button.

<details>

<summary>Click to view screenshots of the About Page</summary>

**About Page Mobile**

![About Page Mobile](/documentation/aboutpage_mobile.png)

**About Page Desktop**

![About Page Desktop](/documentation/aboutpage.png)

</details>

<br>

### Our Services Page
The Our Services page it's reachable via the Our Services link in the navigation bar. There are two sections, the first with a background image, and a description of what kind of services provide the business. The second section with a type of service, an image, a description, and a button to Book a Service, and a Contact Us button for custom projects.

<details>

<summary>Click to view screenshots of the Our Services Page</summary>

**Our Services Page Mobile**

![Our Services Page Mobile](/documentation/ourservicespage_mobile.png)

**Our Services Page Desktop**

![Our Services Page Desktop](/documentation/ourservicespage.png)

</details>

<br>

### Registration
The website has the functionality for a user to register and create an account. The registration form can be accessed through the navigation bar, or through the Home Page second section, and Our Services Page book services section.
- The Register Form includes a message if the user already have an account then there is a sign in link also
- It uses django-allauth to provide all the settings for user authentication and includes the fields below.

    - Username
    - email address
    - password
    - password again

- The form is submitted via Register button at the bottom of the form.
- After the form has been submitted the user is redirected to the Home page and an alert message is displayed on the screen giving the user feedback about their registration.

<details>

<summary>Click to view screenshots of Registration</summary>

**Registration Page**

![Registration Page](/documentation/register.png)

**Register Message**

![Register Message](/documentation/register_message.png)

</details>

<br>

### Contact Us
The Contact Us page is reachable via the Home, About, and Our Services page. Logged-in users and also guests have access to the Contact Us page, so the users don't need to register to send us a message. 
- The contact form includes these fields; name, email, message. 
- The form is submitted via Send button at the bottom of the form.
- After submitting the form successfully, an alert message is displayed on the screen giving the user feedback about their sent message.
    

<details>

<summary>Click to view screenshots of the Contact Us Page</summary>

**Contact Us page**

![Contact Us page](/documentation/contactus.png)

**Contact Us Message**

![Contact Us Message](/documentation/contact_message.png)

</details>

<br>

### Login
Returning users can access the login form through the navigation bar or through the Our Services page if the user wants to book a service.
- The login form includes a message and a link to Sign Up/Register form for the users who have not yet registered.
- It uses django-allauth to provide all the settings for user authentication and includes the fields below;
    - username
    - password

- The form is submitted via Sign In button at the bottom of the form.
- When the user clicks on the sign-in button, they are redirected to the Home page and an alert message is displayed on the screen giving the user feedback about their login.

<details>

<summary>Click to view screenshots of Login</summary>

**Login page**

![Login page](/documentation/login_mobile.png)

**Login Message**

![Login Message](/documentation/signin_message.png)

</details>

<br>

### Logout
The logged-in users can end their session and logout/signout.
- The logout form can only be accessed from the navigation bar.
- A confirmation message appears if they want to sign out.
- When they click on Sign Out button, they are redirected to the Home page and an alert message is displayed on the screen giving the user feedback on their signout.

<details>

<summary>Click to view screenshots of Logout</summary>

**Logout page**

![Logout page](/documentation/logout.png)

**Logout Message**

![Logout Message](/documentation/signout_message.png)

</details>

<br>

### Book a Service
- Guest users will not be able to book service, they will be asked to log in/register first.
- The book service form can be accessed on Our Services page.
- A logged-in user can access a book service form. They can fill out the form by inputting their details;
    - name
    - email
    - request date
    - service type
    - message

- The form is submitted via Send Request button at the bottom of the form.
- After submitting the form successfully, an alert message is displayed on the screen giving the user feedback about their booking.

<details>

<summary>Click to view screenshots of a Booking</summary>

**Guest user**

![Guest user](/documentation/guestuser.png)

**Booking page**

![Booking page](/documentation/bookservice_mobile.png)

**Booking Message**

![Booking Message](/documentation/booking_message.png)

</details>

<br>

### Profile/My Bookings
The website gives the user the functionality to create, view, update, and delete bookings. All bookings are listed on the My Bookings page.
- The user must be logged-in to access the My Bookings page on the navigation bar.
- A logged-in user who has not yet created a booking will have a message with information to add a booking.
- When a user book a service, his request is still pending, so he can still update or delete his booking.
- Admin-approved bookings cant be updated or deleted by users.

<details>

<summary>Click to view screenshots of My Bookings page</summary>

**Not Booked yet**

![No Booking](/documentation/notbookedyet.png)

**My Bookings page**

![My Bookings page](/documentation/mybookings_mobile.png)

</details>

<br>

### Update and Delete Bookings
The website gives the user the functionality to update bookings via the Update button on the Booking Detail Card, and also to delete bookings via the Delete button.
- The user must be logged in to access the My Bookings page and to update or delete the booking.
- When the user clicks on the update button from the pending booking, they will be redirected to the update form where they can update their details. By clicking save, their booking will be updated and redirected to the My Bookings page.
- After submitting the update form successfully, an alert message is displayed on the screen giving the user feedback about their updated booking.
- When the user clicks on the delete button from the pending booking, they will be redirected to the delete booking page where they will be asked if they really want to delete their booking. By clicking delete, their booking will be deleted, or by clicking cancel they will be redirected to the My Bookings page.
- After submitting the delete option, an alert message is displayed on the screen giving the user feedback about their deleted booking.

<details>

<summary>Click to view screenshots</summary>

**Update Booking**

![Update Booking](/documentation/updatebooking.png)

**Update Booking Message**

![Update Booking Message](/documentation/updatebooking_message.png)

**Delete Booking**

![Delete Booking](/documentation/deletebooking.png)

**Delete Booking Message**

![Delete Booking Message](/documentation/delete_message.png)

</details>

<br>

### Admin Panel
The website offers the business owner the ability to view and interact with the database using a web-based Django Admin panel.
- The Admin panel is reachable by typing /admin/ at the end of the website's URL in the URL bar.
- The user is brought to the Django Administration Login Page, where they are required to enter their Username and Password in order to gain access. Superuser status is required to log in.
- The Superuser has the capability to control all aspects of the system, including creating, modifying, deleting, and viewing.
- The project models can be viewed in the Admin panel, they are listed in the booking (Booking models, Custom models).

<details>

<summary>Click to view screenshots</summary>

**Admin login**

![Admin Login](/documentation/adminlogin.png)

**Admin Booking model**

![Admin Booking model](/documentation/djangoadmin1.png)

**Admin Contact model**

![Admin Contact model](/documentation/djangoadmin2.png)

</details>

<br>

## Future Features
- Time field for service bookings, currently the user can choose just a date.
- To archive the finished bookings.
- Email or phone verification.
- Reset/Forgot password functionality.
- User review page.
- When the registered user creates a booking, the name and the email field should be automatically populated.

[Back to top](#table-of-contents)

# Technologies and Tools Used
- [HTML5](https://www.w3schools.com/html/) - The structure and content of the website.
- [CSS3](https://www.w3schools.com/css/css_intro.asp) - The styling for the website.
- [Python](https://www.python.org/) - The functionality of the website.
- [Django](https://www.djangoproject.com/) - Python Web Framework.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Integrated set of Django applications addressing authentication, registration, account management
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Helps to render Django forms in a nicer way.
- [Bootstrap](https://getbootstrap.com/) - Front end development framework.
- [GitPod](https://www.gitpod.io/) - Used to create and edit the website.
- [GitHub](https://github.com/) - Cloud based git repository used.
- [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal used to push changes to the GitHub repository.
- [Cloudinary](https://cloudinary.com/) - Used to host all static files and images.
- [Heroku](https://www.heroku.com) - Used to deploy the website.
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Test responsiveness and debug.
- [Balsamiq](https://balsamiq.com/wireframes/) - Used to create the wireframes for the project.
- [W3C Validator](https://validator.w3.org/) - Used to validate HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - A validator which checks the validity of CSS code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - Used to validate Python code.
- [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL database hosting service.
- [Google Fonts](https://fonts.google.com/) - Fonts
- [Font Awesome](https://fontawesome.com/) - Icons
- [Color Space](https://mycolor.space/) - Colour Palette Generator
- [Pexels](https://www.pexels.com/) - Stock photos
- [Unsplash](https://unsplash.com/) - Stock photos
- [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php) - For responsive visuals of the website
- [Favicon](https://www.favicon.cc/) - for favicon

## Libraries
The following libraries and modules are used in the project and they are located in requirements.txt file.
- asgiref==3.6.0
- cloudinary==1.32.0
- crispy-bootstrap4==2022.1
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==3.2.18
- django-allauth==0.54.0
- django-crispy-forms==2.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- psycopg2==2.9.6
- PyJWT==2.6.0
- python3-openid==3.2.0
- pytz==2023.3
- requests-oauthlib==1.3.1
- sqlparse==0.4.3

[Back to top](#table-of-contents)

# Testing
All testing information can be found in [TESTING.md](https://github.com/kbogar/classic-garage/blob/main/TESTING.md)

# Bugs
I encountered a few errors during the coding of my project and there were fixed throughout the development.
## Solved
- Trailing whitespace errors and line too-long errors in Python code.
- On Contact page html had a bad value for attribute on form element. I cleared the action attribute to fix the issue.
- I had an issue when I changed one of my model fields and tried to migrate the database again, it didn't work. It had to delete some of the migration folders and the database on ElephantSQL to fix the problem.
- There was an issue at the final Heroku deployment, there was an error, and I could not deploy, because I forgot to add crispy-bootstrap4 to requirements.txt. When I added it later it was deployed with no problems.
- Non-logged-in users can access restricted content and functionality either through on-screen elements or direct entry of the URL. This issue was on update and delete bookings page. I added an if/else statement to fix this issue, so just a logged in user has access to these pages, else they need to log in first.

## Unsolved
At the moment there are no known bugs left to solve.

# Deployment
This project is deployed using [Heroku](https://www.heroku.com).
- Before deployment I created a env.py file in Gitpod. This file contains all the sensitive information that we must not push to Github. So I added env.py to .gitignore file.
- Modify settings.py to make django project aware of the env.py file.
- Created a requirements.txt containing the necessary libraries and modules for the app to run properly.
- Also created Procfile, this tells Heroku how to run this project.

The steps for deploying through Heroku are as follows:
- Go to Heroku website and log in.
- Go to Dashboard, click on 'New' and 'Create New App'.

<details>

<summary>Click to view screenshots</summary>

![](/documentation/heroku1.png)

</details>

<br>

- Add name for your app and choose region.
- Then click 'Create app'.

<details>

<summary>Click to view screenshots</summary>

![](/documentation/heroku2.png)

</details>

<br>

- Navigate to 'Deploy' tab and choose 'Connect to Github'.
- Search for your repository that you want to deploy.
- Click 'Connect'.

<details>

<summary>Click to view screenshots</summary>

![](/documentation/heroku3.png)

</details>

<br>

- You can choose if you want manual or automatic deployment.
- Choose Main Branch and click 'Deploy Branch'.

<details>

<summary>Click to view screenshots</summary>

![](/documentation/heroku4.png)

</details>

<br>

- When the deployment is succesfully finished, go to Settings tab.
- Click on 'Reveal Config Vars'.
- Add the necessary variables; `CLOUDINARY_URL`, `DATABASE_URL`, `PORT`, `SECRET_KEY`.
- Click 'Open app'.

<details>

<summary>Click to view screenshots</summary>

![](/documentation/heroku5.png)

</details>

<br>

## Forking the GitHub Repository
Forking allows you to view and edit the code without affecting the original repository.
- Navigate to GitHub repository.
- Click on 'Fork' in the top right corner.
- This will take you to your own repository to fork with the same name as the original branch.

## Creating Local Clone
Steps to create a local clone:
- Click on the code tab under the repository name.
- Then click 'Code' button to the right above the files listed.
- Click on clipboard icon to copy the URL.

[Back to top](#table-of-contents)

# Credits
## Content
- [W3CSchool](https://www.w3schools.com/) for general and helpful tips for Bootstrap and Django.
- [Stack Overflow](https://stackoverflow.com/) when I was stucked and needed help with code.
- [Devpractical](https://devpractical.com/bootstrap-sticky-footer/) on how to create sticky footer in Bootstrap.
- [Bootstrap Documentation](https://getbootstrap.com/) for general tips and setup.
- [Django](https://www.djangoproject.com/) for general tips and how to.
- 'I Think Therefore I am Blog' walkthrough project on how to setup the whole code environment, models, views, forms, etc.
- [Very Academy](https://www.youtube.com/watch?v=GxA2I-n8NR8&list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT) learn Django Class based views tutorial.
- [Selmi Tech](https://www.youtube.com/watch?v=3_3q_dE4_qs) build a doctor apointment booking system tutorial.
- [Slack](https://slack.com/) for any issues and questions.

## Media
- [Free Logo Maker](https://www.freelogodesign.org/) for making the logo of the website.
- [Pexels](https://www.pexels.com/) - Stock photos.
- [Unsplash](https://unsplash.com/) - Stock photos.
# Acknowledgements
- This project was built as a part of the Full Stack Software Development education at [Code Institute](https://codeinstitute.net/).
- My mentor Spencer Barriball for the guidance and encouragement.
- My Wifi thank you for all the support.

[Back to top](#table-of-contents)