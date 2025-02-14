if __name__ == '__main__':
    length = 800

    if length < 500:
        print("small")
    elif 500 <= length < 1000:
        print("medium")
    elif 1000 <= length < 2000:
        print("large")
    else:
        print("extra large")

    print("-"*30)
    is_premium_member = True
    days_registered = 400
    special_access_code = False

    if (is_premium_member and days_registered >365) or special_access_code:
        print("Access to the premium feature granted!")
    else:
        print("Access denied.")



