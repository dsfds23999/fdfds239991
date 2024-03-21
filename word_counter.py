def count_words(text):
    """
    Count the occurrences of each word in the given text.
    
    Args:
        text (str): The input text.
        
    Returns:
        dict: A dictionary where keys are unique words and values are their counts.
    """
    words = text.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word
