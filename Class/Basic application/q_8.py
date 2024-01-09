class Reverse:
    @staticmethod
    def reverse_words(s):
        return ' '.join(reversed(s.split()))


print(Reverse().reverse_words('hello .py'))
