import pickle
import random
import os


class Quiz:
    list = []
    quizst = []

    def __init__(self, soal, javab):
        self.soal = soal
        self.javab = javab

    def __str__(self):
        return f"{self.soal}"

    def pickl(self):
        pickled = pickle.dumps(self)
        file = open("quiz.pk", 'ab')
        file.write(pickled)
        file.close()
        file = open("quiz.pk", 'a')
        file.write('\n')
        file.close()

    def emtahan_dadan(self):
        nomreh = 0
        for _ in range(5):
            quizst = random.choice(Quiz.list)
            print(quizst)
            javab = input("lotfa javab ra vared konid: ")
            os.system("cls" if os.name == "nt" else "clear")
            natijeh = self.barsi_javab(javab)
            nomreh += natijeh

            print("your score is: ", nomreh)

    def barsi_javab(self, javab):
        if javab == self.javab:
            print("javab dorsteh +10")
            return 10
        else:
            print("javab qlateh -3")
            return -3

    @staticmethod
    def khanddan():
        file = open("quiz.pk", "rb")
        Quiz.unpickle_text(file.readlines())
        file.close()

    @staticmethod
    def unpickle_text(file):
        for x in file:
            unpickle = pickle.loads(x)
            Quiz.list.append(unpickle)


bj = Quiz("aya esm man nima s?", "true")
bj_1 = Quiz("aya family man hasani hast?", "True")
bj_2 = Quiz("man 20 salmeh?", "True")
bj_3 = Quiz("aya esm man ali s?", "False")
bj_4 = Quiz("aya family man mohamdi hast?", "False")
bj_5 = Quiz("man 10 salmeh??", "False")
bj_6 = Quiz("aya man zan hastam?", "false")
bj_7 = Quiz("aya man mard hastam?", "true")
bj.pickl()
bj_1.pickl()
bj_2.pickl()
bj_3.pickl()
bj_4.pickl()
bj_5.pickl()
bj_6.pickl()
bj_7.pickl()
Quiz.khanddan()

while True:
    entkhab = input(
        "lotfa entkhab konid\n1)start...\n2)new-Quiz...\n3)show-the-score...\n4)Exit...\nyour number: ")

    if entkhab == "1":
        for x in Quiz.list:
            print(x)


    elif entkhab == "2":
        new_quiz = input("lotfan soal jadid r vared konid: ")
        Quiz.list.append(new_quiz)


    elif entkhab == "3":
        bj.emtahan_dadan()

    else:
        print("Exit...")
        break
