# 🚀 Backup Config System

A FastAPI-based backup configuration management system with user authentication, admin controls, and SMS notifications. This system allows administrators to manage backup configurations and users to access them securely.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Rate Limiting](#rate-limiting)
- [Error Handling](#error-handling)
- [Usage Examples](#usage-examples)

## ✨ Features

- **User Authentication**: Secure login system with unique keys
- **Admin Panel**: Full CRUD operations for configurations and users
- **User Access**: Read-only access to backup configurations
- **SMS Notifications**: Automatic SMS alerts for new user registrations
- **Rate Limiting**: Built-in protection against abuse
- **Database Integration**: Supabase backend for data persistence
- **Input Validation**: Comprehensive data validation using Pydantic

## 🛠 Tech Stack

- **Framework**: FastAPI
- **Database**: Supabase
- **Authentication**: Custom key-based system
- **Rate Limiting**: SlowAPI
- **SMS Service**: External SMS API integration
- **Validation**: Pydantic
- **Configuration**: Python-decouple

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd backup-config-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or using uv
   uv sync
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ADMIN_MOBILE=your_admin_mobile_number
   BASE_URL=your_sms_api_base_url
   API_TOKEN=your_sms_api_token
   SENDER_ID=your_sms_sender_id
   ```

4. **Run the application**
   ```bash
   python -m uvicorn server:app --reload
   ```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SUPABASE_URL` | Your Supabase project URL | Yes |
| `SUPABASE_KEY` | Your Supabase API key | Yes |
| `ADMIN_MOBILE` | Admin's mobile number for SMS notifications | Yes |
| `BASE_URL` | SMS API base URL | Yes |
| `API_TOKEN` | SMS API authentication token | Yes |
| `SENDER_ID` | SMS sender identification | Yes |

## 📚 API Documentation

The API is organized into three main route groups:

### 🔐 Authentication Routes (`/api/v1/auth`)

#### POST `/login`
Authenticate users with their unique login key.

**Rate Limit**: 5 requests per minute

**Request Body**:
```json
{
  "login_key": "string (min 8 characters)"
}
```

**Response**:
```json
{
  "name": "string",
  "user_type": "string"
}
```

**Error Responses**:
- `400`: Invalid login key format
- `401`: Unauthorized key
- `429`: Rate limit exceeded

### 👤 User Routes (`/api/v1/user`)

#### GET `/`
Retrieve all available backup configurations.

**Rate Limit**: 30 requests per minute

**Response**:
```json
{
  "success": true,
  "message": "Configs fetch done",
  "data": [
    {
      "id": "uuid",
      "config_name": "string",
      "config": "string"
    }
  ]
}
```

### 🔧 Admin Routes (`/api/v1/admin`)

#### GET `/`
Retrieve all backup configurations (admin view).

**Rate Limit**: 30 requests per minute

**Response**: Same as user GET route

#### POST `/`
Create a new backup configuration.

**Rate Limit**: 30 requests per minute

**Request Body**:
```json
{
  "config_name": "string (e.g., 'Airtel')",
  "config": "string (e.g., 'vless://...')"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Config creation success!!",
  "data": null
}
```

#### DELETE `/{id}`
Delete a specific backup configuration by ID.

**Rate Limit**: 30 requests per minute

**Parameters**:
- `id`: UUID of the configuration to delete

**Response**:
```json
{
  "success": true,
  "message": "Config deleted!",
  "data": null
}
```

#### POST `/add-client`
Add a new client to the system.

**Rate Limit**: 2 requests per minute

**Request Body**:
```json
{
  "client_name": "string (e.g., 'Dumidu')"
}
```

**Response**:
```json
{
  "success": true,
  "message": "client added!",
  "data": null
}
```

**Features**:
- Automatically generates a 6-character login key
- Sends SMS notification to admin with the new key
- Validates for duplicate client names

#### DELETE `/delete-client/{id}`
Delete a specific client from the system.

**Rate Limit**: 2 requests per minute

**Parameters**:
- `id`: UUID of the client to delete

**Response**:
```json
{
  "success": true,
  "message": "Client deleted!",
  "data": null
}
```

## 🚦 Rate Limiting

The system implements rate limiting to prevent abuse:

| Endpoint | Rate Limit | Purpose |
|----------|------------|---------|
| `/login` | 5/minute | Prevent brute force attacks |
| User/Admin GET | 30/minute | Prevent excessive data requests |
| Admin POST/DELETE | 30/minute | Prevent spam operations |
| Client management | 2/minute | Prevent rapid user creation/deletion |

## ⚠️ Error Handling

The system provides comprehensive error handling with appropriate HTTP status codes:

### Common Error Responses

```json
{
  "detail": "Error message description"
}
```

### Error Types

- **400 Bad Request**: Invalid input data, malformed UUIDs
- **401 Unauthorized**: Invalid login key
- **404 Not Found**: Resource not found
- **429 Too Many Requests**: Rate limit exceeded
- **500 Internal Server Error**: Server-side errors

## 💡 Usage Examples

### 1. User Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"login_key": "ABC123DEF"}'
```

### 2. Get Configurations (User)
```bash
curl -X GET "http://localhost:8000/api/v1/user/"
```

### 3. Create Configuration (Admin)
```bash
curl -X POST "http://localhost:8000/api/v1/admin/" \
  -H "Content-Type: application/json" \
  -d '{
    "config_name": "Airtel",
    "config": "vless://user@server:port?security=tls&type=ws"
  }'
```

### 4. Add New Client (Admin)
```bash
curl -X POST "http://localhost:8000/api/v1/admin/add-client" \
  -H "Content-Type: application/json" \
  -d '{"client_name": "John Doe"}'
```

### 5. Delete Configuration (Admin)
```bash
curl -X DELETE "http://localhost:8000/api/v1/admin/123e4567-e89b-12d3-a456-426614174000"
```

## 🔒 Security Features

- **Input Validation**: All inputs are validated using Pydantic schemas
- **Rate Limiting**: Prevents abuse and brute force attacks
- **UUID Validation**: Ensures proper UUID format for all ID parameters
- **SMS Notifications**: Secure delivery of login credentials
- **Error Handling**: Comprehensive error responses without exposing sensitive information

## 📝 Database Schema

The system uses Supabase with the following main entities:

- **Users**: Store client information and login keys
- **Configurations**: Store backup configuration data
- **User Types**: Distinguish between regular users and admins

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions, please open an issue in the repository or contact the development team.

---

**Note**: This system is designed for internal use and requires proper security measures when deployed in production environments.
