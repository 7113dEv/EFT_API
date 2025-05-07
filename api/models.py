from api import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    created_at = db.Column(db.Date)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }
    



# with app.app_context:
#     rows = Post.query.all()
#     user = Post.query.filter_by(username="root").first()
#     print(f"User: {user}\nRows: {rows}")