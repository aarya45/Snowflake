#Importing Session class from Snowpark library
from snowflake.snowpark.session import Session

#Create session object
def create_session_object():
    #Connection parameters
    connection_parameters = {
        "account" : "_account_identifier",
        "user": "_user_name",
        "password": "_password",
        "role": "_role",
        "Database": "_DB_NAME",
        "Schema": "_SCHEMA_NAME",
        "Warehouse": "_WAREHOUSE_NAME"
    }

    session = Session.builder.configs(connection_parameters).create()

    print(session)
    return session

session = create_session_object()

def create_dataframe(session):
    df_table = session.table("_TABLE_NAME")
    print("/n/n show() method output: ")
    df_table.show()
    print("/n/n collect() method output: ")
    collect_results = df_table.collect()
    print(collect_results)

create_dataframe(session)


    
