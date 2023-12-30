# Django Book Shop E-commerce Website

This is a Django-based e-commerce website for a book shop. The website allows users to browse and purchase books, filter books by category, and manage their shopping cart using Django sessions. The project uses PostgreSQL as the database to store book information.

## Installation

1. Clone the repository to your local machine:

   ````
   git clone <git@github.com:salmaayad0/book-shop-django.git>
   ```

2. Navigate to the project directory:

   ````
   cd shop
   ```

3. Create and activate a virtual environment:

   ````
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the project dependencies:

   ````
   pip install -r requirements.txt
   ```

5. Set up the database:

   - Make sure you have PostgreSQL installed and running.
   - Create a new database for the project.
   - Update the database configuration in the `settings.py` file located in the `shop` directory. Modify the `DATABASES` section with your database credentials.

6. Apply the database migrations:

   ````
   python manage.py migrate
   ```

7. Load the initial book data:

   ````
   python manage.py loaddata initial_books.json
   ```

8. Start the development server:

   ````
   python manage.py runserver
   ```

9. Open your browser and access the website at [http://localhost:8000/](http://localhost:8000/).

## Usage

### Admin Panel

- Access the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/). Use your superuser credentials to log in.
- The admin panel allows you to manage book categories, authors, and other related information.

### Book Listing

- View all books: [http://localhost:8000/](http://localhost:8000/)
- View books by category: [http://localhost:8000/search/category-slug/](http://localhost:8000/search/category-slug/). Replace `category-slug` with the actual slug of the category.

### Book Details

- View a specific book: [http://localhost:8000/book/book-slug/](http://localhost:8000/book/book-slug/). Replace `book-slug` with the actual slug of the book.

### Shopping Cart

- View cart items: [http://localhost:8000/order/items/](http://localhost:8000/order/items/)
- Submit an order: [http://localhost:8000/order/submit/](http://localhost:8000/order/submit/)
- Delete an item from the cart: [http://localhost:8000/order/delete/](http://localhost:8000/order/delete/)
- Update the quantity of an item in the cart: [http://localhost:8000/order/update/](http://localhost:8000/order/update/)

### Media Files

- Access uploaded media files: [http://localhost:8000/media/](http://localhost:8000/media/)

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The project uses the Django web framework. You can find more information about Django in the [official documentation](https://docs.djangoproject.com/).
- The PostgreSQL database is used to store book information. For more details, refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/).
- The project also utilizes Django sessions for managing the shopping cart. You can learn more about Django sessions in the [official documentation](https://docs.djangoproject.com/en/3.2/topics/http/sessions/).

Feel free to customize and enhance the project according to your requirements. Happy coding!