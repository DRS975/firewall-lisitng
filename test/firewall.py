import datetime

def process_commands(input_file):
    protocols = []
    
    with open(input_file, 'r') as file:
        protocols = [line.strip() for line in file.readlines()]

    command_list = []
    last_protocol_index = min(len(protocols), 1500) - 1

    a = 0
    b = 0

    for i, protocol in enumerate(protocols):
        command_list.append(f"edit name{a}/{b}")
        command_list.append(f"set subnet {protocol}/32")
        command_list.append(f"command messagereceived<{datetime.datetime.now().strftime('%d%b%Y')}>")
        if i != last_protocol_index:
            command_list.append("next")
        
        b += 1
        if b > 1500:
            b = 0
            a += 1

    command_list.append("end")

    return command_list

def save_output(output_file, commands):
    with open(output_file, 'w') as file:
        file.write('\n'.join(commands))

input_file = "ipinput.txt"
output_file = "outputtestmega.txt"

commands = process_commands(input_file)
save_output(output_file, commands)
