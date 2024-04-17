# seed.py
from app import app
from models import db, Cupcake

def seed_database():
    print("Dropping all tables...")
    db.drop_all()
    print("Creating all tables...")
    db.create_all()

    print("Adding cupcakes...")
    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    db.session.add_all([c1, c2])
    db.session.commit()
    print("Cupcakes added successfully!")

if __name__ == '__main__':
    with app.app_context():
        seed_database()