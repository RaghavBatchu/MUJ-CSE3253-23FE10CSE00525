# Database Configuration Template

# Database Connection Configuration
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "devops_db",
    "username": "admin",
    "password": "your_secure_password_here",
    "pool_size": 10,
    "max_overflow": 20,
}

# Application Configuration
APP_CONFIG = {
    "debug": True,
    "environment": "development",
    "log_level": "INFO",
    "api_timeout": 30,
}

# AWS Configuration (if using AWS services)
AWS_CONFIG = {
    "region": "us-east-1",
    "access_key_id": "your_access_key",
    "secret_access_key": "your_secret_key",
    "s3_bucket": "your-bucket-name",
}

# Redis Configuration (for caching)
REDIS_CONFIG = {
    "host": "localhost",
    "port": 6379,
    "db": 0,
    "password": None,
}

# Logging Configuration
LOGGING_CONFIG = {
    "log_file": "app.log",
    "max_size": "10MB",
    "backup_count": 5,
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
}
