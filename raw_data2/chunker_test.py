def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


text = "I am a very, very helpful text"

for group in chunker(text, 7):
    print
    repr(group),
# 'I am a ' 'very, v' 'ery hel' 'pful te' 'xt'

print
'|'.join(chunker(text, 10))
# I am a ver|y, very he|lpful text

animals = ['cat', 'dog', 'rabbit', 'duck', 'bird', 'cow', 'gnu', 'fish']

for group in chunker(animals, 3):
    print
    group
# ['cat', 'dog', 'rabbit']
# ['duck', 'bird', 'cow']
# ['gnu', 'fish']
