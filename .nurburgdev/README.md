# URL Shortener Backend API (Python)

Build a URL shortener backend API for an e-commerce company using Python and FastAPI with PostgreSQL.

## Setup Instructions

### Database Setup

1. **Initialize the database schema**: Run the SQL script to create the required tables and indexes:
   ```bash
   psql -h devpostgresql -U devuser -d devdb -f src/db/init.sql
   ```

### Run the Application

```bash
cd src
python main.py
```

## API Endpoints

### Health Check
```
GET /health
```

### Create Auto-Generated Short URL
```
POST /api/short_url
```
**Request Body:**
```json
{
  "long_url": "https://www.myntra.com/sports-shoes/nike/nike-experience-run-11-womens-road-running-shoes/30739789/buy"
}
```
**Response:**
```json
{
  "key": "abcdefgh"
}
```

### Create Custom Short URL
```
POST /api/short_url/custom
```
**Request Body:**
```json
{
  "key": "summer-sales",
  "long_url": "https://www.myntra.com/sports-shoes/nike/nike-experience-run-11-womens-road-running-shoes/30739789/buy"
}
```
**Response:**
```json
{
  "key": "summer-sales"
}
```

### Redirect
```
GET /{key}
```
Redirects to the original long URL.