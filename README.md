# DRF E-commerce Platform

An advanced e-commerce platform built with Django and Django REST Framework (DRF). This project provides a robust backend solution for managing products, orders, users, and payments, with a focus on clean architecture, scalability, and security.

## Features

- **User Management**: Secure user registration, authentication (using JWT), and profile management.
- **Product Management**: CRUD operations for products with support for images and inventory management.
- **Shopping Cart**: Persistent shopping cart functionality for authenticated users.
- **Order Management**: Order creation, tracking, and management.
- **Payment Processing**: Integration with Stripe for secure payment processing.
- **Admin Interface**: Django admin integration for easy management of all entities.
- **API Documentation**: Automatically generated API documentation using DRF's built-in tools.
- **Security**: JWT-based authentication, secure password storage, and best practices for API security.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default, easily switchable to PostgreSQL, MySQL, etc.)
- **Authentication**: JWT (JSON Web Tokens) using `djangorestframework-simplejwt`
- **Payments**: Stripe API
- **Testing**: Django's built-in testing framework with DRF's API test tools

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShubhamNagure/drf-ecommerce-platform.git
   cd drf-ecommerce-platform/ecommerce
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Create a superuser to access the admin interface:
   ```bash
   python manage.py createsuperuser
   ```

7. Access the API at `http://127.0.0.1:8000/api/` and the admin interface at `http://127.0.0.1:8000/admin/`.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries or feedback, please reach out to `nagureshubham@gmail.com`.


   ```plaintext
   MIT License

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.

