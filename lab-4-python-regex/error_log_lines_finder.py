import re


def find_error_log_lines():
    regex = re.compile(
        r'(^.*\[01/Jul/1995:03:(3[5-9]|4[0-9]|5[0-4]):[0-5][0-9] .*(4[0-9][0-9]|5[0-9][0-9]) -)')
    error_log_lines = []

    file = open('access_log_Jul95')
    for line in file:
        for match in re.finditer(regex, line):
            error_log_lines.append(match.group())
    return error_log_lines


def get_addresses_from_log_lines(log_lines):
    list_of_addresses = []
    regex = re.compile(r'((?<=GET ).+?(?=[ H]|[ \"]))')

    for one_line in log_lines:
        for match in re.finditer(regex, one_line):
            list_of_addresses.append(match.group())
    return list_of_addresses


def find_unique_addresses(addresses):
    list_of_unique_addresses = []

    for one_address in addresses:
        if one_address not in list_of_unique_addresses:
            list_of_unique_addresses.append(one_address)
    return list_of_unique_addresses


if __name__ == "__main__":
    found_log_lines = find_error_log_lines()
    print('Found requests with status codes 4XX-5XX:', len(found_log_lines), '\n')
    for request in found_log_lines:
        print(request)
    unique_addresses = find_unique_addresses(get_addresses_from_log_lines(found_log_lines))
    print('\nUnique addresses there:', len(unique_addresses), '\n')
    for address in unique_addresses:
        print(address)
