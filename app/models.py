from app import app, db

# Define User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(10), default="user")  # "user" or "admin"

# Define CashRequest Model
class CashRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default="pending")  # pending, approved, rejected
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# Ensure database tables are created inside the app context
with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")
