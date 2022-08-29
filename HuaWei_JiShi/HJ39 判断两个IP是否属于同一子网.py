def check_ip(ip):
    ip = ip.split('.')
    if len(ip) != 4:
        return False
    for num in ip:
        if 0 <= int(num) <= 255:
            continue
        else:
            return False
    return True


def str2bin(ip):
    bin_ip = ''
    ip = ip.split('.')
    for num in ip:
        num = str(bin(int(num)))[2:]
        num = '0' * (8 - len(num)) + num
        bin_ip += num
    bin_ip = '0' * (32 - len(bin_ip)) + bin_ip
    return bin_ip


def check_mask(mask):
    if check_ip(mask):
        s = str2bin(mask)
        if s.rfind('1') + 1 == s.find('0'):
            return True
        else:
            return False
    else:
        return False


def is_same(ip_1, ip_2, mask):
    a = int(str2bin(ip_1), 2)
    b = int(str2bin(ip_2), 2)
    c = int(str2bin(mask), 2)

    if a & c == b & c:
        return True
    else:
        return False


while True:
    try:
        mask = input()
        ip_1 = input()
        ip_2 = input()
        if check_mask(mask) and check_ip(ip_1) and check_ip(ip_2):
            if is_same(ip_1, ip_2, mask):
                print(0)
            else:
                print(2)
        else:
            print(1)
    except:
        break