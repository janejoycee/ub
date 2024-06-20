#Set up the questions


class MIRC(): 

    def __init__(self): #self is the current object

        self.questions = {
            'social_capital': [
                "I actively support other people who are in recovery.",
                "My family makes my recovery more difficult.",
                "I have at least one friend who supports my recovery.",
                "My family supports my recovery.",
                "Some people in my life do not think I will make it in my recovery.",
                "I feel alone.",
                "I feel like I am part of a recovery community."
            ],
            'physical_capital': [
                "My housing situation is helpful for my recovery.",
                "I have difficulty getting transportation.",
                "My housing situation is unstable.",
                "I have enough money every week to buy the basic things I need.",
                "Not having enough money makes my recovery more difficult.",
                "I can afford the care I need for my health, mental health, and recovery.",
                "I have reliable access to a phone and the internet."
            ],
            'human_capital': [
                "I find it hard to have fun.",
                "I feel physically healthy most days.",
                "I am struggling with guilt or shame.",
                "I am experiencing a lot of stress.",
                "My education and training have prepared me to handle life's challenges.",
                "I have problems with my mental health.",
                "I feel my life has purpose and meaning."
            ],
            'cultural_capital': [
                "It is hard for me to trust others.",
                "I have opportunities to participate in fun activities that do not involve drugs and alcohol.",
                "I feel disconnected from my culture or not part of any culture.",
                "I feel like an outcast.",
                "There are helpful services and resources accessible to me.",
                "It is hard to let go of the part of my identity that was linked to my drinking or drug use.",
                "My neighborhood or town feels safe."
            ] 
        }

        #print(self.questions)

        self.responses = {1: 'Strongly Disagree', 2: 'Disagree', 3: 'Agree', 4: 'Strongly Agree'}

        self.user_responses = {capital: [] for capital in self.questions}

        pass

    def introduction(self):
        print("Instructions: This survey asks how strongly you agree or disagree with each statement based on your current situation or how you feel right now. Your answers help identify resources and challenges in recovery. There are no right or wrong answers.")
        print("We will move onto the first capital now.")

    def collect_responses (self):
        for capital , questions in self.questions.items():
            formal_name_of_cap = capital.replace("_", ' ').title()
            print("This is a gentle reminder, that 'Strongly Disagree' = 1, 'Disagree' = 2: 'Agree' = 3 and 'Strongly Agree' = 4.")
            print(F"The capital you are on is : {formal_name_of_cap}. ")
            for question in questions:
                print(question)
                answer = int(input("Enter your choice (1-4): "))
                for cap, scores in self.user_responses.items:
                    if cap == capital:
                        self.user_responses[capital].append(answer)
                    else:
                        pass
                
    def calculate_scores(self):
        self.capital_scores = {}
        for capital, answers in self.user_responses.items():
            formal_name_of_cap = capital.replace("_", ' ').title()
            self.capital_scores[capital] = sum(answers)
        return self.capital_scores
    
    def total_score(self):
        return sum(self.capital_scores.values())

    def display_results(self):
        print("Your Recovery Capital scores:")
        for dimension, score in self.capital_scores.items():
            formal_name_of_cap = dimension.replace("_", ' ').title()
            print(f"{formal_name_of_cap.capitalize()}: {score}")

        print(f"Total Recovery Capital Score: {self.total_score()}")

    pass

survey = MIRC()
survey.introduction()
survey.collect_responses()
survey.calculate_scores()
survey.display_results()


        




