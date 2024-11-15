class CalculatorChatbot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! I'm {self.name}, your Calculator Chatbot.")
        print("I can perform basic calculations like addition, subtraction, multiplication, and division.")
        print("Type 'exit' to end the chat.")

    def calculate(self, user_input):
        try:
            # Parse and evaluate the input
            result = eval(user_input)
            return f"The result is: {result}"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except Exception:
            return "Invalid input. Please enter a valid mathematical expression."

    def chat(self):
        self.greet()
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print(f"{self.name}: Goodbye! Have a great day!")
                break
            print(f"{self.name}: {self.calculate(user_input)}")


# Main Program
if __name__ == "__main__":
    bot = CalculatorChatbot("CalcBot")
    bot.chat()
