def convert_to_time(number):
    sentence_hours = "hours"
    sentence_minutes = "minutes"
    if number < 60:
        if number == 1:
            sentence_minutes = "minute"
        return f"{number} {sentence_minutes}."
    else:
        hours = number // 60
        if hours == 1:
            sentence_hours = "hour"

        minutes = number % 60
        if minutes == 1:
            sentence_minutes = "minute"

    return f"{hours} {sentence_hours}, {minutes} {sentence_minutes}."


def main():
    print(convert_to_time(61))


if __name__ in "__main__":
    main()
