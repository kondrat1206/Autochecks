from collections import Counter


def get_count_visits_from_ip(ips):
    ip_counter = Counter(ips)
    return ip_counter

def get_frequent_visit_from_ip(ip_list):
    ip_counter = Counter(ip_list)
    most_common_ip = ip_counter.most_common(1)[0]
    return most_common_ip