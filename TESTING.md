# Table of Contents
* [Validator Testing](#validator-testing)
    * [HTML Code Validator](#html-code-validator)
    * [CSS Code Validator](#css-code-validator)
    * [Python Validator](#python-validator)
* [Lighthouse Testing](#lighthouse-testing)
* [Browser and Responsivness Testing](#browser-and-responsivness-testing)
* [Manual Testing](#manual-testing)
    

# Testing

## Validator Testing

### HTML Code Validator
- All the HTML pages were tested with [W3C Validator](https://validator.w3.org/) and there were no errors found.

**Home Page**

![Home page](/documentation/home_test.png)

**About Page**

![About page](/documentation/about_test.png)

**Our Services Page**

![Our Services page](/documentation/ourservices_test.png)

**Register Page**

![Register page](/documentation/register_test.png)

**Login Page**

![Login page](/documentation/login_test.png)

**My Bookings Page**

![My Bookings page](/documentation/mybookings_test.png)

**Update Bookings Page**

![Update Bookings page](/documentation/updatebookings_test.png)

**Delete Bookings Page**

![Delete Bookings page](/documentation/deletebooking_test.png)

**Logout Page**

![Logout page](/documentation/logout_test.png)

**Contact Page**

![Contact page](/documentation/contact_test.png)

**Book Service Page**

![Book Service page](/documentation/bookservice_test.png)

[Back to top](#table-of-contents)

### CSS Code Validator
- The CSS code were tested with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and there were no errors found.
- 7 warnings due to vendor extension prefixes.

**Styles test**

![Styles Test](/documentation/styles_test.png)

[Back to top](#table-of-contents)

### Python Validator
- All the Python files were tested using [CI Python Linter](https://pep8ci.herokuapp.com/) and there were no errors found.
- There were issus with long lines in settings.py and they were fixed with # noqa at the end of the line. Could not separate into two lines because of errors.

**admin.py**

![](/documentation/adminpy_test.png)

**apps.py**

![](/documentation/appspy_test.png)

**constants.py**

![](/documentation/constantspy_test.png)

**forms.py**

![](/documentation/formspy_test.png)

**models.py**

![](/documentation/modelspy_test.png)

**urls.py**

![](/documentation/urlspy_test.png)

**views.py**

![](/documentation/viewspy_test.png)

**models.py**

![](/documentation/modelspy_test.png)

**settings.py**

![](/documentation/settingspy_test.png)

**urls2.py**

![](/documentation/urls2py_test.png)


[Back to top](#table-of-contents)


### Lighthouse Testing
- The project has been tested with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) Lighthouse, for performance, accessibility, best practice, and SEO.
- There are a few lower performance scores on mobile tests because of image downloads from Cloudinary. The images I used are from 200-800kib and in PNG and JPG formats.
- Because of time constraints, I could not investigate further at this time.

**Home Page Desktop**

![](/documentation/lighthousetest_desktophome.PNG)

**Home Page Mobile**

![](/documentation/lighthousetest_mobilehome.PNG)

**About Page Desktop**

![](/documentation/test_desktopabout.PNG)

**About Page Mobile**

![](/documentation/test_mobileabout.PNG)

**Our Services Page Desktop**

![](/documentation/test_desktop_ourservices.PNG)

**Our Services Page Mobile**

![](/documentation/test_mobile_ourservices.PNG)

**Register Page Desktop**

![](/documentation/test_desktop_register.PNG)

**Register Page Mobile**

![](/documentation/test_mobile_register.PNG)

**Login Page Desktop**

![](/documentation/test_desktop_login.PNG)

**Login Page Mobile**

![](/documentation/test_mobile_login.PNG)

**Logout Page Desktop**

![](/documentation/test_desktop_logout.PNG)

**Logout Page Mobile**

![](/documentation/test_mobile_logout.PNG)

**My Bookings Page Desktop**

![](/documentation/test_desktop_mybookings.PNG)

**My Bookings Page Mobile**

![](/documentation/test_mobile_mybookings.PNG)

**Contact Page Desktop**

![](/documentation/test_desktop_contact.PNG)

**Contact Page Mobile**

![](/documentation/test_mobile_contact.PNG)


[Back to top](#table-of-contents)

### Browser and Responsivness Testing
- The website is responsive for screens min width 300px to max width 2560px, and were tested on the following browsers with no known issues:
    - Mozilla Firefox
    - Google Chrome
    - Microsoft Edge

### Manual Testing
- This project was tested manually several times throughout the development.
    - All links on web pages external/internal are working.
    - Clicking on the company logo gets you to the home page.
    - If Guest Users are trying to access a page that requires them to be logged in, then they are redirected to the login/register page.
    - Guest Users have access to the Contact page, by filling out the form they can contact the company.
    - Registered Users have access to booking functionality, by filling out the form they can book a service.
    - Users have to be logged in to see their bookings on the My Bookings page.
    - On the My Bookings page Users can update or delete bookings, and an alert message is showing every time when changes are made.
    - A notification message is shown when something is performed.
    - All forms have validation for the required fields.

[Back to top](#table-of-contents)