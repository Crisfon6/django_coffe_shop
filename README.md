# Coffee Shop

This is a Django-based web application for managing a coffee shop. The application allows users to view products, place orders, and manage their accounts.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Static Files](#static-files)
- [License](#license)

## Features

- User authentication and authorization
- Product listing and management
- Order placement and management
- REST API for products and orders
- Responsive design using Tailwind CSS

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/coffe_shop.git
    cd coffe_shop
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

## Configuration

1. Create a `.env` file in the root directory of the project and add the following environment variables:

    ```dotenv
    DJANGO_DB_ENGINE="django.db.backends.mysql"
    DJANGO_DB_NAME="crisnciv_coffe_shop_db"
    DJANGO_DB_USER="crisnciv_coffe_shop_user"
    DJANGO_DB_PASSWORD="]un$xEu$v)9K"
    DJANGO_DB_HOST="127.0.0.1"
    DJANGO_DB_PORT="5522"
    DJANGO_DB_URL="mysql://crisnciv_coffe_shop_user:]un$xEu$v)9K@127.0.0.1:5522/crisnciv_coffe_shop_db"
    DJANGO_TEST_DB_URL="mysql://crisnciv_coffe_shop_user:]un$xEu$v)9K@127.0.0.1:5522/crisnciv_test_coffe_shop_db"
    ```

2. Update the `settings.py` file to read the environment variables:

    ```python
    import os
    from pathlib import Path
    import environ

    BASE_DIR = Path(__file__).resolve().parent.parent
    env = environ.Env()
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    DATABASES = {
        'default': env.db('DJANGO_DB_URL'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION'"
        }
    }

    if 'test' in sys.argv:
        DATABASES['default'] = env.db('DJANGO_TEST_DB_URL')
        DATABASES['default']['TEST'] = {
            'NAME': 'crisnciv_test_coffe_shop_db',
        }
    ```

## Running the Application

1. Start the development server:

    ```sh
    python manage.py runserver
    ```

2. Open your web browser and go to `http://127.0.0.1:8000/`.

## Running Tests

1. To run the tests, use the following command:

    ```sh
    python manage.py test
    ```

## Static Files

The project uses static files for the admin interface and other parts of the application. These files are located in the `staticfiles` directory.

### Admin Static Files

- The admin static files include JavaScript libraries like [xregexp.js](http://_vscodecontentref_/0) and [select2.full.js](http://_vscodecontentref_/1).
- The icons used in the admin interface are taken from Font Awesome.

### License for Admin Icons

All icons are taken from Font Awesome (https://fontawesome.com/) project. The Font Awesome font is licensed under the SIL OFL 1.1:
- https://scripts.sil.org/OFL

SVG icons source: https://github.com/encharm/Font-Awesome-SVG-PNG
Font-Awesome-SVG-PNG is licensed under the MIT license (see file license in the current folder).

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.