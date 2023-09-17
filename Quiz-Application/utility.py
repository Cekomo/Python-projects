

class UtilityClass():
    
    @staticmethod
    def get_valid_input(input_text, max_value=1000):
        while True:
            category_index = input(input_text)
            if category_index.isdigit() and int(category_index) < max_value:
                print()
                return category_index
            print("Please enter a number corresponding a section.\n")