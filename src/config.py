"""Configuration management."""
import os


def get_api_key():
    return os.environ.get('API_KEY', 'default-key')


def get_database_url():
    return os.environ.get('DATABASE_URL', 'sqlite:///default.db')
