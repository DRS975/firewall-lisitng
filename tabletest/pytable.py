def create_table(paragraph_file, attribute_file, output_file):
    # Read paragraphs from the first file
    with open(paragraph_file, 'r') as f:
        paragraphs = f.readlines()

    # Read attributes from the second file
    with open(attribute_file, 'r') as f:
        attributes = [attr.strip() for attr in f.readlines()]

    # Create a list to store the table rows
    table_rows = []

    # Process each paragraph and extract attribute values
    for paragraph in paragraphs:
        attr_values = {}
        for attr in attributes:
            attr_key = attr + ':'
            if attr_key in paragraph:
                start_index = paragraph.index(attr_key) + len(attr_key)
                end_index = paragraph.find(' ', start_index)
                if end_index == -1:
                    end_index = None
                attr_value = paragraph[start_index:end_index].strip()
                attr_values[attr] = attr_value

        # Add attribute values to the table rows
        table_row = '\t'.join([attr_values.get(attr, '') for attr in attributes])
        table_rows.append(table_row)

    # Prepare the table header
    table_header = '\t'.join(attributes)

    # Prepare the table data
    table_data = '\n'.join(table_rows)

    # Combine the header and data
    output_content = f"{table_header}\n{table_data}"

    # Write the output to the file
    with open(output_file, 'w') as f:
        f.write(output_content)


# Example usage
create_table("paragraphs.txt", "attributes.txt", "output.txt")
