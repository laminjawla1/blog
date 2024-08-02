import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "ef05770be795d87d0ca4aca5efd8f9733b5bb7b5aded441fc5f6f433f4dce3c4"
    DEBUG = True