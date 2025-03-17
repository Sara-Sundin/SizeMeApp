### Project 3 

# SizeMeApp Website 

[View project on Heroku](#) 

## Introduction 

This website serves as the front-facing platform for SizeMeApp, an innovative solution designed to simplify online shopping by helping users find their perfect fit. While this is not the actual application, the website provides key information about how SizeMeApp works, its benefits for both customers and retailers, and how it integrates with e-commerce platforms. 

Explore the site to learn more about how SizeMeApp reduces returns, improves customer satisfaction, and enhances the online shopping experience through smart size recommendations. 

![Screenshot of the website on multi devices](media/images_README/Multiscreen.png)

# CONTENT

[REPOSITORY & DATABASE OVERVIEW](#repository-&-database-overview)
- Project Structure & Explanation
- Repository Diagram
- Database ERD Scheme
<br>

[USER EXPERIENCE (UX)](#user-experience)
- The website across UX planes
- User Stories
- Accessibility
- Aria labels
<br>

[DESIGN PLANNING](#design-planning)
- Design Planning
- Kanban Board

[VISUAL DESIGN IDENTITY](#visual-design-identity)
- Colour Scheme
- Typography
- Imagery
- Wire Frames
- Features
<br>

[TECHNOLOGIES USED](#technologies-used)
- Languages used to create the website
- Frameworks & Libraries
- Software
- Automated Tools
- ChatGPT
<br>

[DEPLOYMENT](#deployment)
- Heroku
<br>

[TESTING](#testing)
- Manual vs. Automated Testing
- Manual Testing
- Devices
- Browsers
- User Story Testing
- Testing Grid
- Automated Testing
- Chrome Dev Tools
- Lighthouse
- Validators
- Testing with Django
- Bugs & Fixes
<br>

[REFERENCES](#references)
- Media References
- Content References
<br>

[CREDITS](#credits)
- Images
- Code
<br>

[PERSONAL NOTES](#personal-notes)

[ACKNOWLEDGMENTS](#acknowledgments)

<br>
<br>
<hr>
<hr>
<br>
<br>

# DATABASE OVERVIEW

The database schema for SizeMeApp is designed to efficiently manage user data, blog content, and user interactions. It consists of five main tables:

CustomUser – Stores user details, including authentication and profile information.
Post – Represents blog posts, which can only be created by admin users.
Comment – Allows all users to comment on blog posts.
LikePost – Manages the many-to-many relationship between users and posts, tracking likes.
Newsletter & Subscriber – Handles newsletter content and email subscriptions.
The schema ensures clear relationships between users and content while maintaining scalability for future enhancements.

![Database ERD Schema](media\images_README\Database ERD Diagram.jpg)


