# eCom

The dataset was found at https://www.kaggle.com/datasets/PromptCloudHQ/flipkart-products
Trimmed the dataset down to a record size of under 7,000. The dataset was trimmed in a way 
to distribute over 5 different product categories. 


The database design was done using draw.io with multiple tables linked together.
The database schema was implemented using django models and then the data parsed afterwards. 
The parsing code also included some error handling to handle inconsistencies in the dataset.
Designed a sketch mockup of the application frontend on paper
Implemented the logic for the application in a step-wise manner. Solving problems and tackling 
challenges on the way to making the application work. 


Paginator was used to divide the data sent to the frontend pages into pages of 51 each per page. 
The application includes authentication using a login form. 
New users can register new accounts using the signup link on the login page.
Behave was used to foster the Behavioural Driven Development procedure. 

The application is deployed at ecom-samshop.herokuapp.com. I, however, observed that the product
images do not load on Google chrome when accessed via the heroku link. This works quite fine on
Safari.
