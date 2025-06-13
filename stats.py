def count_words(contents):
    return len(contents.split())

def count_letters(contents):
    result = {}
    for l in contents:
        l = l.lower()
        if l.isalpha():  # Only count alphabetic characters
            if l not in result:
                result[l] = 0
            result[l] += 1
    return result

def sort_by_value(contents):
    return dict(sorted(contents.items(), key=lambda x: x[1], reverse=True))

    