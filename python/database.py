from sqlalchemy import create_engine
from config import DATABASE

DATABASE_URL = (
    f"postgresql+psycopg2://{DATABASE['USER']}"
    f"@{DATABASE['HOST']}:{DATABASE['PORT']}"
    f"/{DATABASE['DATABASE']}"
)

engine = create_engine(DATABASE_URL)