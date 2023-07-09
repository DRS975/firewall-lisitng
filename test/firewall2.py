import datetime

# Read the input file and store the protocols in a list
def read_input_file(file_name):
    protocols = []
    with open(file_name, 'r') as file:
        for line in file:
            protocol = line.strip()
            protocols.append(protocol)
    return protocols

# Generate the set of commands for each protocol
def generate_commands(protocols):
    commands = []
    name=input("enter ip name")
    for i, protocol in enumerate(protocols):
        commands.append(f'edit {name} {i}')
        commands.append(f'set subnet {protocol}/32')
        commands.append(f'command messagereceived<{datetime.datetime.now().strftime("%d%b%Y")}>')
        if i < len(protocols) - 1:
            commands.append('next')
        else:
            commands.append('end')
    return commands

# Write the commands to the output file
def write_output_file(file_name, commands):
    with open(file_name, 'w') as file:
        file.write('\n'.join(commands))

# Main function to process the commands
def process_commands(input_file, output_file):
    protocols = read_input_file(input_file)
    commands = generate_commands(protocols)
    write_output_file(output_file, commands)

# Specify the input and output file names
input_file = input('enter input name as txt file')
output_file = input('enter name for output as txt')

# Process the commands
process_commands(input_file, output_file)
