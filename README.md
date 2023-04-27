# CLASSIC GARAGE
Classic Garage is a full-stack, responsive, mobile-first website built for fictional motorcycle shop. It is compatible with all current major browsers.

The business offers its customers an easy way to access its services through an online booking system. Users can create an account, view, edit, and delete bookings, and learn more about the business and its services.

[Link to the website](https://classic-garage.herokuapp.com/)

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

# Technologies and Tools Used
- HTML5 - The structure and content of the website.
- CSS3 - The styling for the website.
- Python - The functionality of the website.
- Django - Python Web Framework.
- Django Allauth - Integrated set of Django applications addressing authentication, registration, account management
- Crispy Forms - Helps to render Django forms in a nicer way.
- Bootstrap - Front end development framework.
- GitPod - Used to create and edit the website.
- GitHub - Cloud based git repository used.
- GitBash - Terminal used to push changes to the GitHub repository.
- Cloudinary - Used to host all static files and images.
- Heroku - Used to deploy the website.
- Google Chrome DevTools - Test responsiveness and debug.
- Balsamiq - Used to create the wireframes for the project.
- W3C Validator - Used to validate HTML code.
- W3C CSS Validator - A validator which checks the validity of CSS code.
- CI Python Linter - Used to validate Python code.
- ElephantSQL - PostgreSQL database hosting service.
- Google Fonts - Fonts
- Font Awesome - Icons
- Color Space - Colour Palette Generator
- Pexels - Stock photos
- Unsplash - Stock photos
- Multi Device Website Mockup Generator - For responsive visuals of the website
- Favicon - for favicon

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

# Testing

## Bugs

# Deployment

## Forking the GitHub Repository

## Creating Local Clone

# Credits

# Acknowledgements