## Aho Corasick Algorithm
- It is a string matching algorithm for locating all the occurences of strings from a given list of strings in a text given.
- It uses a trie structure for optimizing the lookup.
- First step involves creating the trie with the fail over state for the mismatches.
- Which can be followed by lookup in a single pass.
- Complexity : `(length_of_list) + (length_of_string_to_search_in) + (number_of_occurences_found)` 
