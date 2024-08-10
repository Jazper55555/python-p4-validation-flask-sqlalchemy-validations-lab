#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

from app import app
from models import db, Author, Post

import re


fake = Faker()

genres = [
    'Fiction',
    'Non-Fiction',
    'Horror',
    'Science Fiction',
    'Romance'
]

# def format_phone_number(phone_number):
#     # Remove all non-digit characters
#     digits = re.sub(r'\D', '', phone_number)

#     # Format the phone number as desired, e.g., (123) 456-7890
#     formatted_number = f"{digits[0:10]}"

#     return formatted_number

with app.app_context():

    Author.query.delete()
    Post.query.delete()

    authors = []
    for n in range(25):
        author = Author(name=fake.name(), phone_number='0123456789')
        authors.append(author)

    db.session.add_all(authors)
    posts = []
    for n in range(25):
        post = Post(title=fake.name(), content=fake.text(), category= rc(genres), summary=fake.text() )
        posts.append(post)

    db.session.add_all(posts)

    db.session.commit()