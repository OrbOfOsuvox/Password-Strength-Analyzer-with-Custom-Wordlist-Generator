from app.utils import leetspeak_variants, year_suffixes, capitalization_variants

def generate_wordlist(inputs):
    base_words = set()

    for item in inputs:
        item = item.strip()
        base_words.update(capitalization_variants(item))
        base_words.update(leetspeak_variants(item))

    final_words = set()
    for word in base_words:
        for suffix in year_suffixes():
            final_words.add(f"{word}{suffix}")
            final_words.add(f"{suffix}{word}")
        final_words.add(word)  # also include the base word

    return sorted(final_words)
