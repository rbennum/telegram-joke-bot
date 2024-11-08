import random

jokes = [
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
    "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I used to play piano by ear, but now I use my hands.",
    "What did one hat say to the other? Stay here; I'm going on ahead.",
    "Why did the bicycle fall over? Because it was two-tired!",
    "I tried to catch some fog, but I mist.",
    "What’s orange and sounds like a parrot? A carrot.",
    "Why did the coffee file a police report? It got mugged.",
    "Why can’t you give Elsa a balloon? Because she’ll let it go!",
    "Why was the math book sad? It had too many problems.",
    "I told my computer I needed a break, and now it won’t stop sending me KitKat ads.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "How does a penguin build its house? Igloos it together!",
    "I told my boss I needed a pay raise; he said my pay was a joke, and I replied, 'Well, now it's funny.'",
    "What did the fish say when it hit the wall? Dam.",
    "Why don’t scientists trust atoms? Because they make up everything."
]

def get_random_joke():
    return random.choice(jokes)
