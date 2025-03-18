# Task 1: Hello
def hello():
    return "Hello!"

print(hello())


# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

print(greet("Olga"))


#Task 3: Calculator
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation."
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"   
    
print(calc(10, 5))  
print(calc(150, 0, "divide"))  
print(calc("Olga", "Olga"))  


# Task 4: Data Type Conversion
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
            case _:
                return "Invalid data type requested."
    except ValueError:
        return f"You can't convert {value} into a {data_type}."   

print(data_type_conversion("123", "int"))
print(data_type_conversion("Olga", "float"))


#Task 5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ValueError):
        return "Invalid data was provided."


print(grade(85, 90, 68)) 
print(grade(97, 95, 96))  
print(grade("nonsense", 60, 90))  


#Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

print(repeat("Hello", 3)) 
print(repeat("Olga", 1))    


#Task 7: Student Scores, Using **kwargs
def student_scores(mode, **kwargs):
    try:
        if not kwargs:
            return "No student data provided."  
             
        if mode == "best":
            return max(kwargs, key=kwargs.get) 
        elif mode == "mean":
            return sum(kwargs.values()) / len(kwargs) 
        else:
            return "Invalid mode. Use 'best' or 'mean'."
    except (TypeError, ValueError):
        return "Invalid data was provided."

print(student_scores("best", Olga=95, Nik=88, Tom=92))  
print(student_scores("mean", Olga=95, Nik=88, Tom=92))  
print(student_scores("best"))  
print(student_scores("mean", Olga="A", Nik=88))  


#Task 8: Titleize, with String and List Operations
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    
    words = text.split()  # Split text into a list of words
    if not words:  
        return ""  # Return an empty string if input is empty

    # Capitalize the first and last word, and apply rules to others
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()

    return " ".join(words)  # Join the words back into a string

print(titleize("raleigh is the best city")) 
print(titleize("the lion king"))  
print(titleize("i see the cat"))  
print(titleize(""))  


# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    # Create the result string by checking each letter in the secret
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print(hangman("apple", "ab"))   
print(hangman("home", "eph"))  


# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    vowels = "aeiou"
    result = []

    for word in text.split():  # Split the sentence into words
        if word[0] in vowels:
            result.append(word + "ay")  # Rule 1: Starts with a vowel
        else:
            # Rule 3: Special case for "qu"
            if "qu" in word:
                qu_index = word.index("qu") + 2
                result.append(word[qu_index:] + word[:qu_index] + "ay")
            else:
                # Rule 2: Move consonants to the end until a vowel is found
                for i, letter in enumerate(word):
                    if letter in vowels:
                        result.append(word[i:] + word[:i] + "ay")
                        break

    return " ".join(result)  # Join the modified words back into a sentence