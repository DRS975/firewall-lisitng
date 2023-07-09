import xml.etree.ElementTree as ET
import psycopg2

def create_table_from_xml(xml_file, table_name):
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_user",
        password="your_password"
    )
    
    # Create a cursor
    cur = conn.cursor()

    # Read the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Get the tag names
    tag_names = set([child.tag for child in root.iter()])

    # Create the PostgreSQL table
    query = f"CREATE TABLE {table_name} (id SERIAL PRIMARY KEY"
    for tag_name in tag_names:
        query += f", {tag_name} TEXT"
    query += ");"
    cur.execute(query)
    conn.commit()

    # Insert values into the table
    for element in root.iter():
        query = f"INSERT INTO {table_name} ("
        query += ", ".join([tag_name for tag_name in tag_names])
        query += ") VALUES ("
        query += ", ".join([f"'{element.find(tag_name).text}'" if element.find(tag_name) is not None else "NULL" for tag_name in tag_names])
        query += ");"
        cur.execute(query)
        conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

# Example usage
create_table_from_xml("data.xml", "my_table")
