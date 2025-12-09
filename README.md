Lee Language

A playful phonetic extension of English where “-ly” becomes “-lee.”

Lee is a transformation system for English words that modifies specific endings to create a distinct, fun, and recognizable variant of the language. It is easy to learn, easy to extend, and simple to implement programmatically.

🌟 What Is Lee?

Lee is an alternate phonetic spelling language derived from English.
Its core principle is:

Rule 1: Any word ending in “ly” becomes “lee”.

Examples:

legally → leegalee

definitely → definitelee

literally → literallee

clearly → clearlee

This single rule makes Lee instantly readable while giving every word a signature style.

You can optionally expand Lee with more rules over time, but this repo starts with the foundational system.

📘 Core Rules
1. Replace -ly with -lee

If a word ends in ly, change it to lee.

quickly → quicklee  
normally → normallee  
rarely → rarelee  
simply → simplyee (double-y effect preserved)

2. Keep the rest of the word intact

Lee is not a full transliteration system — only the suffix changes.

📄 Wordlist

The repository includes a lee-wordlist.txt containing one Lee-converted word per line.
This allows developers to:

generate corpora

use in games

build auto-translators

test phonetic models

create fun text filters

All words follow the standard Lee transformation rule.

💻 Example: Converting English → Lee in Code
JavaScript
function toLee(word) {
  if (word.endsWith("ly")) {
    return word.slice(0, -2) + "lee";
  }
  return word;
}

Python
def to_lee(word):
    return word[:-2] + "lee" if word.endswith("ly") else word

📦 Repository Structure
/
├─ README.md
├─ lee-wordlist.txt
├─ scripts/
│  ├─ convert.py      # Convert any text into Lee
│  ├─ toLee.js        # JS converter function/module

🧪 Example Usage

Input:

I definitely and legally approve this message.


Output:

I definitelee and leegalee approve this message.

🚀 Contribute

Want to expand Lee?
You can:

add more words

propose new phonetic rules

submit scripts (Python, JS, Go)

help build a full Lee dictionary

Pull requests are welcome!

📜 License

MIT — free to use, remix, and build upon.
