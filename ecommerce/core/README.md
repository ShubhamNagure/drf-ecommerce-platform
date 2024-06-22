Note: API's marked with * (asterisk) required admin access token.

### User Management

- **Register User***: `POST /api/register/`
- **List Users**: `GET /api/users/`
- **Retrieve User**: `GET /api/users/{id}/`
- **Update User***: `PUT /api/users/{id}/`
- **Partial Update User***: `PATCH /api/users/{id}/`
- **Delete User***: `DELETE /api/users/{id}/`
- **Login**: `POST /api/token/`
- **Refresh Token**: `POST /api/token/refresh/`
- **Logout**: `POST /api/token/blacklist/`

### Product Management

- **List Products**: `GET /api/products/`
- **Create Product***: `POST /api/products/`
- **Retrieve Product**: `GET /api/products/{id}/`
- **Update Product***: `PUT /api/products/{id}/`
- **Partial Update Product***: `PATCH /api/products/{id}/`
- **Delete Product***: `DELETE /api/products/{id}/`

### Order Management (if implemented)

- **List Orders**: `GET /api/orders/`
- **Create Order**: `POST /api/orders/`
- **Retrieve Order**: `GET /api/orders/{id}/`
- **Update Order***: `PUT /api/orders/{id}/`
- **Partial Update Order***: `PATCH /api/orders/{id}/`
- **Delete Order**: `DELETE /api/orders/{id}/`

### Cart Management (if implemented)

- **View Cart**: `GET /api/cart/`
- **Add to Cart**: `POST /api/cart/`
- **Update Cart Item**: `PUT /api/cart/{id}/`
- **Remove from Cart**: `DELETE /api/cart/{id}/`

### Category Management (if implemented)

- **List Categories**: `GET /api/categories/`
- **Create Category**: `POST /api/categories/`
- **Retrieve Category**: `GET /api/categories/{id}/`
- **Update Category**: `PUT /api/categories/{id}/`
- **Partial Update Category**: `PATCH /api/categories/{id}/`
- **Delete Category**: `DELETE /api/categories/{id}/`
