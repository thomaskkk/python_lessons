class MailMerger():
    def __init__(self) -> None:
        pass
        
    def read_template(self, template_file):
        with open(template_file) as data:
            self.template = data.read()

    def read_names(self, names_file):
        with open(names_file) as data:
            self.names = data.readlines()
            for name in self.names:
                self.names[self.names.index(name)] = name.strip()

    def generate_letters(self, letter_location):
        for name in self.names:
            letter = self.template.replace("[name]", name)
            with open(f"{letter_location}letter_for_{name}.txt", mode="w") as completed_letter:
                completed_letter.write(letter)
        