# make_lee_wordlists_lee.py
#
# RULES:
# 1. Words starting with "lea" and NOT "learn*"/"lear*"/"leath*":
#       replace "lea" -> "lee"
#       leader  -> leeder
#       lease   -> leese
#       leaf    -> leef
#       lean    -> leen
#
# 2. Words starting with "legal":
#       replace leading "le" -> "lee"
#       legal   -> leegal
#       legally -> leegallee (because rule 3 also applies)
#
# 3. ALL OTHER WORDS that end with "ly":
#       change ending "ly" -> "lee"
#       quickly  -> quicklee
#       happily  -> happilee
#
# 4. Everything else stays EXACTLY the same.
#
# OUTPUT:
#   - lee_wordlist.txt : all words transformed (one per line, only new word)
#   - lee_changes.txt  : ONLY words that changed (one per line, only new word)

import os

INPUT_FILE = "wordlist.txt"
OUTPUT_LEE_FILE = "lee_list.txt"
OUTPUT_CHANGES_FILE = "lee_changes.txt"


def transform_word(word: str) -> str:
    """Apply Lee rules to a single word and return the transformed version."""
    w = word.strip()
    if not w:
        return ""

    lower = w.lower()

    # Rule 1: "lea" at start, BUT NOT learn/lear/leath family
    if lower.startswith("lea") and not lower.startswith(("learn", "lear", "leath")):
        # "lea" + rest -> "lee" + rest
        # leader -> leeder, lease -> leese, leaf -> leef, lean -> leen
        return "lee" + w[3:]

    # Rule 2: "legal" at start
    if lower.startswith("legal"):
        # "le" + rest -> "lee" + rest
        # legal -> leegal, legally -> leegal + ly (then rule 3 will hit ly)
        base = "lee" + w[2:]
        # Apply rule 3 if it ends with "ly"
        if base.lower().endswith("ly"):
            return base[:-2] + "lee"
        return base

    # Rule 3: other words that end with "ly" -> change to "lee"
    if lower.endswith("ly"):
        return w[:-2] + "lee"

    # Rule 4: everything else unchanged
    return w


def main():
    if not os.path.exists(INPUT_FILE):
        print("ERROR: wordlist.txt not found in this folder.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
        words = [line.strip() for line in f if line.strip()]

    transformed_words = []
    changed_words_only = []

    for w in words:
        new_w = transform_word(w)
        transformed_words.append(new_w)

        # Only record if actually changed
        if new_w != w:
            changed_words_only.append(new_w)

    # Write full transformed wordlist
    with open(OUTPUT_LEE_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(transformed_words))

    # Write only changed words, new form only
    with open(OUTPUT_CHANGES_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(changed_words_only))

    print("Done.")
    print("Created:")
    print(" -", OUTPUT_LEE_FILE, " (all words, transformed)")
    print(" -", OUTPUT_CHANGES_FILE, " (only changed words, new forms only)")


if __name__ == "__main__":
    main()

