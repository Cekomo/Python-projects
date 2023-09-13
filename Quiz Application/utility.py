

class UtilityClass():
    
    @staticmethod
    def get_valid_input(self, input_text):
        while True:
            category_index = input(input_text)
            if category_index.isdigit(): 
                print()
                return category_index
            print("Please enter a number corresponding a section.")
        print()