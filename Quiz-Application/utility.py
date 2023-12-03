

class UtilityClass():
    
    @staticmethod
    def get_valid_input(input_text, max_value=1000):
        while True:
            category_index = input(input_text) 
            if ((max_value != 1000 and category_index == '0') or 
            (not category_index.isdigit() or int(category_index) >= max_value)):
                print("Please enter a number corresponding a section.\n")
                continue

            print()
            return category_index