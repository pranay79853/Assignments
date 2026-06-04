class ReverseString:
    def reverse_words(self, text):
        words = text.split()
        reversed_text = " ".join(words[::-1])
        return reversed_text

# Example usage
obj = ReverseString()
string = input("Enter a string: ")
print("Reversed string:", obj.reverse_words(string))