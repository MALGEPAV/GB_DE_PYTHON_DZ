long_str = """Jean-Baptiste Frédéric Isidor, Baron Thielemans
(29 April 1922 – 22 August 2016), known professionally as Toots Thielemans
([tuts tiləmans]), was a Belgian jazz musician. 
He was mostly known for playing the chromatic harmonica,
as well as his guitar and whistling skills, and composing.
According to jazz historian Ted Gioia, 
his most important contribution was in "championing the humble harmonica",
which Thielemans made into a "legitimate voice in jazz".
[2] He eventually became the "preeminent" jazz harmonica player.[3]
His first professional performances were with Benny Goodman's 
band when they toured Europe in 1949 and 1950. He emigrated to the U.S.
in 1951, becoming a citizen in 1957.
From 1953 to 1959 he played with George Shearing,
and then led his own groups on tours in the U.S. 
and Europe. In 1961 he recorded and performed live 
one of his own compositions, "Bluesette", which featured him playing guitar and whistling. 
In the 1970s and 1980s, he continued touring and recording,
 appearing with musicians such as Oscar Peterson, 
Ella Fitzgerald, Sarah Vaughan, Bill Evans, Dizzy Gillespie, Kenny Werner, Pat Metheny, Jaco Pastorius, Mina Mazzini, Elis Regina, Quincy Jones, George Shearing, Natalie Cole, Billy Joel, Paul Simon, and Paquito D'Rivera.
Thielemans recorded the soundtracks for The Pawnbroker (1964), 
Midnight Cowboy (1969), The Getaway (1972), Cinderella Liberty (1973),
The Sugarland Express (1974) and Looking for Mr. Goodbar (1977).
His harmonica theme song for the popular Sesame Street TV show was heard for 40 years. 
He often performed and recorded with Quincy Jones,
who once called him "one of the greatest musicians of our time."[4] 
In 2009 he was designated a Jazz Master by the National Endowment for the Arts, 
the highest honor for a jazz musician in the United States."""

long_str_cleared = "".join(list(map(lambda letter: " " if not letter.isalnum() else letter, long_str.lower())))
word_list = long_str_cleared.split()
word_set = set(word_list)
word_counts = [(word, word_list.count(word)) for word in word_set]
sorted_word_counts = sorted(word_counts, key=lambda pair: pair[1], reverse=True)
for pair in sorted_word_counts[0:10]:
    print(pair)
