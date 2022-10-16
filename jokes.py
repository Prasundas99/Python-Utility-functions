# Importing Pyjokes to get random jokes
import pyjokes

# Function to print jokes
def print_joke(language, category):
    # Using the get_jokes method to fetch a joke
    joke = pyjokes.get_joke(language, category)
    print(joke)
    return joke

# Calling the function
try:
    print_joke("en", "neutral") # Neutral Jokes
    print_joke("en", "chuck") # Chuck Norris Jokes
except:
    raise Exception("Some Error Occured!")
