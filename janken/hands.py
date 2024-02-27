rock_aa = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_aa = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_aa = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


class Hand:
    def __init__(self, name, art):
        self.name = name
        self.art = art


rock = Hand('グー', rock_aa)
paper = Hand('パー', paper_aa)
scissors = Hand('チョキ', scissors_aa)
