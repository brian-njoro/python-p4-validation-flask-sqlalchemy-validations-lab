from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_phone_number(self,key,name):
        if not name:
            raise ValueError("please enter your name")
        return name
    
    @validates('/phone_number')
    def validate_phone_number(self,key,phone_number):
        #removing non-numerical characters 
        new_number = ''.join(filter(str.isdigit,phone_number))
        if len(new_number) != 10:
            raise ValueError("Phone number must consist of only 10 digits")
        return phone_number
    

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self,key,title):
        if not title:
            raise ValueError("Every post must have a title!")
        return title
    
    @validates('summary')
    def validate_summary(self,key,summary):
        if summary and len(summary) > 250:
            raise ValueError("post summaru cannot esxeed 250 characters!")
        
    @validates('content')
    def validate_content(self, key, content):
        if content and len(content) < 250:
            raise ValueError("Post content must be at least 250 characters long.")
        return content
    
    @validates('title')
    def validate_clickbait(self, key, title):
        bait_words = ["Won't Believe", "Secret", "Guess"]
        if not any(keyword in title for keyword in bait_words):
            raise ValueError("Post title must contain at least one clickbait keyword.")


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
