from setuptools import setup

setup(
    name='FastAPI_Docker',
    version='0.0.1',
    author='Ivan A.',
    author_email='ya.aif2002@yandex.ru',
    description='for kaspersky',
    install_requires=[
        'fastapi==0.70.0',
        'requests==2.26.0',
        'uvicorn==0.15.0'
    ],
    script=['app/main.py']
)