import os
from colorama import Fore, Style
from art import *
from termcolor import colored
import time

careers = {
    "Data mining": {
        "What is it?": """Data mining is digging into giant piles of data to uncover hidden patterns and other useful stuff that would be impossible for a human to find on their own. It uses special mathematical and computing techniques to search through all that data.


Companies collect massive amounts of information - numbers, stats, facts about customers and sales and expenses. Data mining lets you “shovel” all that data into computers so they can carefully sift through looking for valuable bits of insider insight. Those computers use programming scripts and modeling to surface cool patterns that are secretly lurking within all the noise and numbers.


For example, data mining might dig up facts like what age group buys the most shoes online, what zip codes order the most paperback romance novels, or which customers are most likely to cancel a subscription. Companies can take these data and use them to make smarter choices around their marketing, inventories, product offerings, you name it! (and show you better ads)
""",
        'What postsecondary education is required to work in this area related to computers:': {
            "What program must the individual have (post-secondary degree)?": 'To work as a data miner, you will need at least a bachelor’s degree in computer science, mathematics, statistics, or a related field. However, some companies may prefer candidates with a master’s degree or a PhD in these fields, especially for more advanced or research-oriented positions (pays better).',
            "What are the (high school) entrance requirements for this program?": 'The entrance requirements for a bachelor’s degree in computer science, mathematics, statistics, or a related field may vary depending on the institution, but generally, you will need to have a high school diploma or equivalent, and a strong background in mathematics, science, and English. You may also need to take standardized tests, such as the SAT or the ACT, and submit letters of recommendation, personal statements, and transcripts .',
            "Which institutions offer this program (post-secondary schools)?": """University of British Columbia: Master of Data Science 
University of Toronto: Master of Science in Applied Computing - Data Science 
University of Waterloo: Bachelor of Computer Science - Data Science 
McGill University: Graduate Certificate in Data Mining and Machine Learning 


etc.
""",
            "How long is the program?": """Data mining programs typically take four years to complete. However, some master's degree programs can be completed in as little as two years.
""",
            "What is the cost?": """The cost of the program may vary depending on the institution, the level of degree, the residency status, and the financial aid, but generally, the tuition fees for a bachelor’s degree range from about $7,000 to $15,000 per year, the tuition fees for a master’s degree range from about $8,000 to $20,000 per year, and the tuition fees for a PhD range from about $9,000 to $25,000 per year .
"""
        },
        "What work habits are important for success in this career related to computer studies?": """Good problem-solving skills: Data mining scientists need to think critically step by step in order to solve complex problems effectively.

Pay attention to detail: They must carefully review their work to avoid errors or serious consequences.

Stay on top of New technologies: They must learn new innovation and technology in this ever-changing field of computer science.

communication skills: Clear and concise explanations of technical concepts are necessary. Or else your boss won’t understand and replace you with somebody that’s more straightforward.

Good at both Independent and collaborative work: data mining scientists must work effectively both independently and as part of a team. 
""",
        'Salary': """The median annual salary for data miners is $97,000. However, salaries can vary depending on experience, location, and industry."""
    }, 

    "Machine learning": {
        "What is it?": """Machine learning means using computer algorithms that can learn and improve from data without being explicitly programmed. (like if statements) These algorithms find patterns in large datasets to make predictions and decisions on their own. As they process more data over time, the machine learning models are able to adapt and improve their performance ALL ON ITS OWN. The goal is for the algorithms to identify statistical relationships in data that would be impossible for a human to uncover. Machine learning tech is behind innovations like voice assistants, autonomous vehicles, fraud prevention, and medical insights. ALL without requiring hard-coded software instructions!""",
        'What postsecondary education is required to work in this area related to computers:': {
            "What program must the individual have (post-secondary degree)?": """To become a machine learning engineer, you will typically need a bachelor's degree in computer science, statistics, mathematics, or a related field. But some employers may also prefer a master's degree in machine learning or a related field.""",
            "What are the (high school) entrance requirements for this program?": """To be admitted to a machine learning program, you will typically need a strong academic record in high school, particularly in math and science. You may also need to take standardized tests, such as the SAT or ACT.

""",
            "Which institutions offer this program (post-secondary schools)?": """Many universities and colleges offer machine learning programs. Some of the most well-respected programs are offered at Stanford University, Massachusetts Institute of Technology, Carnegie Mellon University, and the University of California, Berkeley.
""",
            "How long is the program?": """Machine learning programs typically take four years to complete. However, some master's degree programs can be completed in as little as two years.
""",
            "What is the cost?": """The cost of a machine learning program can vary depending on the institution and the type of program. However, the average is between $10,000 and $50,000 total in tuition and fees.
"""
        },
        "What work habits are important for success in this career related to computer studies?": """- Think step by step, brainstorm solutions, create models, and really scrutinize your work
Constantly study and learn, as machine learning is advancing and improving nonstop
Communicate well to truly understand needs, break down complex concepts, and collaborate
Stay organized tracking all your datasets, models and experiments so you can retrace steps
Have patience and persistence, since ML requires continuously tweaking models until they work well
""",
        'Salary': 'The median annual salary for machine learning engineers is $116,000. '
    }, 

    "Data scientist": {
        "What is it?": "A data scientist is like a detective that uses numbers and stats instead of clues to figure stuff out. They take giant collections of facts, figures, and information and dig through it all to find cool patterns that can be used to predict things. Data scientists use their math skills, programming abilities, and statistical knowledge to organize the messy data and uncover hidden secrets and insights. Then they have to put together charts, graphs and presentations to explain what they discovered in a way that normal business people can understand so companies can make really good choices that hopefully makes the company more profits!",
        'What postsecondary education is required to work in this area related to computers:': {
            "What program must the individual have (post-secondary degree)?": 'To work as a data scientist, you usually need at least a bachelor’s degree in computer science, data science, or a related field. However, many employers prefer a master’s degree or even a doctorate in data science. You also need to have certifications or experience in specific tools and programming languages that are needed for data science.',
            "What are the (high school) entrance requirements for this program?": """Some of the common entrance requirements for data science programs are high school diplomas with good grades in mathematics, statistics, and computer science. Some programs may also require standardized test scores, letters of recommendation, or personal statements.
""",
            "Which institutions offer this program (post-secondary schools)?": """There are many institutions that offer data science programs, some examples are:

University of California, Berkeley: Master of Information and Data Science (MIDS) 
Harvard University: Master of Science in Data Science 
Stanford University: Master of Science in Statistics: Data Science Massachusetts Institute of Technology: MicroMasters Program in Statistics and Data Science 
Coursera: IBM Data Science Professional Certificate 
""",
            "How long is the program?": """The duration and cost of data science programs vary depending on the institution, the level of degree, etc.
On average, a bachelor’s degree takes about four years to complete, a master’s degree takes about two years, and a doctorate takes about four to six years. 
""",
            "What is the cost?": """The cost of tuition and fees can range from a few thousand dollars to tens of thousands of dollars per year.
"""
        },
        "What work habits are important for success in this career related to computer studies?": """Constantly reading and learning: Data science is a fast-changing field, so to avoid getting fired, data scientists need to keep up with the latest trends, technologies, and research.

Data preparing and database management: Data scientists need to be able to collect, clean, organize, and store data from various sources and formats, and make it ready for analysis.

Problem-solving and good iq: Data scientists need to be able to ask good questions, design AND implement solutions, and improve their results. They need to be able to solve problems systematically chunk by chunk.

Communication and collaboration: Data scientists need to be able to explain their findings and recommendations to different audiences, such as CEOs, managers, or their peers, and work with other data scientists and managers.
""",
        'Salary': """The average salary for a data scientist is $91,016 per year in Canada.
"""
    }
}


def clear_screen():
    # Check if the operating system is Windows
    
    #os.system('cls')

    os.system('clear')

def printing_main_menu():
  print(""" 
 /\_/\  
( o.o ) 
 > ^ <
""")
  
  
  print('WELCOME!')
  Art = text2art("MAIN     MENU")  # Generate ASCII art
  print(Fore.YELLOW + Art + Style.RESET_ALL)
  print("""Which money making career you want to know more? \n
    1. \033[1;35;40mData mining\033[0m 🚀
    2. \033[1;36;40mMachine Learning\033[0m 💻
    3. \033[1;33;40mData scientist\033[0m 🧪
    """)

def exit_program():
    clear_screen()
    print("Thank you for using this program. Goodbye!")
    time.sleep(1)
    clear_screen()
    exit()

def ask_user_input(type): 
    if type == 'int':
        while True:
            try:
                i = int(input(Style.DIM + Fore.WHITE + "Enter your selection: " + Style.RESET_ALL))
                return i
            except:
                print("Please enter a valid number")
                continue
    

def handle_user_selection(user_input):
    if user_input == 1:
        career = 'Data mining'
    elif user_input == 2:
        career = 'Machine learning'
    elif user_input == 3:
        career = 'Data scientist'
    else:
        print("Invalid selection. Please try again.")
        return True

    while True:
        clear_screen()
        print(Fore.GREEN + f"You have selected {career}. What would you like to know?\n" + Style.RESET_ALL)

        keys = list(careers[career].keys())
        for i, key in enumerate(keys, start=1):
            print(f"{i}. {key}")
        print()

        print(Style.BRIGHT + Fore.GREEN + "Back to main menu (5)")
        print(Style.BRIGHT + Fore.BLUE + "Go back (0)")
        print(Style.BRIGHT + Fore.RED + "Exit program (-1)")
        print(Style.RESET_ALL)
        print()

        user_input = ask_user_input('int')
        if user_input == -1:
            exit_program()
        elif user_input == len(keys) + 1: # main menu
            return False
        elif user_input == 0: # go back
            return True
        elif user_input > 0 and user_input <= len(keys):
            selected_key = keys[user_input - 1]
            if isinstance(careers[career][selected_key], dict):
                handle_inner_selection(careers[career][selected_key])
            else:
                clear_screen()
                print(Fore.GREEN + f"{selected_key}\n" + Style.RESET_ALL)
                print(careers[career][selected_key])
                print()
                input(Style.BRIGHT + Fore.MAGENTA + "Press enter to continue..."+ Style.RESET_ALL)
        else:
            print(Fore.RED+"Invalid selection. Please try again."+Style.RESET_ALL)
    return True

def handle_inner_selection(inner_dict):
    while True:
        clear_screen()
        keys = list(inner_dict.keys())
        for i, key in enumerate(keys, start=1):
            print(f"{i}. {key}")

        print()

        print(Style.BRIGHT + Fore.GREEN + "Back to main menu (5)"+ Style.RESET_ALL)
        print(Style.BRIGHT + Fore.BLUE + "Go back (0)"+ Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED + "Exit program (-1)" + Style.RESET_ALL)
        print(Style.RESET_ALL)
        print()

        user_input = ask_user_input('int')
        if user_input == 0: # go back
            return
        
        elif user_input == -1:
            exit_program()

        elif user_input > 0 and user_input <= len(keys):
            selected_key = keys[user_input - 1]
            clear_screen()

            #print
            print(Fore.GREEN + f"{selected_key}\n" + Style.RESET_ALL)
            print(inner_dict[selected_key])
            print()
            input(Style.BRIGHT + Fore.MAGENTA + "Press enter to continue..."+ Style.RESET_ALL)    
            print(Fore.RED+"Invalid selection. Please try again."+Style.RESET_ALL)

# Start the program
while True:
    clear_screen()
    printing_main_menu()
    user_input = ask_user_input('int')
    if user_input == -1:
        exit_program()
    else:
        if not handle_user_selection(user_input):
            continue
