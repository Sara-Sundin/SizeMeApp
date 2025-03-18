### Project 3

# SizeMeApp Website 

[View project on Heroku](#) 

## Introduction 

This website serves as the front-facing platform for SizeMeApp, an innovative solution designed to simplify online shopping by helping users find their perfect fit. While this is not the actual application, the website provides key information about how SizeMeApp works, its benefits for both customers and retailers, and how it integrates with e-commerce platforms. 

Explore the site to learn more about how SizeMeApp reduces returns, improves customer satisfaction, and enhances the online shopping experience through smart size recommendations. 

![Screenshot of the website on multi devices](assets/images_readme/multiscreen.png)

# CONTENT

[DATABASE OVERVIEW](#database-overview)
- Database ERD Schema

[USER EXPERIENCE (UX)](#user-experience)
- The website across UX planes
- User Stories
- Accessibility
- Aria labels

[DESIGN PLANNING](#design-planning)
- Design Planning
- Kanban Board

[VISUAL DESIGN IDENTITY](#visual-design-identity)
- Colour Scheme
- Typography
- Imagery
- Wire Frames
- Features

[TECHNOLOGIES USED](#technologies-used)
- Languages used to create the website
- Frameworks & Libraries
- Software
- Automated Tools
- AI

[DEPLOYMENT](#deployment)
- Heroku with Github Integration

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

[REFERENCES](#references)
- Media References
- Content References

[CREDITS](#credits)
- Images
- Code

[PERSONAL NOTES](#personal-notes)

[ACKNOWLEDGMENTS](#acknowledgments)

<br>
<br>
<hr>
<hr>

# DATABASE OVERVIEW
- [Database ERD Schema](#database-erd-schema)

The database schema for SizeMeApp is designed to efficiently manage user data, blog content, and user interactions. It consists of six main tables:

- CustomUser – Stores user details, including authentication and profile information.
- Post – Represents blog posts, which can only be created by admin users.
- Comment – Allows all users to comment on blog posts.
- LikePost – Manages the many-to-many relationship between users and posts, tracking likes.
- Newsletter – Handles newsletter content
- Subscriber – Handles email subscriptions.

The schema ensures clear relationships between users and content while maintaining scalability for future enhancements.

## Database ERD Schema

![Database ERD Schema](assets/images_readme/database_erd_diagram.jpg)

[Back to Content Table](#content)

<hr>
<hr>

# USER EXPERIENCE
- [UX planes](#the-website-across-UX-planes)
- [User Stories](#user-stories)
- [Accessibility](#accessibility)
- [Aria labels](#aria-labels-used)

## The website across UX planes

### Strategy Plane
The primary goal of the SizeMeApp website is to provide users with clear, accessible information about the app’s functionality while guiding them toward signing up and using the service. The target audience includes online shoppers seeking accurate size recommendations, as well as retailers looking to reduce returns and improve customer satisfaction.

The website meets user needs by:

- Offering a clear explanation of how SizeMeApp works.
- Providing calls-to-action that encourage users to sign up.
- Showcasing business benefits for retailers and e-commerce brands.
- Creating a seamless experience for users to explore the app's features.

### Scope Plane
The website includes essential features to educate and engage users:

- A homepage that introduces SizeMeApp and its benefits.
- A sign-up process that allows users to create an account.
- An interactive “How It Works” page explaining the app’s technology.
- A blog section where users can explore trends in fashion and sizing.
- A contact page for user inquiries and business partnerships.

Additional features, such as testimonials, success stories, and a retailer-focused section, enhance credibility and help potential users and businesses understand the impact of the app. This will be implemented in the future.

### Structure Plane
The website is structured to ensure smooth navigation and user engagement:

- The homepage provides an overview with a strong call to action.
- The "How It Works" page explains the sizing technology in an easy-to-understand format.
- A user dashboard (for registered users) allows them to manage their profile and measurements.
- The blog section offers informative content and allows registered users to engage via comments.

This logical structure ensures that first-time visitors, returning users, and frequent users can easily find relevant content.

### Skeleton Plane
The website layout is designed for clarity and usability:

- Navigation menus provide quick access to key sections.
- Clear CTAs (e.g., "Sign Up," "Try Now") guide users toward important actions.
- A well-structured blog page ensures easy reading and engagement.
- The user dashboard presents stored measurements and recommendations in an intuitive format.
- The contact page offers a simple, accessible form for inquiries.

The layout is responsive, ensuring an optimized experience across desktop, tablet, and mobile devices.

### Surface Plane
The visual design of the SizeMeApp website is clean, modern, and user-friendly, emphasizing trust and functionality:

- A neutral color palette combined with accent colors for CTAs enhances readability and usability.
- Typography is professional and easy to read, reinforcing clarity.
- High-quality visuals (icons, imaged) strengthen user engagement.
- Hover effects improve interactivity without distracting from core content.

Together, these design choices ensure that the website provides an engaging, informative, and intuitive experience for all visitors.

<hr>

## User Stories

The development of the SizeMeApp website followed a structured user story framework, ensuring that each feature was designed with clear objectives, measurable success, and actionable development steps.

### Example of User Story Implementation

#### User Story:
As a registered user, I want to update my measurements, so that I can keep my size data accurate as my body changes.

#### Acceptance Criteria:
- Users can edit and save new measurements.
- Changes are updated in real time.

#### Tasks:
- Implement an “Edit Measurements” feature.
- Ensure previous data is overwritten securely.
- By following this structured approach for each feature, the website ensures a user-centered experience while maintaining development clarity and efficiency.

The site follows the CRUD (Create, Read, Update, Delete) methodology to manage data efficiently. Each user story is structured to ensure that core functionalities align with CRUD operations, enabling seamless interaction with the system.

The user stories for SizeMeApp are structured into three categories:

- New Visitors – First-time users exploring the site to understand its purpose and decide whether to sign up.

- Returning Users – Registered users who come back to interact with features such as storing measurements and commenting on blog posts.

- Frequent Users – Engaged users who update their data, interact regularly, and receive personalized recommendations.

### New Visitors (First-Time Users Exploring the Site)
New visitors primarily engage with the site through reading and navigating content to understand SizeMeApp and its benefits.

- Visitors want to quickly understand what SizeMeApp does, how it works, and whether it is relevant to them.
- Clear call-to-action buttons guide users to sign up and test the application.
- Information is provided for both individual shoppers and business owners, including benefits for reducing returns.
- Blog posts and comments are accessible to all visitors to learn about online sizing and fashion technology.
- A team page introduces the people behind SizeMeApp to build trust.
- A contact form provides an easy way to ask questions or give feedback.

CRUD implementation: Create (contact form submission), Read (blog posts, team page, testimonials).

### Returning Visitors (Users Coming Back After Initial Engagement)
Returning users have registered and now interact with the site by storing personal data and engaging with content.

- Users can store their personal measurements in their profile for easier access while shopping online.
- They can comment on blog posts to engage in discussions.
- A simple and secure login process allows them to access stored measurements and interact with blog content.
- Users can like blog posts to save their favorite content.

CRUD implementation: Create (measurements, comments, likes), Read (stored data, blog posts), Update (profile details).

### Frequent Visitors (Engaged Users Who Interact Regularly)
Frequent users continue to refine their data and interact with advanced features.

- Users can update their measurements as their body changes to ensure accuracy.
- They remain logged in for convenience, reducing the need to re-enter credentials.
- Based on stored measurements, users receive personalized recommendations.
- Newsletters inform them about new features and updates.

CRUD implementation: Read (recommendations, testimonials), Update (measurements, profile), Read/Delete (notifications).

### Additional CRUD Features for Blog and Measurements
To ensure full CRUD coverage, additional user stories for managing blog posts, comments, and user data are included:

- Admins can create, edit, and delete blog posts to maintain relevant content.
- Registered users can edit or delete their own comments.
- Admins can moderate and delete inappropriate comments.
- Users can delete their account if they choose to remove their data.

CRUD implementation: Create (blog posts, comments, newsletters), Read (blog content, comments, measurements), Update (blog posts, profile), Delete (comments, user accounts).

Full user stories and progress tracking are available on the **SizeMeApp Kanban Board**:  
[View the Kanban Board](https://github.com/users/Sara-Sundin/projects/10/views/1)

<hr>

## Accessibility
The following measures has been taken to make sure the website is accessible.
- Semantic Elements: Elements like header, main, and footer are used to provide clear structure, making it easier for screen readers to interpret content.
- Descriptive Headings: Properly structured heading levels (e.g., h1, h2, h3) to create a logical document outline.
- Alt Attributes: Every image includes meaningful alt text, ensuring visually impaired users understand the content.
- Focusable Elements: Navigation links, buttons, and forms are fully accessible using only the keyboard (e.g., via tab and enter keys).
- High Contrast: Text and background colors are chosen to meet the standards.
- Flexible Layouts: The website is fully responsive, ensuring accessibility across various devices, including desktops, tablets, and smartphones.
- Viewport Meta Tag: Ensures proper scaling and readability on mobile devices.
- Labels for Form Fields: All form fields include <label> tags or appropriate aria-label attributes to guide users through form completion.
- ARIA labels: Aria roles are added where necessary to define regions of the page for assistive technologies.
- Readable Fonts: Fonts like "Lato" are legible with sufficient size and line spacing for comfortable reading.
- Scalable Text: Text can be resized without loss of content or functionality.
- Accessibility Testing Tools: Lighthouse and Django automated tools has been used to identify and address accessibility issues.

<hr>

## ARIA Labels
To ensure that the website is fully accessible and user-friendly for individuals using assistive technologies, the following ARIA attributes should be implemented. Some of these labels are already in place, while others need to be added to enhance accessibility further.

### Base Template (all pages)
- aria-controls="navbarNav" (for navbar toggler)
- aria-expanded="false" (for navbar toggler)
- aria-label="Toggle navigation" (for navbar toggler)
- role="img" and aria-label="SizeMeApp Logo" (for logo)
- aria-hidden="true" (for user avatar)
- aria-current="page" (for active navigation links)
- role="contentinfo" (for footer)

### Blog Page
- aria-label="{{ post.title }}" (for the image container)
- aria-live="polite" (for the author name flash message)
- aria-label="Read more about {{ post.title }}" (for the post link)
- aria-label="Page navigation" (for the pagination navigation)
- aria-label="Go to next page" (for the next page link)

### Post Page
- aria-label="{{ post.title }}" (for the featured image)
- aria-label="Close" (for the close button in the delete confirmation modal)
- aria-labelledby="deleteModalLabel" (for the delete confirmation modal)
- aria-hidden="true" (for the delete confirmation modal when not active)

### Dashboard Page
- role="img" for user avatar and measurement guide image.
- aria-label="User avatar" for the profile picture.
- aria-labelledby="avatarModalTitle" for the avatar modal.
- aria-labelledby="chestLabel" (and similar for waist, hips, shoulders) for measurement fields.
- aria-label="Illustration showing how to take body measurements." for the measurement guide image.
- aria-label="Delete measurements" for the delete button.
- aria-expanded="false" on the measurement toggle button (should be dynamically updated).

### Avatar Generator
- aria-label="Select color [color name]" for swatches.
- aria-label="Avatar preview" for the avatar canvas.
- aria-label="Save your avatar" for the download button.
- aria-label="Reset avatar settings" for the reset button.
- aria-label="Go back to main thumbnails" for the back button in additional thumbnails.
- role="img" for the avatar preview.
- aria-expanded="false" for hidden thumbnail sections (should be updated dynamically).

### Home Page
- aria-label="SizeMeApp Logo" (for hero section logo)
- aria-label="Sign up or go to dashboard" (for CTA button)
- aria-label="Enter your email address" (for newsletter email input)
- aria-label="Subscribe to newsletter" (for newsletter subscribe button)
- role="status" (for success message container)
- aria-label="Return to the homepage" (for back to home button)
- aria-label="Learn more about Why SizeMeApp" (for icon buttons linking to about page)
- aria-label="Visit our Instagram page (opens in a new tab)"
- aria-label="Visit our LinkedIn page (opens in a new tab)"
- aria-label="Connect on Whatsapp (opens in a new tab)"

### About Page
- aria-hidden="true" (for decorative icons)
- role="img" and aria-label="Sara Sundin, Co-Founder & Fashion Tech Expert" (for team images)
- aria-labelledby="sara-label" (for team descriptions)
- aria-labelledby="why-title" (for section headings)
- aria-label="Visit our Instagram page (opens in a new tab)"
- aria-label="Visit our LinkedIn page (opens in a new tab)"
- aria-label="Connect on Whatsapp (opens in a new tab)"

### Contact Page
- aria-labelledby="contact-form-heading" (for form association)
- aria-required="true" (for required input fields)
- aria-label="Send your message" (for the send message button)
- role="status" (for success message container)
- aria-label="Return to the homepage" (for back to home button)
- role="contentinfo" (for contact details)
- aria-hidden="true" (for decorative icons)
- aria-label="Visit our Instagram page (opens in a new tab)"
- aria-label="Visit our LinkedIn page (opens in a new tab)"
- aria-label="Connect on Whatsapp (opens in a new tab)"

### Under Construction Page
- aria-hidden="true" (for decorative icon)
- role="status" (for under construction message container)
- aria-label="Enter your email address" (for newsletter email input)
- aria-label="Subscribe to our newsletter" (for newsletter subscribe button)
- aria-label="Return to the dashboard" (for back to dashboard button)

### Sign In Form
- aria-labelledby="sign-in-heading" (for the page heading)
- role="alert" (for error messages)
- aria-label="Enter your email" (for login input)
- aria-label="Enter your password" (for password input)
- aria-label="Show or hide password" (for password toggle button)
- aria-label="Reset your password" (for forgot password link)
- aria-label="Sign in to your account" (for sign-in button)

### Register Form
- aria-labelledby="sign-up-heading" (for page heading)
- role="alert" (for error messages)
- aria-label="Enter your full name" (for name input)
- aria-label="Enter your email address" (for email input)
- aria-label="Enter your password" (for password input)
- aria-label="Show or hide password" (for password toggle button)
- aria-label="Reset your password" (for forgot password link)
- aria-label="Create your account" (for sign-up button)

### Log Out
- aria-labelledby="sign-out-heading" (for page heading)
- role="alert" (for confirmation message)
- aria-label="Confirm sign out" (for sign-out button)


[Back to Content Table](#content)

<br>
<br>
<hr>
<hr>
<br>
<br>

# DESIGN PLANNING
- [Design Planning](#design-planning)
- [Kanban Board](#kanban-board)

## Design Planning
This diagram represents the planning phase of my SizeMeApp project, mapping out its core structure and functionality. It outlines how users register, log in, and manage their profiles, including updating measurements for accurate size recommendations. I designed a dashboard with an avatar generator, a blog with a comment system, and a newsletter feature. In the end I managed to implify all features of the diagram except the actual application SizeMeApp, making the site a front end user and marketing tool.

![Planning Diagram](assets/images_readme/planning_project_3.jpg)

## Kanban Board
In the development of SizeMeApp, I used a Kanban board to organize tasks and prioritize development. By labeling features as Must-Have, Should-Have, Could-Have, and Wont-Have, I ensured a clear focus on essential components like user authentication, the dashboard, and measurement integration, while identifying non-critical elements for future development. This visual management tool helped me break down tasks into To Do, In Progress, and Completed, ensuring a clear overview of each design and development stage. I made sure all tasks required for the project were completed, while leaving some for future enhancements.
<br>

![The Kanban Board in progress](assets/images_readme/kanban_board_in_progress.jpg)

[Back to Content Table](#content)

<br>
<br>
<hr>
<hr>
<br>
<br>

# VISUAL DESIGN IDENTITY
- [Colour Scheme](#colour-scheme)
- [Typography](#typography)
- [Imagery](#imagery)
- [Wire Frames](#wire-frames)
- [Structure of the website](#structure-of-the-website)
- [Features](#features)

## Colour Scheme
The SizeMeApp color scheme is carefully chosen to create a clean, modern, and user-friendly interface. It consists of four key colors:

#616f82 (Muted Blue) – Used for the header, footer, and headings, this color establishes a professional and trustworthy feel. Blue is often associated with reliability, making it an ideal choice for a tool focused on accuracy in sizing.

#878787 (Neutral Grey) – The primary background color, grey adds subtle depth while maintaining a neutral, sophisticated look. It helps separate sections without being too visually dominant.

#ffffff (White) – Applied as a secondary background color, ensuring a clean and spacious layout. White provides contrast, improving readability and enhancing the minimalist aesthetic.

#e84e1b (Vibrant Orange) – Used for buttons and highlights, orange draws attention to important interactive elements, such as calls to action. The warm tone energizes the interface and creates a sense of urgency and engagement.
<br>

![Colour Scheme](assets/images_readme/color_scheme_3.jpg)

<hr>

## Typography
The chosen typography for SizeMeApp consists of Poppins for headings and Raleway for body text. Both are Google Fonts, carefully selected to balance a modern, professional aesthetic with optimal readability. This pairing enhances the user experience by ensuring a structured yet approachable interface that aligns with SizeMeApp’s goal of providing accuracy and ease in online shopping.

![Fonts](assets/images_readme/fonts_3.jpg)

### Poppins 
Poppins brings a clean, contemporary, and professional feel to the site. Its bold yet minimal design ensures clear hierarchy, making key sections such as headings, navigation, and CTAs stand out effectively.

### Raleway 
Raleway is a lightweight, elegant sans-serif font designed for readability. Its subtle letter spacing and refined structure make it ideal for body text, ensuring smooth reading and a user-friendly experience. This complements the bold presence of Poppins, providing a well-balanced visual hierarchy.

<hr>

## Imagery
The images used on this site are mainly generated using AI. The images for the blog posts and the male background template are generated through ChatGPT. The robot avatar outlines are created in Illustrator from a dighital.com icon pack. The logo images are created by myself using Illustrator.

<hr>

## Wire Frames
The wireframes were created in Adobe Illustrator for mobile, tablet and desktop. I have developed and used my own toolkit for the wireframes. The outcome for the website looks slightly different than the initial wireframes but for the most part the page remained consistent to the wireframes. For the final website I created a separate contact page and an "under construction" page for the SizeMeApp application.

<details open>
  <summary>Wireframes Home Page</summary>

  ![Wireframes Home Page](assets/images_readme/wireframes_home.jpg)
</details>

<details>
 <summary>Wireframes About & Contact Page</summary>

  ![Wireframes About Page](assets/images_readme/wireframes_about.jpg)
</details>

<details>
 <summary>Wireframes Dashboard Page</summary>

  ![Wireframes Dashboard Page](assets/images_readme/wireframes_dashboard.jpg)
</details>

<details>
 <summary>Wireframes Blog Page</summary>
 
 ![Wireframes Blog Page](assets/images_readme/wireframes_blog.jpg)
</details>

<details>
 <summary>Wireframes Post Page</summary>

![Wireframes Post Page](assets/images_readme/wireframes_post.jpg)
</details>

<hr>

## Features

### All pages

#### Favicon
The favicon for SizeMeApp features a minimalist three-ring design, symbolizing balance, precision, and connection - key elements in finding the perfect fit when shopping online. The central, bold ring represents the core function of the app: accurate sizing, while the two smaller rings above and below convey adaptability and seamless user experience.

This clean, geometric icon was designed to be simple yet recognizable, ensuring strong brand identity even at small sizes. The favicon enhances the visual consistency of the platform, aligning with the app’s modern and functional design.

 ![Favicon](assets/images_readme/favicon_rings_32x32.png)

#### Navigation
The navigation bar in SizeMeApp is designed for easy access to key features while maintaining a clean and modern look. It provides clear navigation to sections such as Home, About, Blog, and Contact, ensuring users can quickly find what they need.

For logged-in users, the navbar offers a personalized experience by displaying their avatar alongside the text "Logged in as [Username]", reinforcing a sense of identity and engagement.

This feature makes it easy for users to confirm their login status while navigating the site. The navbar also includes a Dashboard link for managing stored measurements and a Logout option for seamless account control.

The design ensures a consistent user experience, adapting for different screen sizes with a responsive mobile-friendly layout with a toggle. 

![Navigation Bar Desktop](assets/images_readme/navbar_desktop.jpg)

<details>
  <summary>Navigation Bar - Mobile</summary>

  ![Navigation Mobile](assets/images_readme/navbar_mobile.jpg)

</details>

#### Social Media Icons
SizeMeApp features Font Awesome social media icons for Instagram, LinkedIn, and WhatsApp, allowing users to easily connect with the brand. These icons include an interactive hover effect, where they expand and change color, providing visual feedback and enhancing user engagement. Their placement close to the footer ensures quick access to social platforms while maintaining a clean, modern design.

![Social Media Icons Desktop](assets/images_readme/media_icons_desktop.jpg)

#### Footer
The footer in SizeMeApp provides a simple and professional closing element for the site. It contains a copyright notice displaying "© 2025 TechFit Solutions. All rights reserved.", reinforcing brand identity and legal protection. The footer maintains a minimalistic design, ensuring it doesn’t distract from the main content while offering a consistent visual structure across all pages.

![Footer Desktop](assets/images_readme/footer_desktop.jpg)

### Home Page

#### Hero Section
The hero section serves as the visual centerpiece of SizeMeApp, immediately capturing attention with a clean, modern design. It prominently features the SizeMeApp logo, reinforcing brand recognition. In the background, a transparent, gridded human figure symbolizes precision, measurement, and technology, aligning with the app’s mission to provide accurate size recommendations. This striking visual sets the tone for a seamless user experience.

![Hero Section Desktop](assets/images_readme/hero_section_desktop.jpg)

<details>
  <summary>Hero Section - Mobile</summary>

  ![Hero Section Mobile](assets/images_readme/hero_section_mobile.jpg)

</details>

#### Intro Section - How It Works - Home page
The intro and "How It Works" section provide users with a clear, engaging overview of SizeMeApp’s purpose and functionality. It features three interactive headings - "Why SizeMeApp," "How It Works," and "Start Shopping" - each accompanied by a hover-effect icon that changes color and expands when hovered over. These icons serve as visual navigation links to the About page, ensuring users can seamlessly explore more details about the app.

![Intro Section Desktop](assets/images_readme/intro_section_desktop.jpg)

<details>
  <summary>Intro Section - Mobile</summary>

  ![Intro Section Mobile](assets/images_readme/intro_section_mobile.jpg)

</details>

#### Newsletter Signup
The newsletter section encourages users to stay updated with SizeMeApp’s latest features and news. It includes a simple, user-friendly sign-up form, allowing visitors to enter their email and subscribe. The CTA button ensures quick interaction, while the clean design keeps it visually appealing and accessible.

![Newsletter Section Tablet](assets/images_readme/sign_up_newsletter_tablet.jpg)

<details>
  <summary>Newsletter Section - Mobile</summary>

  ![Intro Section Mobile](assets/images_readme/sign_up_newsletter_mobile.jpg)

</details>

#### Success Message Newsletter
After subscribing, users see a clear success message confirming their sign-up. It reassures them that they’ll receive updates and includes a "Back to Home" button for easy navigation.

![Newsletter Success Message Tablet](assets/images_readme/success_newsletter_tablet.jpg)

#### About Us Section - Home page
The About section provides a brief introduction to SizeMeApp’s mission—revolutionizing online shopping with accurate size recommendations. A hover-effect icon and CTA link direct users to the About page, where they can explore more details about the technology, team, and benefits.

![About Us Intro Section Tablet](assets/images_readme/about_us_section_home_tablet.jpg)

### About Page 
- Why SizeMeApp Section
- How It Works Section
- Start Shopping Section

![About Page Sections Desktop](assets/images_readme/about_page_sections_desktop.jpg)

<details>
  <summary>About Page Sections - Mobile</summary>

  ![About Page Sections Mobile](assets/images_readme/about_page_sections_mobile.jpg)

</details>

#### About Us Section
The About Us section introduces the team behind SizeMeApp, highlighting their expertise in fashion tech and user experience. It features team photos and bios, giving users insight into the minds shaping the platform. This section builds trust and credibility, reinforcing the app’s mission.

![About Us Section Tablet](assets/images_readme/about_us_section_tablet.jpg)

<details>
  <summary>About Us Section - Mobile</summary>

  ![About Us Section Mobile](assets/images_readme/about_us_section_mobile.jpg)
</details>

### Contact Page
The Contact page provides an easy way for users to reach out with questions or feedback. It includes a contact form for direct messages, along with email, phone, and social media links. 

![Contact Page Desktop](assets/images_readme/contact_page_form_desktop.jpg)

#### Contact Form
The contact form allows users to easily send messages by entering their name, email, and inquiry. A confirmation message appears after submission, ensuring users know their request was received.

![Contact Form Mobile](assets/images_readme/contact_page_form_mobile.jpg)

#### Success Message Contact Form
After submitting a form, users see a clear success message, confirming their message was sent. It reassures them that the team will respond soon and includes a "Back to Home" button for easy navigation. 

![Success Message Contact Desktop](assets/images_readme/success_contact_tablet.jpg)

### Blog Page
The Blog Page provides insights on online sizing, fashion tech, and shopping tips. Posts are well-organized, and logged-in users can like and comment, fostering engagement and discussion.

#### Blog Cards
The blog cards provide a clean and structured preview of each post, displaying the featured image, title, excerpt, author, and date. Each card ensures easy readability and includes a clickable link to the full post. The design is responsive, adapting seamlessly across different screen sizes. 

![Blog Cards Desktop](assets/images_readme/blog_page_desktop.jpg)

<details>
  <summary>Blog Cards - Mobile</summary>

  ![Blog Cards Mobile](assets/images_readme/blog_page_mobile.jpg)
</details>

#### Post Page
The Post Page presents each blog post in a clean, readable format, featuring the title, featured image, author, and date. Below the content, users can like and comment to engage with discussions. A structured layout ensures easy navigation, and responsive design makes it accessible on all devices. 

#### Comment Count & Likes
Each blog post displays comment counts and like totals, allowing users to see engagement at a glance. Logged-in users can like posts and leave comments, fostering interaction and discussion.

![Comment Count & Likes Mobile](assets/images_readme/comment_count_likes_mobile.jpg)

#### Comment Section (CRUD)
The comment section supports full CRUD functionality, allowing users to Create, Read, Update, and Delete their comments. Logged-in users can post, edit, or remove their comments, while all visitors can read discussions. The system ensures a smooth and interactive user experience.

![Comment Section Desktop](assets/images_readme/comment_section_desktop.jpg)

<details>
  <summary>Comment Section - Mobile</summary>

  ![Comment Section Mobile](assets/images_readme/comment_section_mobile.jpg)
</details>

### Account Details

#### Register Form
The sign-up form offers a quick and secure registration process, collecting essential details like name, email, and password. A "Forgot your password?" link provides easy recovery. After signing up, users are automatically redirected to the dashboard, ensuring a seamless onboarding experience. 

![Register Form Desktop](assets/images_readme/sign_up_account_desktop.jpg)

<details>
  <summary>Register Form - Mobile</summary>

  ![Register Form Mobile](assets/images_readme/sign_up_account_mobile.jpg)
</details>

#### Login Form
The login form offers a user-friendly experience with placeholder text for guidance and a password toggle for visibility control. After logging in, the avatar and "Logged in as [Username]" text appear in the navigation bar, enhancing personalization and usability. 

![Login Form Mobile](assets/images_readme/login_form_mobile.jpg)

<details>
  <summary>Login Form - Desktop</summary>

  ![Login Form Desktop](assets/images_readme/login_form_desktop.jpg)
</details>

#### Logout Confirm Message
The logout link allows users to securely sign out of their account. Clicking it redirects them to a confirmation page with the message "Are you sure you want to sign out?", ensuring intentional logouts. This prevents accidental logouts and provides a seamless user experience. 

![Logout Message Mobile](assets/images_readme/logout_message_mobile.jpg)

#### Reset Password Form
The reset password form allows users to securely recover their account by entering their email. After submitting, a confirmation message appears, informing them that a reset link has been sent. This ensures a smooth and secure process, allowing users to regain access to their accounts effortlessly. 

![Reset Password Mobile](assets/images_readme/reset_password_mobile.jpg)
![Confirm Reset Desktop](assets/images_readme/confirm_reset_reset_desktop.jpg)

### Dashboard
The dashboard provides a centralized space for users to manage their measurements securely. The "Body Measurements" section, hidden by default for privacy, allows users to enter, update, and delete their size data. Additionally, the dashboard includes an avatar generator and a direct link to the SizeMeApp application for accurate size recommendations.

![Dashboard Desktop](assets/images_readme/dashboard_desktop.jpg)

#### Avatar Maker
The avatar generator lets users create a custom robot avatar, adding a unique and playful touch to their profile. Users can personalize features like head shape, eyes, mouth, and colors. The avatar can be saved and updated anytime, enhancing engagement while maintaining a futuristic, tech-inspired aesthetic. 

![Avatar Tablet](assets/images_readme/avatar_generator_tablet.jpg)

<details>
  <summary>Avatar Generator - Desktop</summary>

  ![Avatar Desktop](assets/images_readme/avatar_generator_desktop.jpg)
</details>

#### Measurement Form (CRUD)
The measurements form allows users to enter, update, and delete their body measurements for accurate size recommendations. Hidden under the "Body Measurements" section for privacy, it includes fields for chest, waist, hips, and shoulders. The form ensures a secure and user-friendly experience, giving users full control over their data.

![Measurement Form Tablet](assets/images_readme/measurements_tablet.jpg)

<details>
  <summary>Measurement Form - Mobile</summary>

  ![Measurement Form Mobile](assets/images_readme/measurements_mobile.jpg)
</details>

### Mockup SizeMeApp Access
The SizeMeApp button in your dashboard is currently a mockup for future development.

![SizeMeApp Access](assets/images_readme/enter_application_tablet.jpg)

### Under Construction Message
Clicking the SizeMeApp access button will take you to the under construction page, where we're building the SizeMeApp tool. Sign up for the newsletter for updates or follow the link to return to the dashboard.

![Under Construction Page](assets/images_readme/under_construction_tablet.jpg)

### 404 Page
Oops! You’ve landed on a 404 page, but don’t worry—you’re not lost alone! Your custom avatar is here to guide you back. The page you’re looking for doesn’t exist, but you can return to the dashboard or explore other sections of SizeMeApp to find what you need.

![404 Page]()

### Future Features
We’re taking SizeMeApp to the next level with an AI-powered application that ensures perfect fit recommendations. Soon, our site will feature a direct link to the SizeMeApp tool, making sizing effortless.

Our advanced AI system will analyze user measurements, brand size charts, and past purchases for accurate, real-time recommendations. A community-driven review system will let shoppers share fit insights, helping others make informed choices.

Retailers will be able to integrate SizeMeApp into their stores, reducing returns and waste. Future features include virtual try-ons and mobile measurement scanning, shaping a more personalized, sustainable shopping experience. Stay tuned!

<br>
<br>
<hr>
<hr>
<br>
<br>

# TECHNOLOGIES USED
- [Languages used to create the website](#languages-used-to-create-the-website)
- [Frameworks & Libraries](#frameworks-and-libraries)
- [Software](#software)
- [Automated Tools](#automated-tools)
- [AI](#ai)


## Languages Used to Create the Website
- HTML
- CSS
- JavaScript
- Python

## Frameworks and Libraries
- Django (for development and testing).
- Bootstrap (for responsive design and styling).
- Font Awesome (for icons).
- Google Fonts (for typography).
- Iloveimg.com (to compress images for faster loading).

## Software
- Adobe Illustrator (for wireframes and image creation).
- Adobe Photoshop (for image editing and optimization).
- VS Code (for version control).
- GitHub (to save and store the website's code and files).

## Automated Tools
- Chrome DevTools (for debugging and testing).
- Lighthouse (to analyze performance, accessibility, and SEO).
- W3C HTML & CSS Validator (to validate and check the html and css).
- JSHint (to validate and check the javascript code).
- Techsini.com (for multidevice image and testing responsiveness).

## AI

[Back to Content Table](#content)

<br>
<br>
<hr>
<hr>
<br>
<br>

# DEPLOYMENT
- [Heroku with GitHub Integration](#heroku-with-github-integration)

## Prerequisites
- GitHub repository containing your project files.
- A Procfile (if needed) specifying the start command for your app.
- A requirements.txt (for Python apps).

## Create a Heroku Account and App
- Go to Heroku and sign up (or log in if you already have an account).
- Click "New" > "Create new app" from the Heroku dashboard.
- Choose a unique App Name and select a region.
- Click "Create App".

![Heroku Deployment Add App](assets/images_readme/deploy_heroku_add-app.jpg)

## Connect GitHub Repository to Heroku
- In the Deploy tab of your Heroku app, go to "Deployment Method".
- Select "GitHub".
- Click "Connect to GitHub" and authorize Heroku to access your repositories.
- Search for your repository name and click "Connect".

![Heroku Deployment Github](assets/images_readme/deploy_heroku_connect-github.jpg)

## Configure Environment Variables
In the Settings tab, click "Reveal Config Vars" to add environment variables like API keys, database URLs, etc.

![Heroku Deployment Config Vars](assets/images_readme/deploy_heroku_add-config_vars.jpg)

## Deploy the App
- Under "Manual Deploy", select the branch you want to deploy (main).
- Click "Deploy Branch".
- Wait for Heroku to build and deploy your app.

## Check Your Deployed Website
- Once the deployment is successful, Heroku will provide a URL (e.g., https://your-app-name.herokuapp.com/).
- Click the URL (VIEW) to access your deployed website.

![Heroku Deployment Add App](assets/images_readme/deploy_heroku_deploy-branch.jpg)

<br>
<br>
<hr>
<hr>
<br>
<br>









