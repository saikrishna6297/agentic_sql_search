from database_setup.university_database import init_university_db
from database_setup.ecommerce_database import init_ecommerce_db


def initialize_databases():
    init_ecommerce_db()
    init_university_db()