# FastAPIStore

An educational e-commerce backend built with **FastAPI, SQLAlchemy and Alembic**.

The project demonstrates a modular API structure for authentication,
users, product catalogs, images and reviews.

## Features

- User and authentication API modules
- Categories and subcategories
- Product management
- Product images
- Product reviews
- Admin interface integration
- Database migrations with Alembic
- Docker Compose and nginx configuration

## Technology Stack

| Area | Technologies |
| --- | --- |
| Language | Python |
| API framework | FastAPI |
| Validation | Pydantic |
| Database access | SQLAlchemy |
| Migrations | Alembic |
| Admin interface | SQLAdmin |
| Deployment configuration | Docker, Docker Compose, nginx |

A PostgreSQL driver is included in the dependencies.
The database connection must be configured before startup.

## Project Structure

```text
FastAPIStore/
├── main.py             # Application entry point
├── mysite/             # Application modules
├── migrations/         # Database migrations
├── nginx/              # Reverse proxy configuration
├── alembic.ini         # Alembic configuration
├── Dockerfile
├── docker-compose.yml
└── req.txt             # Python dependencies
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/minbaevv/FastAPIStore.git
cd FastAPIStore
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r req.txt
```

### 4. Configure the database

Review the application's database configuration and the Alembic
environment. Set the required local connection parameters and make sure
the database is available.

Do not commit passwords, tokens or real user data to the repository.

### 5. Apply migrations and start the API

After configuring the database:

```bash
alembic upgrade head
python main.py
```

These instructions are based on the repository structure and entry point.
A complete clean-environment setup still needs to be verified.

## Development Priorities

- Document the exact environment variables and add a safe `.env.example`
- Verify authentication and object-level permissions
- Add or extend API tests for validation and error handling
- Check migrations against a clean database
- Verify the Docker Compose startup procedure
- Configure continuous integration

## Project Status

This is a learning project, not a production-ready store.
The presence of an API module or deployment configuration does not
guarantee that all scenarios have been tested.

## Attribution and License

If parts of this project follow a course, tutorial or another repository,
retain the original attribution and document the changes made.

No reuse license is declared here. Check the repository's licensing
before redistributing its code.

## Author

**Kubanychbek Duishekeev**

[GitHub](https://github.com/minbaevv) ·
[LinkedIn](https://www.linkedin.com/in/kubanychbek-duishekeev-7b9872427/) ·
[Telegram](https://t.me/d_kubanychbek) ·
[Gmail](mailto:duishekeevkubanychbek@gmail.com)
