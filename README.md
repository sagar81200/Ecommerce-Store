Clone the repo using 
git clone https://github.com/sagar81200/Ecommerce-Store.git

Create and Activate a Virtual Environment:

python -m venv venv
On MAC: source venv/bin/activate  
On Windows: venv\Scripts\activate

install all required packages listed in the requirements.txt file:
pip install -r requirements.txt

run migrtion:
python manage.py migrate

Start the Development Server:
python manage.py runserver


Endpoints :-

GET- http://127.0.0.1:8000/store/products/
To list All the Products

POST - http://127.0.0.1:8000/store/products/
To create new Product

GET - http://127.0.0.1:8000/store/products/<product_id>
To get a specific product

GET- http://127.0.0.1:8000/store/category/
To get all the categories

POST - http://127.0.0.1:8000/store/category/
To create new category 

GET- http://127.0.0.1:8000/store/category/1/
To get a specific category

GET - http://127.0.0.1:8000/store/products/expensive-product/
To get the most expensive product

PATCH - http://127.0.0.1:8000/store/products/<product_id>/update-stocks/
To update the stocks of a product

