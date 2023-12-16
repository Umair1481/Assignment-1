import sys
class preprocessor:
    def __init__(self, inp_1, out_1):
        self.inp_1 = inp_1
        self.out_1 = out_1
        self.spaces_eliminate = []
        self.comments_eliminate = []
        self.tabs_eliminate = []
        self.annotation_eliminate = []
    def eliminate_spaces(self):
        with open(self.inp_1, 'r') as file:
            data = file.readlines()
        # Remove blank lines
        for line in data:
            stripped_line = line.strip('\n')
            if stripped_line.strip():
                self.spaces_eliminate.append(stripped_line)
        #print(self.spaces_eliminate)
    def eliminate_comments(self):
        for comments in self.spaces_eliminate:
            if comments.strip().startswith("#") or comments.strip().startswith('"""'):
                self.comments_eliminate.append(" ")
            else:
                self.comments_eliminate.append(comments)
        if self.spaces_eliminate != self.comments_eliminate:
            self.spaces_eliminate = self.comments_eliminate
    def eliminate_tabs(self):
        for tabs in self.comments_eliminate:
            if tabs != " ":
                self.tabs_eliminate.append(tabs.strip())
        if self.spaces_eliminate != self.tabs_eliminate:
            self.spaces_eliminate = self.tabs_eliminate
    def eliminate_annotation(self):
        for annotation in self.tabs_eliminate:
            if not annotation.strip().startswith("import") or annotation.strip().startswith("from") or annotation.strip().startswith("@") or annotation.strip().startswith("*"): 
                self.annotation_eliminate.append(annotation)
        if self.spaces_eliminate != self.annotation_eliminate:
            self.spaces_eliminate = self.annotation_eliminate
    def output_write(self):
        with open(self.out_1, 'w') as out_1:
            out_1.write('\n'.join(self.spaces_eliminate))
    def display_file(self):
        for data in self.spaces_eliminate:
            print(data)
class processor:
    def __init__(self, out_1,out_2):
        self.out_1 = out_1
        self.out_2 = out_2
        self.linear_array = []
    def write_out2(self):
        with open(self.out_1, 'r') as file:
            data = file.readlines()
        # Remove blank lines
        for line in data:
            stripped_line = line.strip('\n')
            self.linear_array.append(stripped_line)
        new_string = " "
        buffer = "$"
        for i in self.linear_array:
            new_string += i
        new_string += buffer
        with open(self.out_2, 'w') as file:
            file.write(new_string.lstrip())
    def display_out2(self):
        with open(self.out_2, 'r') as file:
            data = file.readlines()
        print(data)
        for i in data:
            print(i)
class LexicalAnalyzer:
    def __init__(self, out_2):
        self.out_2 = out_2
        self.tokens = []
    def analyze(self):
        with open(self.out_2, 'r') as file:
            data = file.readlines()
            current_token = ""
            print(data)
            for char in data[0]:  # Accessing the first element of the list
                
                if char.isalpha():
                    current_token += char
                    
                else:
                    if current_token:
                        self.tokens.append(current_token)
                        current_token = ""

                    if char.isspace():
                        continue  # Skip whitespaces
                    else:
                        self.tokens.append(char)
    def display_tokens(self):
        for token in self.tokens:
            print(f"lexemes = {token}")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python_script.py inp_1.py out_1.py"  "out_2.py")
        sys.exit(1)
    else:
        inp_1 = sys.argv[1]
        out_1 = sys.argv[2]
        out_2 = sys.argv[3]
        x = preprocessor(inp_1, out_1)
        x.eliminate_spaces()
        x.eliminate_comments()
        x.eliminate_tabs()
        x.eliminate_annotation()
        x.output_write()
        #x.display_file()
        y = processor(out_1,out_2)
        y.write_out2()
        #y.display_out2()
        z = LexicalAnalyzer(out_2)
        z.analyze()
        z.display_tokens()
        
        
        
        