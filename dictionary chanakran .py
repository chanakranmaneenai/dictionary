class DictionaryEntry:
    def __init__(self, english_word, thai_translation,word_type):
        self.english_word = english_word
        self.thai_translation = thai_translation
        self.word_type = word_type


class Dictionary:
    def __init__(self):
        self.entries = []
        self.current_entry = None

    def add_entry(self, english_word, thai_translation, word_type):
        entry = DictionaryEntry(english_word, thai_translation, word_type)
        self.entries.append(entry)
        if len(self.entries) == 1:
            self.current_entry = entry

    def show_current_entry(self):
        if self.current_entry:
            entry = self.current_entry
            print(f"Word: {entry.english_word}, Translate: {entry.thai_translation},Type :{entry.word_type}")
        else:
            print("This word isn't in my dictionary")


    def show_entries(self):
        if self.entries:
            for entry in self.entries:
                print(f"Word์: {entry.english_word}, Translate: {entry.thai_translation},Type :{entry.word_type}")
        else:
            print("This word isn't in my dictionary")

    def show_next_entry(self):
        if self.current_entry and self.entries.index(self.current_entry) < len(self.entries) - 1:
            self.current_entry = self.entries[self.entries.index(self.current_entry) + 1]
            self.show_current_entry()
        else:
            print("No next word")

    def show_previous_entry(self):
        if self.current_entry and self.entries.index(self.current_entry) > 0:
            self.current_entry = self.entries[self.entries.index(self.current_entry) - 1]
            self.show_current_entry()
        else:
            print("This word isn't in my dictionary")

    def edit_current_entry(self, thai_translation, word_type):
        if self.current_entry:
            entry = self.current_entry
            entry.thai_translation = thai_translation
            entry.word_type = word_type
            print("Fix now")
        else:
            print("This word isn't in my dictionary")


    def search_entry(self, search_word):
        found_entries = [entry for entry in self.entries if search_word.lower() in entry.english_word.lower()]
        if found_entries:
            print(f"Search word '{search_word}':")
            for entry in found_entries:
                print(f"Word: {entry.english_word}, Translate: {entry.thai_translation}, Type :{entry.word_type}")
        else:
            print(f"This word isn't in my dictionary if you")

def main():
    dictionary = Dictionary()
    dictionary.add_entry("Accessories", "เครื่องประดับ","Noun")
    dictionary.add_entry("Behavior", "พฤติกรรม","Noun")
    dictionary.add_entry("Control", "ควบคุม","Verb")
    dictionary.add_entry("Determination", "ปณิธาน","Noun")
    dictionary.add_entry("Eliminate", "กำจัด","Verb")
    dictionary.add_entry("Fortune", "โชค","Noun")
    dictionary.add_entry("Greed", "ความโลภ","Noun")
    dictionary.add_entry("Humanity", "มนุษยชาติ","Noun")
    dictionary.add_entry("Imposter", "ตัวปลอม","Noun")
    dictionary.add_entry("Justice", "ความยุติธรรม","Noun")
    dictionary.add_entry("Knife", "มีด","Noun")
    dictionary.add_entry("Lamp", "โคมไฟ","Noun")
    dictionary.add_entry("Mysterious", "ลึกลับ","Adjective")
    dictionary.add_entry("Notorious", "ฉาวโฉ่","Verb")
    dictionary.add_entry("Operator", "ตัวดำเนินการ","Noun")
    dictionary.add_entry("Personal", "ส่วนตัว","Adjective")
    dictionary.add_entry("Questions", "คำถาม","Noun")
    dictionary.add_entry("Respect", "เคารพ","Verb")
    dictionary.add_entry("Sacrifice", "เสียสละ","Verb")
    dictionary.add_entry("Timely", "ถูกกาลเทศะ","Adjective")
    dictionary.show_entries()

    while True:
        print("My dictionary")
        print("1. Search","2. Present word","3. Next word","4. Previous word","5. Edit word","6. Show all","7.Quit")

        choice = input("Make your choice: ")

        if choice == '1':
            search_word = input("ค้นหาคำศัพท์ (ภาษาอังกฤษ): ")
            dictionary.search_entry(search_word)
        elif choice == '2':
            dictionary.show_current_entry()
        elif choice == '3':
            dictionary.show_next_entry()
        elif choice == '4':
            dictionary.show_previous_entry()
        elif choice == '5':
            english_word = input("Input word: ")
            thai_translation = input("Input translate: ")
            word_type = input("Input type")
            dictionary.add_entry(english_word, thai_translation, word_type)
            print("Finish")
        elif choice == '6':
            dictionary.show_entries()
        elif choice == '7':
            break
        else:
            print("Error please try again")

if __name__ == "__main__":
    main()
