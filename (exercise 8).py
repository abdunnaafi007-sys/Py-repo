class StringReverser:
    def __init__(self, text):
        self.text = text
        
    def reverse_words(self):
        # Split the string into words, reverse the list, and join them back
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

# Example usage
input_string = input("Enter a sentence: ")
reverser = StringReverser(input_string)
result = reverser.reverse_words()
print("Reversed sentence word by word:", result)
