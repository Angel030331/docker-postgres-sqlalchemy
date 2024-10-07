from sqlalchemy import create_engine, insert, text
import time

time.sleep(5)

engine = create_engine("postgresql+psycopg2://postgres:postgres@db:5432/DB")
conn = engine.connect()
query=text("INSERT INTO identity (_name, surname) VALUES ('Michel', 'Palefrois'), ('Renaud', 'Bertop');")
conn.execute(query)
conn.commit()

print('done')

# use the SQLAlchemy library to access our Postgres database with Python

# test services
# docker-compose build && docker-compose up -d
    # Now you can connect database with software like PGAdmin to visualize it. 
    # Database is up at http://localhost:5432 and you can connect with credentials sets in your docker-compose.yml file.