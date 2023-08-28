def positive_values(list_payment):
    list_positive = []
    positives = filter(lambda i: i > 0, list_payment)
    for i in positives:
        list_positive.append(i)
    return list_positive