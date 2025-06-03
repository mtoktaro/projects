from sqlalchemy import create_engine, text

def execute_query(query, engine):
    
    
    with engine.connect() as connection:
        result = connection.execute(text(query))
        return result.fetchall()
