from difflib import get_close_matches

def fuzzy_match(query, options, cutoff=0.7):
    """
    Return the closest match to query from options using fuzzy matching.
    :param query: string to search
    :param options: list of strings to search in
    :param cutoff: similarity threshold (0-1)
    """
    matches = get_close_matches(query, options, n=1, cutoff=cutoff)
    return matches[0] if matches else None