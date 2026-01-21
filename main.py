#!/usr/bin/env python3
"""
Main Application Entry Point
"""

from config import APP_CONFIG, DB_CONFIG

def main():
    """Main function to start the application"""
    print("Starting DevOps Application...")
    print(f"Environment: {APP_CONFIG.get('environment')}")
    print(f"Debug Mode: {APP_CONFIG.get('debug')}")
    print(f"Connecting to database at {DB_CONFIG.get('host')}:{DB_CONFIG.get('port')}")
    print(f"Database: {DB_CONFIG.get('database')}")
    print("Application started successfully!")

if __name__ == "__main__":
    main()
