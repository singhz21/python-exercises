# This file runs a program that quizzes the user

# Define the program that will be the quiz


def quiz():

    # Inform the user about the program
    print('Hello there! I am a tiny little, 10-question, general science quiz that intends to test your wits.')
    input('Press ENTER to continue')
    print(' ')
    print('I will ask you one question at a time and give you four answers to pick from, out of which, only one will be correct.')
    input('Press ENTER to continue')
    print(' ')
    print('To provide your answer, just type the number (1, 2, 3 or 4) that corresponds with your answer.')
    input('Press ENTER to continue')
    print(' ')
    print('At the end of the 10 questions, you shall have your score.')
    input('Press ENTER to continue')
    print(' ')

    # Initialise variables and lists/arrays
    user_answers = []
    correct_answers = [4, 2, 2, 1, 4, 3, 4, 2, 3, 1]

    # Start the quizzing whilst checking for any errors
    try:
        # Question 1
        print('Question 1: An electric bulb filament is made of?')
        print('1. Copper')
        print('2. Aluminium')
        print('3. Lead')
        print('4. Tungsten')  # Correct answer
        print(' ')
        user_answers.append(
            int(input('Please type your answer and hit ENTER >>> ')))
        print(' ')

        # Question 2
        print('Question 2: Which of the following is a non-metal that remains liquid at room temperature?')
        print('1. Phosphorus')
        print('2. Bromine')  # Correct answer
        print('3. Chlorine')
        print('4. Helium')
        print(' ')
        user_answers.append(
            int(input('Please type your answer and hit ENTER >>> ')))
        print(' ')

        # Question 3
        print('Question 3: Chlorophyll is a naturally occuring chelate compound in which the central metal is?')
        print('1. Copper')
        print('2. Magnesium')  # Correct answer
        print('3. Iron')
        print('4. Calcium')
        print(' ')
        user_answers.append(
            int(input('Please type your answer and hit ENTER >>> ')))
        print(' ')

        # Question 4
        print('Question 4: Which of the following is used in pencils?')
        print('1. Graphite')  # Correct answer
        print('2. Silicon')
        print('3. Charcoal')
        print('4. Phosphorus')
        print(' ')
        user_answers.append(
            int(input('Please type your answer and hit ENTER >>> ')))
        print(' ')

        # Question 5
        print('Question 5: Which of the following gas is not know as a "green house gas"?')
        print('1. Methane')
        print('2. Nitrous oxide')
        print('3. Carbon dioxide')
        print('4. Hydrogen')  # Correct answer
        print(' ')
        user_answers.append(
            int(input('Please type your answer and hit ENTER >>> ')))
        print(' ')

        # Question 6
        print('Question 6: The hardest substance available on Earth is?')
        print('1. Gold')
        print('2. Iron')
        print('3. Diamond')  # Correct answer
        print('4. Platinum')
        print(' ')
        user_answers.append(
            int(input('Please type your answer and hit ENTER >>> ')))
        print(' ')

        # Question 7
        print('Question 7: The gases used in different types of welding would include?')
        print('1. Oxygen and Hydrogen')
        print('2. Oxygen, Hydrogen, Acetylene and Nitrogen')
        print('3. Oxygen, Acetylene and Argon')
        print('4. Oxygen and Acetylene')  # Correct answer
        print(' ')
        user_answers.append(
            int(input('Please type your answer and hit ENTER >>> ')))
        print(' ')

        # Question 8
        print('Question 8: The property of a substance to absorb moisture from the air on exposure is called?')
        print('1. Osmosis')
        print('2. Deliquescence')  # Correct answer
        print('3. Efflorescence')
        print('4. Desiccation')
        print(' ')
        user_answers.append(
            int(input('Please type your answer and hit ENTER >>> ')))
        print(' ')

        # Question 9
        print('Question 9: Galvanised iron sheets have a coating of?')
        print('1. Lead')
        print('2. Chromium')
        print('3. Zinc')  # Correct answer
        print('4. Tin')
        print(' ')
        user_answers.append(
            int(input('Please type your answer and hit ENTER >>> ')))
        print(' ')

        # Question 10
        print('Question 10: The element common to all acids is?')
        print('1. Hydrogen')  # Correct answer
        print('2. Carbon')
        print('3. Sulphur')
        print('4. Oxygen')
        print(' ')
        user_answers.append(
            int(input('Please type your answer and hit ENTER >>> ')))
        print(' ')

        # Print result
        print(user_answers)
        print(correct_answers)
        input('Press Enter to exit ')

    # Run this bit of code if an error is encountered
    except ValueError:
        print('Please enter a numeric value between 1 and 4!')
        input('Press Enter to exit ')


# Call the program to be executed when the file is run
quiz()
