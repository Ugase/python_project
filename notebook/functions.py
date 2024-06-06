import json
import blessed

term = blessed.Terminal()
center = term.width // 2


def create_unit(subject:dict, name:str):
    subject[name] = {}


def create_lesson(subject:dict, unit_name:str, lesson_number:int, title:str, definition:str, example=""):
    subject[unit_name].setdefault(f"Lesson {lesson_number}", {})["Title"] = title
    subject[unit_name].setdefault(f"Lesson {lesson_number}", {})["Definition"] = definition
    if example:
        subject[unit_name].setdefault(f"Lesson {lesson_number}", {})["Example"] = example


def get_list_of_unit(subject:dict):
    return list(subject.keys())


def get_list_of_lesson(subject:dict, unit_name:str):
    return [f"{lesson} - {subject[unit_name][lesson]['Title']}" for lesson in subject[unit_name]]


def get_lesson_title(subject:dict, unit_name:str, lesson_number:int):
    lesson_number -= 1
    return get_list_of_lesson(subject, unit_name)[lesson_number]


def get_lesson(subject:dict, unit_name:str, lesson_number:int):
    lesson = subject[unit_name][f"Lesson {lesson_number}"]
    title_padding = center - len(lesson["Title"])
    try:
        examples = lesson["Example"]
        expad = center - (len("Examples"))
        print(f"{title_padding * ' '}{lesson['Title']}\n{title_padding * ' '}{'-' * len(lesson['Title'])}\n\n{lesson['Definition']}\n\n\n{" " * expad}Examples:\n{" " * expad}{"-" * len("Examples")}\n\n{examples}")
    except:
        print(f"{title_padding * ' '}{lesson['Title']}\n{title_padding * ' '}{'-' * len(lesson['Title'])}\n\n{lesson['Definition']}\n\n")


def save(subject:dict, file:str):
    with open(file, "w") as f:
        json.dump(subject, f)

def load(file:str, cluster:bool):
    if cluster:
        with open(file, "r") as f:
            full_file = f.read()
            list_of_file_names = full_file.split()
            for file_name in list_of_file_names:
                file_name.replace(" ", "")
                if "-Math" in file_name:
                    file_name.replace("-Math", "")
                    math = file_name
                elif "-English" in file_name:
                    file_name.replace("-English", "")
                    english = file_name
                elif "-Science" in file_name:
                    file_name.replace("-Science", "")
                    science = file_name
                elif "-Computer" in file_name:
                    file_name.replace("-Computer", "")
                    computer = file_name
                elif "-Social" in file_name:
                    file_name.replace("-Social", "")
                    social = file_name
                elif "-Religion" in file_name:
                    file_name.replace("-Religion", "")
                    religion = file_name
            with open(math, "r") as m:
                math = json.load(m)
            with open(english, "r") as e:
                english = json.load(e)
            with open(science, "r") as s:
                science = json.load(s)
            with open(computer, "r") as c:
                computer = json.load(c)
            with open(social, "r") as ss:
                social = json.load(ss)
            with open(religion, "r") as r:
                religion = json.load(r)
        return [math, english, science, computer, social, religion]
    with open(file, "r") as sub:
        return json.load(sub)