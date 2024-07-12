from fastapi import FastAPI


from models import recreate_postgres_tables
recreate_postgres_tables()

app = FastAPI(
    title="Demo App"
)
