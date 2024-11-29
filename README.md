# NARTH VAD3R MERCH
----------------
This website was created as the 4th Milestone Project for Code Institute's web application development course.

<img src="/media/homepage.png">
<br><br>

**[Link to the Deployed Site](https://narth-vad3r-merch-92994612de68.herokuapp.com/)**
<br><br>
----------------

## Contents
<br><br>

* [User Experience](#user-experience)
    * [Rationale](#rationale)
    * [Owner Goals](#owners-goals)
    * [Shoppers Goals](#shoppers-goals)HRKU-fd5be397-4552-47a2-b72b-e28ac7a82095
* [Design](#design)
    * [User Stories](#user-stories)
    * [WireFrames](#wireframes)
    * [Database Schema](#database-schema)
    * [Styling](#styling)
* [Feautres](#features)
    * [Multi-Page Features](#mutli-page-features)
    * [Homepage](#homepage)
    * [Products Page](#products)
    * [Product Details Page](#product-details-page)
    * [Add Review Page](#add-review-page)
    * [Edit Review Page](#edit-review-page)
    * [Bag Page](#bag-page)
    * [Checkout Page](#checkout-page)
    * [Checkout Success Page](#checkout-success-page)
    * [Profile Page](#profile-page)
    * [Send Response Page](#send-response-page)
    * [Allauth Pages](#allauth-pages)
    * [404 Error Page](#404-error-page)
    * [500 Error Page](#500-error-page)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

<br><br>

----------------

## User Experience

### Rationale

**NARTH VAD3R MERCH** is an online store specializing in merch for my online streaming platform and personality. This store caters to fans and followers who would like to wear the brand item and support the channel, offering a wide range of products that celebrate the NARTH VAD3R theme.

There is clear and simple intuitive buttons as guidance to help the user along their way, such as a "Register", "Login", "Logout", "Home", "Create Review", "Edit Review", "Delete Review" and so on. The user must be logged in to edit or delete their comments/reviews.
<br><br>

### Owners Goals
- The owner aims to offer a wide range of products that celebrate the NARTH VAD3R theme. This includes both clothing, accessories, and many other bits and bobs, ensuring there's something for every fan.
- The owner wants customers to have a positive and enjoyable shopping experience. This includes a user-friendly website that is easily navigable.
- The owner wants to offer customers the ability to express their opinions, providing valuable insights for both the owner and potential buyers by leaving reviews for products if they wish.
- Customer satisfaction is a top priority. The owner is dedicated to providing excellent UX and UI for the users pleasure and ease, assistance with orders, and addressing any concerns that may arise.
<br><br>

### Shoppers Goals
- Shoppers want to browse through a diverse selection of NARTH VAD3R merchandise.
- Some shoppers may have specific products titles in mind that they're looking to find and purchase.
- Shoppers would want a user-friendly website with a secure checkout process to ensure a hassle-free shopping experience.
- Some shoppers may want to engage with the community by leaving reviews for products they've purchased.
<br><br>

## Design
<br><br>

### User Stories

From the goals outlined above user stories were created to ensure that development efforts are aligned with user needs and preferences.

| **USER STORY #**                 | **AS A** | **I WANT TO BE ABLE TO...**                                                          | **SO THAT I CAN...**                                                                  |
| ------------------------------------ | --------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **VIEWING & NAVIGATION**         |                 |                                                                                          |                                                                                           |
| 1                                    | Shopper         | Easily navigate through the site.                                                        | Discover a comprehensive list of products.                                                |
| 2                                    | Shopper         | Browse products within a specific category.                                              | Easily locate products of interest without extensive searching.                           |
| 3                                    | Shopper         | Browse products within a specific subcategory.                                           | Efficiently identify desired products without sifting through numerous options.           |
| 4                                    | Shopper         | Access detailed information about individual products.                                   | Access product details including price, description,manufacturer, reviews and images.     |
| 5                                    | Shopper         | Conveniently view the total quantity of items in my shopping bag throughout my visit.    | Make informed purchasing decisions to stay within budget.                                 |
| 6                                    | Shopper         | Effortlessly switch between product categories and their corresponding subcategories.    | Quickly find specific products I'm searching for.                                         |
| **REGISTRATION & USER ACCOUNTS** |                 |                                                                                          |                                                                                           |
| 7                                    | Shopper         | Register for an account with ease.                                                       | Enjoy the convenience of a personal account with access to my profile.                    |
| 8                                    | Shopper         | Receive a confirmation email promptly after registering.                                 | Receive confirmation of successful account registration (use example email at this time). |
| 9                                    | Shopper         | Conveniently log in and out of my shopper's account.                                     | Access and manage my personal account information.                                        |
| 10                                   | Shopper         | Effortlessly recover my password if forgotten.                                           | Easily recover access to my account if needed.                                            |
| 11                                   | Shopper         | Enjoy a personalized user profile.                                                       | Review my complete order history and personal details.                                    |
| **SORTING & SEARCHING**          |                 |                                                                                          |                                                                                           |
| 12                                   | Shopper         | Sort available products based on preferences.                                            | Effortlessly identify products by price, category and subcategory or name.                |
| 13                                   | Shopper         | Organize products within a specific category.                                            | Locate the best-priced product within specific categories.                                |
| 14                                   | Shopper         | Arrange products within specific subcategories.                                          | Quickly determine the most suitable product for my preferences and needs.                 |
| 15                                   | Shopper         | Search for products by name or description with ease.                                    | Efficiently locate specific products I intend to purchase.                                |
| 16                                   | Shopper         | Quickly review search history and the number of results.                                 | Easily identify I am viewing the correct products.                                        |
| **PURCHASING & CHECKOUT**        |                 |                                                                                          |                                                                                           |
| 17                                   | Shopper         | Easily select desired quantities for products during the purchasing process.             | Avoid unintentionally selecting an incorrect product quantity.                            |
| 18                                   | Shopper         | Receive on-screen notifications when adding products to my shopping bag.                 | Receive instant feedback to confirm the accuracy of my actions or to rectify errors.      |
| 19                                   | Shopper         | View items in my shopping bag for easy checkout.                                         | Clearly see the total cost of my purchase and review the list of all items included.      |
| 20                                   | Shopper         | Adjust quantities for individual items in my shopping bag.                               | Effortlessly adjust my purchase details before proceeding to checkout.                    |
| 21                                   | Shopper         | Enter payment information securely and conveniently.                                     | Complete the checkout process swiftly and seamlessly.                                     |
| 22                                   | Shopper         | Trust that my personal and payment information is kept safe and secure.                  | Provide necessary information for the purchase with confidence.                           |
| 23                                   | Shopper         | Receive an order confirmation after completing a purchase.                               | Verify that all details provided are accurate to prevent any mistakes.                    |
| **PRODUCT REVIEWS**              |                 |                                                                                          |                                                                                           |
| 24                                   | Shopper         | Access available product reviews while browsing.                                         | Access valuable insights from other customers about the product.                          |
| 25                                   | Shopper         | Easily understand how to contribute my own reviews.                                      | Decide whether to contribute my own review based on personal experiences.                 |
| 26                                   | Shopper         | Submit my own review of the product.                                                     | Share my personal product experience with the community.                                  |
| 27                                   | Store Owner     | Edit or update previously submitted reviews.                                             | Choose to edit a review incase of inappropriate/offensive language, racism etc.           |
| 28                                   | Store Owner     | Delete a review if necessary.                                                            | Have the ability to completely remove unacceptable comments or discriminatory statements. |
| **ADMIN & STORE MANAGEMENT**     |                 |                                                                                          |                                                                                           |
| 29                                   | Store Owner     | Add new products to the store.                                                           | Add new items to my store's inventory.                                                    |
| 30                                   | Store Owner     | Edit or update existing product information.                                             | Modify product details, including price, description, manufacturer etc.                   |
| 31                                   | Store Owner     | Remove products from the store.                                                          | Remove items that are no longer available for sale from the inventory.                    |

### WireFrames 

* Wireframes
    * Figma: Easy to create, uses and shares detailed images whilst also effective.
    * Please find my wireframes here: [Figma: NARTH-VAD3R-MERCH Wireframes](https://www.figma.com/design/3bpngbRKa1hOoDr93XJkBu/Untitled?node-id=1-2&node-type=canvas&t=RaiKsccqktDh65Fp-0)
<br><br>

### Database Schema

Schema to show tables in database along with their relation to each other, also included is the allauth-user schema to show custom tables relationship.

**[Database Schema Here](https://lucid.app/lucidchart/808d5995-54d8-41b8-ae69-c35a23535251/edit?page=0_0&invitationId=inv_3c81c0e6-226f-4ee3-9813-6e3a6adfbce7#)**
<br><br>

### Styling

 * Colour Scheme
    * Primary colours used on the website: ![Color Scheme](/media/narth-vad3r-merch-colour-pallette.png)

 * Typography
    * 'Orbitron' font is the main font used throughout the site as this is the font that goes with the brands theme. All have sans-serif as its fallback font, in case the imported fonts dont load for any reason.
    * The main logo uses the 'Orbitron' font.
    * "Star Wars" have been used in the page titles and "Orbitron" has been used for the paragraph text.
 <br><br>

 ## Features

 ### Mutli-Page Features

 #### Navbar

The website's navigation comprises two key elements: the top navigation and the main navigation. The top navigation, depicted below, features essential functionalities. Visitors can access the site's logo, conduct product searches using the search bar, and either "Register" or "Login" via the "My Account" icon. Additionally, users can easily view the total number of items in their shopping bag. Once signed in, the options available in the "My Account" dropdown menu where they can access "My Profile" and "Logout".

The second component, the main navigation, empowers visitors to explore various product categories. This component is accessible through the hamburger icon on mobile devices. This navigation system and all of its constituent elements have been meticulously designed to be fully responsive, as exemplified by the accompanying screenshots.

<details>
<summary>Navbar - Desktop</summary>
<br>
<img src="/media/navbar-dt.png">
</details>
<details>
<summary>Navbar - Mobile</summary>
<br>
<img src="/media/navbar-mobile.png">
</details>
<details>
<summary>My Account - Logout</summary>
<br>
<img src="/media/logout-dt-lighthouse.png">
</details>
<details>
<summary>My Account Profile</summary>
<br>
<img src="/media/profile.png">
</details>

This deliberate design ensures that visitors can seamlessly and intuitively navigate the site, regardless of their device or screen size, enhancing their overall browsing experience.
<br><br>

#### Footer

The footer is a consistent element present on every page of the website. It serves as a valuable navigation tool for mobile users, providing a basic copyright text. When scrolling down, amongst the footer a "back to top" button will appear to take you to the top of the page when pressed.

<details>
<summary>Footer</summary>
<br>
<img src="/media/footer.png">
</details>
<details>
<summary>Footer - With Back Button</summary>
<br>
<img src="/media/footer-backbtn.png">
</details>
<br><br>


#### Toasts

Toasts are utilized throughout the site. Toasts are small, non-intrusive notifications that are displayed to the user to convey various types of messages. They serve the purpose of providing feedback or important information in a visually unobtrusive manner.

1. Success Toast:
Indicates that an action or process was successful. Accented in green.

2. Error Toast:
Alerts the user about an error or problem that occurred. Accented in red.

3. Info Toast:
Provides informative messages that do not require immediate action from the user. Accented in blue.

4. Warning Toast:
Warns the user about a situation that may require their attention. Accented in yellow.

<br><br>

### Homepage

The homepage has a minimalist design, featuring a tagline that encapsulates the essence of the store. A Call-to-Action (CTA) button guides visitors to explore the comprehensive range of products available on the site. This deliberate simplicity ensures that the homepage remains uncluttered, with a special emphasis on directing the user to the diverse collection of anime apparel.

<details>
<summary>Homepage - Desktop</summary>
<br>
<img src="/media/homepage.png">
</details>
<details>
<summary>Homepage - Mobile</summary>
<br>
<img src="/media/homepage-mobile.png">
</details>
<br><br>

### Products

The Products Page dynamically showcases products sourced from the database, contingent upon selected filtering options including category, subcategory and search terms.

<details>
<summary>Products - Desktop</summary>
<br>
<img src="/media/products.png">
</details>
<details>
<summary>Products - Mobile</summary>
<br>
<img src="/media/products-mobile.png">
</details>
<br><br>

<br><br>

3. Products Detail: When clicked on a product from the product page, the user will be taken to the product detail page. This is where the user can find all the information on the product such as description, materials, fit etc.

<details>
<summary>Products Information - Desktop</summary>
<br>
<img src="/media/product_detail.png">
</details>
<details>
<summary>Products Information - Mobile</summary>
<br>
<img src="/media/product-detail-mobile.png">
</details>
<br><br>

4. Sort Selector: A dropdown menu located near the top of the page, allowing users to sort products based on various criteria such as price, name, manufacturer, category, and subcategory.

<details>
<summary>Sort Selector</summary>
<br>
<img src="/media/sort-selector.png">
</details>
<br><br>

5. Product Cards: Each product is displayed in an individual card format. Cards are arranged in column amounts suitable for screen size of the user. The card includes:

* Product Image: Clickable and serves as a direct link to the product's detail page, providing users with a visual representation of the product, also has glow and animation on hover.
* Product Name: Clearly states the name of the product.
* Rating: Displays the product rating to help users.
* Price: Indicates the cost of the product.
* Category and Subcategory: Specifies the specific category and subcategory to which the product belongs redirects to a view of products filtered by relevant category or subcategory.

<details>
<summary>Product Card</summary>
<br>
<img src="/media/cards.png">
</details>
<br><br>

### Product Details Page

 The Product Details Page plays a pivotal role in guiding users through their shopping journey, providing them with the information and tools they need to make informed purchasing decisions. It combines visual appeal with functional features to create an engaging and user-friendly shopping experience.

<details>
<summary>Product Details - Desktop</summary>
<br>
<img src="/media/product_detail.png">
</details>
<details>
<summary>Product Details - Mobile</summary>
<br>
<img src="/media/product-detail-mobile.png">
</details>

 1. Product Image: Presents a visual representation of the product, providing users with a clear view of what they are considering. Image will open in new tab if clicked enabling user closer inspection, in further development image would open in zoomable modal.

 2. Product Information:

    * Product Name: Clearly states the name of the product.
    * Price: Indicates the cost of the product.
    * Category and Subcategory: Specifies the specific category and subcategory to which the product belongs redirects to a view of products filtered by relevant category or subcategory.
    * Manufacturer: Displays the name of the manufacturer or publisher responsible for producing the product.
    * Product Description: Offers a comprehensive overview of the product's features, specifications, and benefits, assisting users in making informed decisions.
    * Materials: Shows the user what materials the product is made from.
    * Country of Origin: This tells the user where the black product originally comes from.
    * Fit: Helps the user know how the product fits to help with sizing when purchasing.

3. Quantity Input Box: Allows users to specify the quantity of the product they wish to add to their shopping bag, ensuring precise ordering. Users are unable to select a quantity outside of the range 1-99, this achieved by disabling the use of the decrement and increment buttons on the quantity input and by checking the validity of the form on submission.

4. "Keep Shopping" and "Add to Bag" Buttons: Offer two distinct options for user actions. "Keep Shopping" allows users to continue browsing products, while "Add to Bag" submits the quantity input form and places the selected item into their shopping bag.

5. Reviews Section (Hidden by JS Click to Reveal): Conceals the reviews section by default, providing a cleaner interface. Users can choose to reveal the reviews by clicking on the heading, providing additional feedback and insights about the product. Revealing reviews section also enables the user to submit a review about the product by revealing the "Leave a Review" Button. Ability to add reviews is limited to authenticated users.

<details>
<summary>Leave Review</summary>
<br>
<img src="/media/leave-review.png">
</details>
<details>
<summary>Reviews Section</summary>
<br>
<img src="/media/reviews.png">
</details>

<br><br>

### Reviews

When the user clicks the Leave a Review button on the product details page, they are redirected to the Add Review page for that product. The Add Review page contributes to a dynamic and interactive shopping experience, empowering users to share their opinions and contribute to the collective knowledge about products available in the store. Ability to add a review is limited to authenticated users.

<details>
<summary>Add Review- Desktop</summary>
<br>
<img src="/media/leave-review.png">
</details>
<details>
<summary>Reviews</summary>
<br>
<img src="/media/reviews.png">
</details>
<br><br>

**Add Review Page Components**

1. Review Form:
* Title Field: Allows the user to input a title for their review.
* Textarea for Content: Provides a space for the user to write the content of their review.
* Rating Dropdown: Allows the user to select a rating from 0 to 5, indicating their overall satisfaction with the product.

<br><br>

### Edit Review Page

The Edit Review page serves the purpose of allowing users to make modifications to their existing reviews. It shares a similar structure with the Add Review page, but the form is prepopulated with the current review data. Ability to edit reviews is limited to the user that created the review or Administrator.

<details>
<summary>Edit Review - Desktop</summary>
<br>
<img src="/media/edit-review.png">
</details>
<details>
<summary>Edit Review - Mobile</summary>
<br>
<img src="/media/edit-review-mobile.png">
</details>

<br><br>

### Basket page

The Basket page enhances the overall shopping experience by giving users control over their selections, enabling them to review and modify their choices, and providing transparent cost information.

<details>
<summary>Basket - Desktop</summary>
<br>
<img src="/media/basket.png">
</details>
<details>
<summary>Basket - Mobile</summary>
<br>
<img src="/media/basket-mobile.png">
</details>
<br><br>

 **Basket Page Components**
 
 1. Product Information Section:

* Product Image: Displays a visual representation of the product, providing users with a clear visual reference.

* Product Name: Identifies the name or title of the product, ensuring easy recognition.

* Product SKU: Provides a unique identifier for the product, aiding in inventory management.

* Product Price per Unit: Indicates the cost of a single unit of the product, allowing users to understand the pricing structure.

* Quantity Input Box: Allow users to increment or decrement the quantity of the product in their shopping bag, facilitating easy adjustments.

* Update Button: Enables users to update the quantity of the product currently in the bag, providing flexibility in their shopping choices.

* Remove Button: Allows users to remove the product from the bag if they decide not to proceed with the purchase.

* Sub-Total per Item: Displays the total cost for each individual product based on the quantity selected.


2. Bag Summary:

* Bag Total: Reflects the cumulative cost of all the items currently in the shopping bag.

* Delivery Cost: Indicates any associated delivery charges.

* Grand Total: Provides the total cost of all products in the shopping bag, including both product costs and any applicable delivery charges.

* Free Delivery Threshold Alert: If the grand total is below the free delivery threshold, a prominent text in red advises the shopper how much more they need to spend to qualify for free delivery.

<br><br>

3. Shopping Basket Buttons:

Keep Shopping CTA: A button that redirects the user back to the products page, allowing them to continue browsing and adding more items to their shopping bag.

Secure Checkout: This button initiates the checkout process, leading the user to a secure page to complete their purchase.


### Checkout Page

The Checkout Page plays a pivotal role in ensuring a smooth and secure transition from product selection to order confirmation. It provides users with the necessary tools and information to review, confirm, and successfully complete their purchase.

<details>
<summary>Checkout - Desktop</summary>
<br>
<img src="/media/checkout.png">
</details>
<details>
<summary>Checkout - Mobile</summary>
<br>
<img src="/media/checkout-mobile.png">
</details>
<br><br>

**Checkout Page Components**

1. Order Form: Collects essential information from the user, including personal details, delivery address, and payment information. This ensures accurate processing and delivery of the order.

* User Details:
    - Full Name
    - Email Address
    - Phone Number

* Delivery Information:
    - Street Address Line 1
    - Street Address Line 2 (Optional)
    - Town/City
    - County/Region (Optional)
    - Country (Dropdown Selection)
    - Postal Code

* Payment Information:
    - Card Information (Handled by Stripe)

2. Order Summary: Provides a clear and detailed overview of the user's selected items, including product images, quantities, names, and subtotals. This allows users to review their order before finalizing the purchase.

 At the Bottom of the Order Summary:
* Order Total
* Delivery Cost
* Grand Total
If the Grand Total is below the free delivery threshold, a red text warning will inform the user how much more they need to spend to qualify for free delivery.

3. Buttons:

"Adjust Bag" Button: Allows users to go back to the shopping bag page to make any necessary adjustments before finalizing the order.

"Complete Order" Button: Submits the order form for processing. Payment is handled securely by Stripe.

<br><br>

### Checkout Success Page

After the successful processing of an order, the shopper is automatically redirected to the Checkout Success Page. This page provides a comprehensive receipt that includes the following details:

<details>
<summary>Checkout Success - Desktop</summary>
<br>
<img src="/media/checkout-success.png">
</details>
<details>
<summary>Checkout Success - Mobile</summary>
<br>
<img src="/media/checkout-success-mobile.png">
</details>
<br><br>

**Checkout Success Page Components**

1. Order Information:

* Order Number or Reference ID.

* Order Details. Comprehensive information about each item in the order, including:
    - Product Name
    - Quantity
    - Price per Unit
    - Subtotal
    - Delivery Information:

* Details about where the order will be delivered, including:
    - Address
    - Any specific delivery instructions (if provided)
    - Billing Information:

* Summary of the billing details used for the transaction.

2. Return to Products Button:

This button allows the shopper to return to the Products Page, giving them the opportunity to explore more items or categories.

3. Confirmation Email:

A confirmation email is automatically sent to the user's provided email address. The email includes a summary of the order.

### Profile Page

The Profile Page serves as a hub for users to see their account information such as username, email and recent orders. It contributes to a seamless and personalized user experience. Ability to access profile page is limited to authenticated users.

<details>
<summary>Profile - Desktop</summary>
<br>
<img src="/media/profile.png">
</details>
<details>
<summary>Profile - Mobile</summary>
<br>
<img src="/media/profile-mobile.png">
</details>
<br><br>

**Profile Page Components**

1. Default Delivery Information Form:
* Full Name
* Street Address 1
* Street Address 2
* Town/City
* County/Region
* Country (Dropdown Selection)
* Postal Code

2. Accordion Sections:
* Order History:
Displays past orders with the following details for each order:
- Order Number (Link to Past Order Confirmation)
- Date of Order
- Items in Order
- Order Total

<br><br>

### Allauth Pages

Site utilizes allauth for user account creation and authentication. Allauth is a powerful authentication framework for Django that streamlines the process of implementing user authentication and account management features in your web application. It offers a wide range of functionalities to handle user registration, login, email confirmation and password management.

1. User Registration: allauth provides a robust mechanism for user registration. Users can sign up by providing essential information such as username, email, and password.

2. Sign Up: Users can sign up to the website and create an account using their credentials.

3. Login and Logout: Users can securely log in to the application using their registered credentials. allauth also offers a user-friendly logout process.

4. Password Management: Users can reset their password if they forget it, and allauth handles the entire password reset flow, including sending reset emails and updating the password.

5. Integration with Django Admin: allauth seamlessly integrates with the Django admin interface, making it easy to manage user accounts and authentication settings.

### 404 Error Page

The 404 Error Page serves the purpose of handling and communicating 404 errors, indicating that the requested page could not be found. A button is provided that redirects the user back to the Homepage.

### 500 Error Page

The 500 Error Page serves the purpose of handling and communicating 500 errors, indicating that the there was an internal server error.. A button is provided that redirects the user back to the Homepage.

## Technologies

### Languages

* HTML5 - for content and structure.
* CSS3 - for styling.
* JS/JQuery - for frontend functionality and functions that request and handle data from the backend.
* Python - for the backend functionality.
    * Python Modules used -
    * asgiref==3.8.1
    * boto3==1.35.67
    * botocore==1.35.67
    * crispy-bootstrap5==2024.10
    * dj-database-url==0.5.0
    * Django==4.2
    * django-allauth==65.0.2
    * django-countries==7.6.1
    * django-crispy-forms==2.3
    * django-storages==1.14.4
    * gunicorn==23.0.0
    * jmespath==1.0.1
    * pillow==11.0.0
    * psycopg2==2.9.10
    * psycopg2-binary==2.9.10
    * s3transfer==0.10.4
    * sqlparse==0.5.1
    * stripe==11.1.1
    * whitenoise==6.8.2

<br><br>

### Tools

* Cloudconvert - used to convert images to WEBP format.
* Tinypng - used to compress images.
* Baslamiq - used to create wireframes.
* Logo.com - used to create logo.
* Diagrams.net - used to create DB schema.
* Am I Responsive - used to create responsive mockup for readme.
* Google Dev Tools - used for troubleshooting during development.
* Git/Github - used for version control and storage.
* Bootstrap - used for layout, positioning and styling.
* Favicon.io - used to create favicon.
* FontAwesome - used for icons.
* Heroku - used for deployment.
* Djecrety - used to create secret keys.
* AWS S3 - used to store images and static files.
* Stripe - Used to process the payment information.
* SQLite - Used for database for local development.
* ElephantSQL - Used to host the production database.
<br><br>

## Testing

All Python files have been run through the CI Python Linter to ensure it is PEP8 compliant, all are clear with no errors.

All JavaScript files have been run through JShint and have no errors using jshint esversion: 6.

The W3C Markup Validator and W3C CSS Validator services were used to validate every page of the project, to ensure there were no errors.

 * [W3C Markup Validtor](https://validator.w3.org/)
 * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
 * [JS Lint](https://www.jslint.com/)
 * [JS Hint](https://www.jshint.com/)
 * [CI Python Linter PEP8](https://pep8ci.herokuapp.com/#)

### Validation results

<details>
<summary>Homepage</summary>
<br>
<img src="/media/homepage-html-validation.png">
</details>
<details>
<summary>Products</summary>
<br>
<img src="/media/products-html-validation.png">
</details>
<details>
<summary>Product Detail</summary>
<br>
<img src="/media/product-detail-html-validation.png">
</details>
<details>
<summary>Edit Review</summary>
<br>
<img src="/media/edit-review-html-validation.png">
</details>
<details>
<summary>Basket</summary>
<br>
<img src="/media/basket-html-validation.png">
</details>
<details>
<summary>Checkout</summary>
<br>
<img src="/media/checkout-html-validation.png">
</details>
<details>
<summary>Checkout Success</summary>
<br>
<img src="/media/checkout-success-html-validation.png">
</details>
<details>
<summary>Sign Up</summary>
<br>
<img src="/media/sign-up-html-validation.png">
</details>
<details>
<summary>Login</summary>
<br>
<img src="/media/sign-in-html-validation.png">
</details>
<details>
<summary>Logout</summary>
<br>
<img src="/media/logout-html-validation.png">
</details>
<details>
<summary>Profile</summary>
<br>
<img src="/media/profile-html-validation.png">
</details>
<details>
<summary>404</summary>
<br>
<img src="/media/404-html-validation.png">
</details>
<details>
<summary>500</summary>
<br>
<img src="/media/500-html-validation.png">
</details>
<br><br>

### CSS Validation

All static CSS files pass CSS Validation at [W3C CSS validation service](https://jigsaw.w3.org/css-validator/) with no errors.

<details>
<summary>base.css</summary>
<br>
<img src="/media/base-css-validation.png">
</details>
<details>
<summary>checkout.css</summary>
<br>
<img src="/media/checkout-css-validation.png">
</details>

<br><br>

### JS Validation

JS files and scripts on templates run through [JShint](https://jshint.com/) for validation with no errors.

<details>
<summary>Script validation.</summary>
<br>
<img src="/media/js-validation.png">
</details>

<br><br>

### Python Validation

Pylance used during development to detect errors and PEP8 compliance, but code also run through [CI PEP8 Linter](https://pep8ci.herokuapp.com/) and passed with no warnings.

#### Root Level
<details>
<summary>custom-storages.py</summary>
<br>
<img src="/media/custom-storage-py-validation.png">
</details>
<details>
<summary>manage.py</summary>
<br>
<img src="/media/manage-py-validation.png">
</details>

#### NARTH VAD3R MERCH 
<details>
<summary>asgi.py</summary>
<br>
<img src="/media/asgi-py-validation.png">
</details>
<details>
<summary>settings.py</summary>
<br>
<img src="/media/setting-py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="/media/urls-py-validation.png">
</details>
<details>
<summary>wsgi.py</summary>
<br>
<img src="/media/wsgi-py-validation.png">
</details>

#### Basket App
<details>
<summary>apps.py</summary>
<br>
<img src="/media/basket-apps-py-validation.png">
</details>
<details>
<summary>contexts.py</summary>
<br>
<img src="/media/basket-contexts-py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="/media/urls-py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="/media/basket-views-py-validation.png">
</details>
<details>
<summary>templatetags/bag_tools.py</summary>
<br>
<img src="/media/basket-bagtools-py-validation.png">
</details>

#### Checkout App
<details>
<summary>admin.py</summary>
<br>
<img src="/media/checkout-admin-py-validation.png">
</details>
<details>
<summary>apps.py</summary>
<br>
<img src="/media/checkout-apps-py-validation.png">
</details>
<details>
<summary>models.py</summary>
<br>
<img src="/media/checkout-models-py-validation.png">
</details>
<details>
<summary>signals.py</summary>
<br>
<img src="/media/checkout-signals-py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="/media/checkout-urls-py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="/media/checkout-views-py-validation.png">
</details>
<details>
<summary>webhook_handler.py</summary>
<br>
<img src="/media/checkout-webhook-handler-py-validation.png">
</details>
<details>
<summary>webhooks.py</summary>
<br>
<img src="/media/checkout-webhooks-py-validation.png">
</details>

#### Home App
<details>
<summary>apps.py</summary>
<br>
<img src="/media/home-apps-py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="/media/home-urls-py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="/media/home-views-py-validation.png">
</details>

#### Products App
<details>
<summary>admin.py</summary>
<br>
<img src="/media/product-admin-py-validation.png">
</details>
<details>
<summary>apps.py</summary>
<br>
<img src="/media/products-apps-py-validation.png">
</details>
<details>
<summary>forms.py</summary>
<br>
<img src="/media/products-forms-py-validation.png">
</details>
<details>
<summary>models.py</summary>
<br>
<img src="/media/products-models-py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="/media/products-urls-py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="/media/products-views-py-validation.png">
</details>

#### Profiles App
<details>
<summary>apps.py</summary>
<br>
<img src="/media/profiles-apps-py-validation.png">
</details>
<details>
<summary>models.py</summary>
<br>
<img src="/media/profiles-models-py-validation.png">
</details>
<details>
<summary>urls.py</summary>
<br>
<img src="/media/profiles-urls-py-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="/media/profiles-views-py-validation.png">
</details>


### Manual Testing

* The website was tested on Google Chrome & Microsoft Edge.
* The website was viewed on a desktop computer and Moto G Power mobile phone.
* A large amount of manual testing was done to ensure all buttons are working correctly.
* A large amount of manual testing was done to ensure that the logic behind the game worked and the user experience is fulfilled.
* A large amount of manual testing was done to ensure that there were no bugs hindering the game and any progression.
* Family and friends were asked to review the website for a better understanding of the user experience.
* Dev Tools was used to test how the site looks on various screen sizes.
* Dev Tools Lighthouse was use to test the performance accessibility, best prectices and SEO of each page.
* JS Lint was used to ensure there are no major issues with the script.


| Feature/Test                                          | Expected Outcome.                                                                                                        | Result |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------ |
| Logo in Navbar.                                       | Redirect to Homepage.                                                                                                    | Pass.  |
| Nav Links.                                            | Redirect to relevant pages.                                                                                              | Pass.  |
| CTA Login button on Homepage.                         | Redirects to login page.                                                                                                 | Pass.  |
| Login Form - empty.                                   | Will not submit if empty fields.                                                                                         | Pass.  |
| Login Form - incorrect username.                      | Form submits but doesn't login, gives falsh message.                                                                     | Pass.  |
| Login Form - incorrect password.                      | Form submits but doesn't login, gives falsh message.                                                                     | Pass.  |
| Login Form - correct details.                         | Form submits and redirects user to relevant page for that user.                                                          | Pass.  |
| Register link on Log In Form.                         | Redirects to register page.                                                                                              | Pass.  |
| Register Form - empty.                                | Will not submit if empty fields.                                                                                         | Pass.  |
| Register Form - username exists.                      | Form submits but does not register user, error page with username already exists.                                        | Pass.  |
| Register Form - new user details.                     | Form submits adding new user and redirects to Homepage with flash message.                                               | Pass.  |
| Log In link on Register Form.                         | Redirects to Log In page.                                                                                                | Pass.  |
| Log Out Button.                                       | Logs user out, clears session and redirects to Homepage.                                                                 | Pass.  |
| Remember Me.                                          | Remember me checkbox remembers the users username when the page is refreshed.                                            | Pass.  |
| See Full Post CTA.                                    | Redirects to full post.html of specific post.                                                                            | Pass.  |
| Review Fields.                                        | All post fields can be filled out.                                                                                       | Pass.  |
| ReviewRequired Fields - No Completed.                 | Will not submit if required fields are empty.                                                                            | Pass.  |
| Review Submit CTA Button.                             | Submit button works , post successfully posted with flash message.                                                       | Pass.  |
| Review Edit CTA Button Visibility.                    | Review Owner Only Can See Edit CTA Button.                                                                               | Pass.  |
| Review Edit CTA Button - Functions.                   | Review owner can use button and takes them to the edit_post.html and are able to edit all post information.              | Pass.  |
| Review Edit Submit CTA Button.                        | Once edited , the post owner can submit the post and recieve a flash message of successful post.                         | Pass.  |
| Review Delete CTA Button Visibility.                  | Review Owner Only Can See Delete CTA Button.                                                                             | Pass.  |
| Review Delete CTA Button - Functions.                 | Review owner can use button and executes the modal pop up for confirmation.                                              | Pass.  |
| Reviews Visibility.                                   | Reviews are visible to users who clicked on specific post.                                                               | Pass.  |
| Review Delete CTA Button - Functions.                 | Review owner can use button and executes the modal pop up for confirmation.                                              | Pass.  |
| Delete Message.                                       | Delete button successfully deletes post/comment with flash message of confirmation, cancel button removes the modal.     | Pass.  |
| Type a non-existent page path.                        | Redirects to 404 page.                                                                                                   | Pass.  |
| 404 page                                              | Appears as should with navigation back to homepage.                                                                      | Pass.  |
| 404 page - home button.                               | Redirects to Homepage.                                                                                                   | Pass.  |
| 500 page                                              | Appears as should with navigation back to homepage.                                                                      | Pass.  |


### Lighthouse Report

#### Desktop analysis
<details>
<summary>Home Page
</summary>

![Homepage Screen Lighthouse Report](/media/homepage-dt-lighthouse.png)
</details>

<details>
<summary>Products Page
</summary>

![Create Post Screen Lighthouse Report](/media/products-page-dt-lighthouse.png)
</details>

<details>
<summary>Product Detail Page
</summary>

![Edit Post Screen Lighthouse Report)](/media/product-detail-dt-lighthouse.png)
</details>

<details>
<summary>Edit Review Page
</summary>

![Register Screen Lighthouse Report](/media/edit-review-m-lighthouse.png)
</details>

<details>
<summary>Basket Page
</summary>

![Login Screen Lighthouse Report](/media/basket-dt-lighthouse.png)
</details>

<details>
<summary>Checkout Page
</summary>

![Login Screen Lighthouse Report](/media/checkout-dt-lighthouse.png)
</details>

<details>
<summary>Checkout Success Page
</summary>

![Login Screen Lighthouse](/media/checkout-success-dt-lighthouse.png)
</details>

<details>
<summary>My Account
</summary>

![Login Screen Lighthouse Report](/media/my-account-dt-lighthouse.png)
</details>

<details>
<summary>Sign Up Page
</summary>

![Login Screen Lighthouse Report](/media/sign-up-dt-lighthouse.png)
</details>

<details>
<summary>Sign In Page
</summary>

![Login Screen Lighthouse Report](/media/login-dt-lighthouse.png)
</details>

<details>
<summary>Logout Page
</summary>

![Login Screen Lighthouse Report](/media/logout-dt-lighthouse.png)
</details>

#### Mobile analysis
<details>
<summary>Home Page
</summary>

![Homepage Screen Lighthouse Report](/media/homepage-m-lighthouse.png)
</details>

<details>
<summary>Products Page
</summary>

![Create Post Screen Lighthouse Report](/media/products-m-lighthouse.png)
</details>

<details>
<summary>Product Detail Page
</summary>

![Edit Post Screen Lighthouse Report)](/media/product-detail-m-lighthouse.png)
</details>

<details>
<summary>Edit Review Page
</summary>

![Register Screen Lighthouse Report](/media/edit-review-m-lighthouse.png)
</details>

<details>
<summary>Basket Page
</summary>

![Login Screen Lighthouse Report](/media/basket-m-lighthouse.png)
</details>

<details>
<summary>Checkout Page
</summary>

![Login Screen Lighthouse Report](/media/checkout-m-lighthouse.png)
</details>

<details>
<summary>Checkout Success Page
</summary>

![Login Screen Lighthouse](/media/checkout-success-m-lighthouse.png)
</details>

<details>
<summary>My Account
</summary>

![Login Screen Lighthouse Report](/media/my-account-m-lighthouse.png)
</details>

<details>
<summary>Sign Up Page
</summary>

![Login Screen Lighthouse Report](/media/sign-up-m-lighthouse.png)
</details>

<details>
<summary>Sign In Page
</summary>

![Login Screen Lighthouse Report](/media/login-m-lighthouse.png)
</details>

<details>
<summary>Logout Page
</summary>

![Login Screen Lighthouse Report](/media/logout-m-lighthouse.png)
</details>

---

## Deployment and local development

### Heroku

To deploy to Heroku:
1. In GitPod CLI, the root directory of the project, run:
    pip3 freeze --local > requirements.txt
    to create a requirements.txt file containing project dependencies.
2. In the Gitpod project workspace root directory, create a new file called Procfile, with capital 'P'.
    Open the Procfile. Inside the file, check that web: python3 app.py has been added when creating the file
    Save the file.
3. Push the 2 new files to the GitHub repository
4. Login to Heroku, select Create new app, add the name for your app and choose your closest region.
5. Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository and click 'connect'.
6. Navigate to the settings tab, click reveal config vars and input the following:

| Key | Value |
| :---: | :---: |
| DATABASE_URL | postgresql |
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET_KEY | mysecretkey |

Actual Enviroment variables not disclosed for security.

### GitHub Pages

GitHub Pages used to deploy live version of the website.
1. Log in to GitHub and locate [GitHub Repository Star Wars Discussion Blog](https://github.com/DarthKoder/narth_vad3r_merch)
2. At the top of the Repository(not the main navigation) locate "Settings" button on the menu.
3. Scroll down the Settings page until you locate "GitHub Pages".
4. Under "Source", click the dropdown menu "None" and select "Main" and click "Save".
5. The page will automatically refresh.
6. Scroll back to locate the now-published site [link](https://github.com/DarthKoder/narth_vad3r_merch) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [GitHub Repository Star Wars Discussion Blog](https://github.com/DarthKoder/narth_vad3r_merch)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.

### Local Clone

1. Log in to GitHub and locate [GitHub Repository Star Wars Discussion Blog](https://github.com/DarthKoder/narth_vad3r_merch)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

---

## Credits

### Code
 * Understanding some JavaScript concepts and code needed for certail aspects of the game [W3schools](https://www.w3schools.com/)
 * The README template was helpfully provided by my mentor Mitko at Code Institute 
 * Helping with writing and understanding python [Python Tutor](https://pythontutor.com/)
 * Helping with writing and understanding python and find code that was helpful to me [Python Docs](https://docs.python.org/3/contents.html)

### Content

 * All content was written by the developer.
 * [Color contrast checker](https://coolors.co/contrast-checker/112a46-acc8e5) was used to decide which colours would be used for the website.

### Media 

All Media used in the site and README is original.

---

## Acknowledgements
 * My mentor Mitko for helping me with ideas to improve the design and ways to build it. 
 * W3schools for the information online when needed. 
 * Python Tutor to help me write and understand python and debug any issues.
 * Slack community for encouragement and information.
 * My motivation for this project was my love for Star Wars and my love for streaming and wanted to build something for my online gaming community. 
<br><br>
