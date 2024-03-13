import pandas as pd
from sqlalchemy import create_engine, inspect

# MySQL database connection parameters
host = 'localhost'
user = 'root'
password = '20206296'
database = 'classicmodels'

# Create a MySQL database connection
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

# Use SQLAlchemy's inspector to get information about the database
inspector = inspect(engine)

# Create an Excel writer
excel_file_path = 'database_schema.xlsx'
with pd.ExcelWriter(excel_file_path) as writer:
    # Loop through tables and write schema information to Excel
    for table_name in inspector.get_table_names():
        table_df = pd.DataFrame(inspector.get_columns(table_name))
        foreign_keys = inspector.get_foreign_keys(table_name)
        if not table_df.empty:
            table_df.to_excel(writer, sheet_name=table_name, index=False)
        if foreign_keys:
            fk_df = pd.DataFrame([{'Foreign Key': fk['referred_columns'][0], 'References': fk['referred_table']} for fk in foreign_keys])
            fk_df.to_excel(writer, sheet_name=f'{table_name}_foreign_keys', index=False)

print(f'Database schema exported to Excel file: {excel_file_path}')
