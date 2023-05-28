# Product Information API

This project implements an API for fetching and managing product information. It includes various endpoints to fetch product details, comments, apply filters, and retrieve paginated product lists.

## Features

- Fetch product information from an external API
- Fetch comments for a specific product
- Provide filter options for product listing
- Retrieve paginated product lists with filtering and pagination

## Installation

1. Clone the repository:

```bash
git clone https://github.com/manishkrojha0/product-info-django.git

2. Create a new virtual environment:
```bash
python -m venv venv

3. Move to virtual environment:
- for mac/linux:- ```source venv/bin/activate
- for windows:- ```venv/Scripts/activate

3. Install project dependencies 
```bash
pip install -r requirements.txt

4. Run the migrations file by command.
```bash
python manage.py migrate

5. Important note - Please configure your database and keep your secrets keys in .env folder.

6. Run the application 
```bash
python manage.py runserver


## Usage

    - Use the following API endpoints to interact with the application:
        Fetch product information: /api/fetch-products/
        Fetch comments for a product: /api/fetch-comments/
        Filter product list: /api/product-filters/
        Paginated product list: /api/product-list/

    Access the API endpoints using a tool like cURL, Postman, or any other API testing tool.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
