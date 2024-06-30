#Split words from string
import nltk
text='''Certainly! 🎥🌟

**"Kalki 2898 AD": A Sci-Fi Extravaganza with Hindu Mythology**

Director Nag Ashwin's *Kalki 2898 AD* is a visually stunning film that blends futuristic ideas with Hindu mythology. Starring Prabhas, Deepika Padukone, and Amitabh Bachchan, the movie takes place thousands of years after the Mahabharata war. In a dystopian world, Kashi becomes the last city ruled by Supreme Yaskin (played by Kamal Haasan). The rich thrive in the Complex, while the poor suffer. Bhairava (Prabhas), a bounty hunter, dreams of entering the Complex. Ashwattama (Amitabh Bachchan), from a different yuga, has a crucial role to play. Meanwhile, pregnant Sumathi (Deepika Padukone) escapes the Complex, setting in motion a chain of events that will change everything. With grand visuals and superlative performances, *Kalki 2898 AD* is a must-watch for fans of sci-fi and mythology¹². 🚀🎬
'''

split_words=nltk.word_tokenize(text)
print(split_words)


### output

['Certainly', '!', '🎥🌟', '*', '*', "''", 'Kalki', '2898', 'AD', "''", ':', 'A', 'Sci-Fi', 'Extravaganza', 'with', 'Hindu', 'Mythology', '*', '*', 'Director', 'Nag', 'Ashwin', "'s", '*', 'Kalki', '2898', 'AD', '*', 'is', 'a', 'visually', 'stunning', 'film', 'that', 'blends', 'futuristic', 'ideas', 'with', 'Hindu', 'mythology', '.', 'Starring', 'Prabhas', ',', 'Deepika', 'Padukone', ',', 'and', 'Amitabh', 'Bachchan', ',', 'the', 'movie', 'takes', 'place', 'thousands', 'of', 'years', 'after', 'the', 'Mahabharata', 'war', '.', 'In', 'a', 'dystopian', 'world', ',', 'Kashi', 'becomes', 'the', 'last', 'city', 'ruled', 'by', 'Supreme', 'Yaskin', '(', 'played', 'by', 'Kamal', 'Haasan', ')', '.', 'The', 'rich', 'thrive', 'in', 'the', 'Complex', ',', 'while', 'the', 'poor', 'suffer', '.', 'Bhairava', '(', 'Prabhas', ')', ',', 'a', 'bounty', 'hunter', ',', 'dreams', 'of', 'entering', 'the', 'Complex', '.', 'Ashwattama', '(', 'Amitabh', 'Bachchan', ')', ',', 'from', 'a', 'different', 'yuga', ',', 'has', 'a', 'crucial', 'role', 'to', 'play', '.', 'Meanwhile', ',', 'pregnant', 'Sumathi', '(', 'Deepika', 'Padukone', ')', 'escapes', 'the', 'Complex', ',', 'setting', 'in', 'motion', 'a', 'chain', 'of', 'events', 'that', 'will', 'change', 'everything', '.', 'With', 'grand', 'visuals', 'and', 'superlative', 'performances', ',', '*', 'Kalki', '2898', 'AD', '*', 'is', 'a', 'must-watch', 'for', 'fans', 'of', 'sci-fi', 'and', 'mythology¹²', '.', '🚀🎬']