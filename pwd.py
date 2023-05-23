import sys

sys.setrecursionlimit(10**6)

options = {
    'f': '',
    'h': False,
    'o': '',
    'help': False,
    'output': '',
    'vvv': None,
    'date': None
}

banner_text = '''

    ██████╗░░██╗░░░░░░░██╗██████╗░
    ██╔══██╗░██║░░██╗░░██║██╔══██╗
    ██████╔╝░╚██╗████╗██╔╝██║░░██║
    ██╔═══╝░░░████╔═████║░██║░░██║
    ██║░░░░░░░╚██╔╝░╚██╔╝░██████╔╝
    ╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═════╝░
    1.2 https://github.com/sethvoid/pwd

    +-----------------------------------------------------------------------------------------+
    | Please do not use in military or secret service organizations, or for illegal purposes. |
    +-----------------------------------------------------------------------------------------+

    Pwd usage:
    --file       Wordlist file (required)
    --output     Name of output file
    --vvv        Verbose mode (some nice information)
    --help       Display what you are currently looking at.


'''

def output(message, status='[INFO]'):
    global options

    if options['vvv'] is not None or status == '[ERROR]':
        print(status, message)

def counter_show(count):
    sys.stdout.write("\rProcessed: {}  ".format(count))
    sys.stdout.flush()

def load_word_list(file_path):
    word_list = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.replace('.', '')
            line = line.replace(' ', '')
            line = line.replace('\t', '')
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            word_list.append(line)
    output('Word list loaded.')
    return word_list

def generate_payload(word_list, joiners, substitution_array, common_numbers, output_file):
    count = 0
    for depth1 in word_list:
        pre_payload = []
        pre_payload.append(depth1.upper())
        pre_payload.append(depth1.lower())
        pre_payload.append(depth1.capitalize())
        for depth2 in word_list:
            if depth2 == depth1:
                continue
            pre_payload.append(depth1.upper() + depth2.upper())
            pre_payload.append(depth1.upper() + depth2.lower())
            pre_payload.append(depth1.lower() + depth2.upper())
            pre_payload.append(depth1.lower() + depth2.lower())
            pre_payload.append(depth1.capitalize() + depth2.upper())
            pre_payload.append(depth1.capitalize() + depth2.lower())
            pre_payload.append(depth1.capitalize() + depth2.capitalize())
            for join in joiners:
                pre_payload.append(depth1.upper() + join + depth2.upper())
                pre_payload.append(depth1.lower() + join + depth2.lower())
                pre_payload.append(depth1.upper() + join + depth2.upper())
                pre_payload.append(depth1.lower() + join + depth2.lower())
                pre_payload.append(depth1.upper() + join + depth2.upper())
                pre_payload.append(depth1.capitalize() + join + depth2.lower())
                pre_payload.append(depth1.capitalize() + join + depth2.capitalize())
        for node in pre_payload:
            working_node = ''
            node_split = list(node)
            for letter in node_split:
                if letter in substitution_array:
                    letter = substitution_array[letter]
                working_node += letter
            if node != working_node:
                pre_payload.append(working_node)
        for word in pre_payload:
            with open(output_file, 'a') as file:
                file.write(word + '\n')
                for y in range(1900, int(datetime.now().year) + 1):
                    file.write(word + str(y) + '\n')
                    count += 1
                    counter_show(count)
                for common_number in common_numbers:
                    file.write(word + common_number + '\n')
                    count += 1
                    counter_show(count)
            output('[' + depth1 + '] word iteration complete.')
        del pre_payload

def main():
    global options

    if '-f' in sys.argv:
        options['f'] = sys.argv[sys.argv.index('-f') + 1]
    if '--file' in sys.argv:
        options['f'] = sys.argv[sys.argv.index('--file') + 1]
    if '-h' in sys.argv:
        options['h'] = True
    if '--help' in sys.argv:
        options['help'] = True
    if '-o' in sys.argv:
        options['o'] = sys.argv[sys.argv.index('-o') + 1]
    if '--output' in sys.argv:
        options['o'] = sys.argv[sys.argv.index('--output') + 1]
    if '-vvv' in sys.argv:
        options['vvv'] = True
    if '--date' in sys.argv:
        options['date'] = True

    if options['h'] or options['help']:
        return

    if options['f'] == '':
        output('Missing parameter: --file', '[ERROR]')
        return
    if options['o'] == '':
        output('Missing parameter: --output', '[ERROR]')
        return

    word_list_file = options['f']
    output_file = options['o']

    if not os.path.exists(word_list_file):
        output('Missing word file.', '[ERROR]')
        return

    joiners = [
        '.',
        '_',
        '-',
        '=',
        '/',
        '\\',
        '#',
        '@',
        '~',
        ',',
        '|'
    ]

    substitution_array = {
        's': '$',
        'e': '3',
        'l': '1',
        'i': '!',
        'a': '@',
        't': '7',
        'o': '0'
    }

    common_numbers = [
        '1111',
        '!!!!',
        '2222',
        '3333',
        '4444',
        '5555',
        '6666',
        '7777',
        '8888',
        '9999',
        '0000',
        '1234',
        '!234',
        '432!',
        '432!',
        '123',
        '!23',
        '321',
        '32!',
        '12',
        '!2',
        '21',
        '2!',
        '1',
        '!',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0'
    ]

    output(banner_text)
    output('Loading word list')
    word_list = load_word_list(word_list_file)
    output('Starting run')
    generate_payload(word_list, joiners, substitution_array, common_numbers, output_file)
    output('Script complete {} seconds'.format(time.time() - start))

if __name__ == '__main__':
    main()
