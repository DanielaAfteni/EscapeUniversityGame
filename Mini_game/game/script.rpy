# # The script of the game goes in this file.

# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

# define e = Character("Eileen")


# # The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     return



define system = Character("System")

define presenter = Character("Presenter")

define ciorba = Character("Ciorbă")

define bostan = Character("Bostan")

define mysterious_person = Character("Mysterious person")

define a_student = Character("Student")

define bad_student = Character("Bad student")

define teacher = Character("Teacher")

define smart_student = Character("Smart student")

define gui.text_outlines = [(4, "0124", 0, 0), (3, "0124", 0, 0), (1, "0124", 0, 0), (1, "0124", 0, 0)]


init:
    image bg utmblocresize = "utmblocresize.jpg"

    image bg student_apartment_resize = "student_apartment_resize.jpg"

    image bg dawn_resize = "dawn_resize.jpg"

    image bg utm_at_night_resize = "utm_at_night_resize.jpg"

    image bg event_resize = "event_resize.jpg"

    image bg ciorba_speech = "ciorba_speech_resize.jpg"

    image bg applause_resize = "applause_resize.jpg"

    image bg bostan 2 = "2_resize.jpg"

    image bg food_resize = "food_resize.jpg"

    image bg black_resize = "black_resize.jpg"

    image bg mysterious_person_resize = "mysterious_person_resize.jpg"

    image bg dark_3_resize = "3_resize.jpg"

    image bg call_police_4_resize = "4_resize.jpg"

    image bg formula = "formula_resize.png"

    image bg start_timer_resize = "start_timer_resize.jpg"

    image bg calculator_use_resize = "calculator_use_resize.jpg"

    image bg calculate_by_myself = "calculate_by_myself.png"

    image bg calculated_formula_resize = "calculated_formula_resize.png"

    image bg dark_halls_resize = "dark_halls_resize.jpg"

    image bg computer_in_dark_resize = "computer_in_dark_resize.jpg"
    
    image bg computer_opened_resize = "computer_opened_resize.jpg"

    image bg underground_resize = "underground_resize.jpg"

    image bg catches_you_cheating_18_resize = "catches_you_cheating_18_resize.jpg"
    
    image bg i_did_not_cheat_resize = "i_did_not_cheat_resize.jpg"

    image bg so_sorry_resize = "so_sorry_resize.jpg"
    
    image bg panel_resize = "panel_resize.jpg"
    
    image bg working_on_panel_rezise = "working_on_panel_rezise.jpg"
    
    image bg university_hall_light_resize = "university_hall_light_resize.jpg"

    image bg a_lot_of_cables_resize = "a_lot_of_cables_resize.png"
    
    image bg problem_science_resize = "problem_science_resize.png"
    
    image bg another_hall_resize = "another_hall_resize.jpg"
    
    image bg team_resize = "team_resize.jpg"

    image bg 29_resize = "29_resize.png"

    image bg 30_resize = "30_resize.jpg"

    image bg 31_resize = "31_resize.jpg"

    image bg 32_resize = "32_resize.jpg"

    image bg 33_resize = "33_resize.png"

    image bg 34_resize = "34_resize.jpg"

    image bg discuss_with_others_resize = "discuss_with_others_resize.jpg"
    
    image bg solve_problem_by_myself_resize = "solve_problem_by_myself_resize.jpg"
    
    image bg problem_solution_resize = "problem_solution_resize.png"
    
    image bg 26_resize = "26_resize.jpg"

    image bg 27_resize = "27_resize.jpg"

    image bg 28_resize = "28_resize.jpg"
    
    image bg keys_resize = "keys_resize.png"
    
    image letter 1 = "1.png"

    image presenter default = "presenter_png.png"

    image bostan default = "bostan_default.png"

    image any_student = "any_student.png"

    image bad_student default = "bad_student_resize.png"

    image crowd default = "crowd_resize.png"

    image smart_student_better_resize = "smart_student_1.png"
    
    image ciorba_25 = "25_r.png"

    # Variables:
    $ courage = 0
    $ luck = 0
    $ social_state = 3  # min = 0
    $ time = 0          # max = 15
    $ lives = 1


label splashscreen:
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] = .5
            _preferences.volumes['sfx'] = .5
            _preferences.fullscreen = True
    return

label start:
    $ hf_init("bg room", 5,
        ("present", 1013, 705, _("Present")),
        ("pencil", 211, 360, _("Pencil")),
        ("glue", 800, 515, _("Glue")),
        ("clock", 1550, 161, _("Clock")),
        ("money", 250, 50, _("Money present")),
        mouse=True,
        inventory=False,
        hint=True,
        hover=brightness(.05),
        w=200,
        h=200
    )

    $ hf_bg()
    with dissolve

    centered "{size=+24}Escape University Game\nLet's start!"

    centered "{size=+24}You have a cleanning day"
    centered "{size=+24}Instruction\nYou need to find 5 listed objects in 5 seconds\nClick to start"

    $ hf_start()

    $ renpy.pause(1, hard=True)

    if hf_return == 0:
        centered "{size=+24}SUPER!\nYou found all the objects!"
    else:
        centered "{size=+24}GAME OVER\nYou did not found: [hf_return] objects"

    menu:
        "Try again":
            jump start

        "Continue":
            jump start_of_the_game

        "End":
            pass

    $ hf_hide()
    with dissolve
    return



label start_of_the_game:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg utm_bloc.jpg
    show bg utmblocresize

    "I got a notification: It is the 55th anniversary of TUM!"

    show bg student_apartment_resize

    "Finally I finished the session, I am free and I will have free time to rest and relax!"

    "This was a complicated semester and I really worked hard."

    "I got an invitation!"

    show letter 1

    "I am invited to celebrate the 55th anniversary of Technical University of Moldova"

    menu:
        "What to do?"

        "Accept":
            system "Thanks for joining! The details to the private event will be sent shortly"
            jump start_party
            
        "Refuse":

            jump think_about_invitation
    
    return

label start_party:

    hide letter 1

    "The celebration will start late in the evening, so by the time I get ready."

    show bg dawn_resize

    "It is already the time to go"

    show bg utm_at_night_resize

    "I see that many people come to this even!" 
    
    "It means that I still did not come in vain, something grandiose is being prepared." 
    
    "In any case, at least I will eat well :)"

    show bg event_resize

    show presenter default

    presenter "Welcome!" 
    presenter "Ladies and gentlemen"
    presenter "Today, we gather here to celebrate the 55th anniversary of the Technical University of Moldova." 
    presenter "It is a special occasion for all of us, as we reflect on the journey that brought us here and the achievements we have made along the way."
    presenter "The event will start with mr. Ciorbă's and mr. Bostan's speeches."
    presenter "Please mr. Ciorbă, the dean of the Technical University of Moldova!"

    show bg ciorba_speech
    hide presenter default

    ciorba "Hello!"
    ciorba "Ladies and gentlemen, esteemed faculty, honored guests, and cherished students"
    ciorba "Welcome again to the 55th anniversary celebration of the Technical University of Moldova." 
    ciorba "It is with immense pride and gratitude that I stand before you today to commemorate this significant milestone in our institution's journey."
    ciorba "Over the past 55 years, our university has stood as a beacon of knowledge, innovation, and excellence in education."
    ciorba "From our humble beginnings to our current stature as a leading technical institution, we have remained steadfast in our commitment to fostering academic excellence and nurturing the brightest minds of tomorrow."
    ciorba "As we reflect on our past achievements, let us also look towards the future with optimism and determination. The challenges we face may be great, but so too are the opportunities that lie ahead."
    ciorba "In an ever-changing world, it is imperative that we continue to adapt, evolve, and innovate in order to stay at the forefront of technological advancements and societal progress."
    ciorba "I hope that even in future we will succeed even more!"
    ciorba "Happy anniversary to all of you!"

    show bg applause_resize

    show presenter default

    presenter "Thank you mr. Ciorbă for you speech."
    presenter "Now, please dear students, mr. Bostan, the rector of Technical University of Moldova!"

    hide presenter default

    show bg bostan 2

    bostan "Welcome to all!"
    bostan "I cannot express my gratitude toward UTM and all of you!"
    bostan "We should not forget that at the heart of our university are our students, whose passion, intellect, and creativity drive us forward each day."
    bostan "You are the lifeblood of our institution, and it is through your hard work and dedication that we continue to thrive."
    bostan "As you embark on your academic journey with us, know that you are not only shaping your own futures but also contributing to the greater good of society."
    bostan "In closing, I would like to express my heartfelt gratitude to all those who have contributed to the success of the Technical University of Moldova over the past 55 years." 
    bostan "Whether you are a student, faculty member, staff member, alumni, or supporter of our institution, your dedication and support have been instrumental in shaping our collective success."
    bostan "Here's to the next 55 years of excellence, innovation, and impact. Happy anniversary, Technical University of Moldova!"

    show bg event_resize

    show presenter default

    presenter "Thank you mr. Bostan for you speech."
    presenter "Now, ladies and gentlemen, we are inviting you at our banquet!"
    
    hide presenter default

    "Nice"

    show bg food_resize

    menu:
        "What to do?"

        "I am hungry and I am coming to you, food!":
            show bg food_resize
            "I can stay even more at this event. It is not bad at all."
            "Morever, mr. Ciorbă and mr. Bostan finished their speeches and now they left the event to let the students have fun."
            jump light_turned_off
            
        "NO, I am not hungry and I am leaving.":
            show bg utm_at_night_resize
            "So, I am going home."

            # END 

    return

label light_turned_off:
    
    "This food is really great!"
    
    show bg black_resize

    "What did happen?"
    "It's dark!"
    "All the lights are turned off!" 
    show bg dark_3_resize
    "Doors are locked!!!"
    "What I hear?"
    "Someone givies escape instructions through the speakers of the room?!"
    show bg mysterious_person_resize
    
    menu:
        "What to do?"

        "Wait until someone asks about the purpose of the action":
            show bg dark_3_resize
            show any_student
            a_student "Why is it all for?"
            $ luck += 1
            show bg mysterious_person_resize
            hide any_student
            mysterious_person "Right now I wanted to tell you "
            jump pre_start_game
            
        "Ask first what this is for":
            "Why is it all for?"
            $ courage += 1
            mysterious_person "Right now I wanted to tell you "
            jump pre_start_game

        "I'm calling the police!":
            show bg call_police_4_resize
            mysterious_person "No phones allowed!"
            mysterious_person "No cheating allowed!"
            show bg mysterious_person_resize
            mysterious_person "Consider this your last warning, students!"
            jump pre_start_game

    
    return

label pre_start_game:
    show bg mysterious_person_resize
    mysterious_person "Now, welcome to our special event."
    mysterious_person "This is a chance for each of you to prove your problem-solving abilities!"
    mysterious_person "After all, isn't this the foundation of our beloved university?"
    mysterious_person "Follow the instructions, and good luck!"
    mysterious_person "See you at the end!"
    mysterious_person "Of course, if you'll reach it on time ..."

    menu:
        "What to do?"

        "Listen to the enumerated instructions":
            jump start_game
            
        "Think a little bit":
            $ social_state += 1
            "Mr. Bostan???"
            "Now everybody understands that it is indeed mr. Bostan"
            mysterious_person "Prove it!"
            menu:
                "What to do?"

                "Say a reason":
                    $ courage 
                    "Only he uses a phrase 'if you'll reach it'!"
                    mysterious_person "Then you have to be even more motivated to get out of the block first!"
                    jump start_game
                    
                "I am afraid of what he might say back to me":
                    $ luck += 1
                    mysterious_person "I'll give you a hint."
                    show bostan default
                    bostan "That's me."
                    hide bostan default
                    jump start_game
    return

label start_game:
    mysterious_person "Instruction 1"
    
    show bg formula
   
    mysterious_person "Solve the given formula to enter the computer's passwords (where is the Instruction 2)"
    mysterious_person "Start of the time!!!"

    show bg start_timer_resize

    menu:
        "What to do?"

        "Calculate it by yourself":
            $ social_state += 1
            $ time += 2
            show bg calculate_by_myself
            "It will take some time but still I know how to calculate this."
            show bg calculate_by_myself
            "I learned that at the mr. Bostan's course."
            show bg calculated_formula_resize
            "It was complicated, but I did it."

            jump result_taken
            
        "Use calculator":
            $ time += 1
            show bg calculator_use_resize
            "I will try to hide."
            python:
                import random
                random_nr = random.randint(1, 10)
            if random_nr >= 6:
                $ time += 1
                show bg calculated_formula_resize
                "I got the result very fast!"
                jump result_taken
            else:
                system "Hey you, you got caught cheating!"
                system "You're eliminated!"
            
    return

 
label result_taken:
    "Somebody from students noticed that I have the result."

    show bad_student default
    "He wants to take my result!"
    bad_student "Give that to me!"
    $ time += 1

    menu:
        "What to do?"

        "Say no concretely":
            bad_student "You will regret it!"
            hide bad_student default
            $ courage += 1
            jump computer_first
            
        "He will get the result anyway, if not from me, then from someone else":
            bad_student "Ha! Good job!"
            hide bad_student default
            $ luck += 1
            jump computer_late
            

    return

label computer_first:
    show bg dark_halls_resize

    $ time += 1

    "Now, I need to go to that computer and enter the password that I calculated."
    "As I understand, in that computer should be the next instruction."
    
    show bg computer_in_dark_resize
    
    "WOW! I am the first!"
    
    $ time += 1

    "Now, I need to unlock the computer"
    
    centered "{size=+24}Do you remember the password?"
    centered "{size=+24}Instruction\nYou need to repreat the pattern.\nSelect the difficulty level\nClick to start"

    jump memory_game

    
    return




label after_the_game_be_first:
    show bg computer_opened_resize

    "I need to open the file with the next instruction."

    "Hmm..., it contains the location of the station, light box."

    system "Instruction 2"

    system "The light in the building must be turned on!"
    
    "time [time]"

    show bg dark_halls_resize

    "I need to go to that location, but it is in underground?"

    show bg underground_resize

    "Again! Nobody!"
    "It seems I will win today, but I don't know what is the problem."

    menu:
        "What to do?"

        "I will wait until somebody solves the problem":
            "It will take some time, but I really don't know how to solv this problem."
            "A student came!"
            jump another_student_solved_the_problem

        "I will try to come up with a solution":
            $ courage += 2
            jump try_to_come_up_with_a_solution


label another_student_solved_the_problem:
    
    hide crowd default
    show smart_student_better_resize
    smart_student "I found the problem"
    $ luck += 1
    $ time += 4
    "A smart student found the problem instead of me and solved it"
    hide smart_student_better_resize
    show bg working_on_panel_rezise
    "He turns on the light."
    jump the_light_is_on
    
    return

label computer_late:
    show bg dark_halls_resize

    $ time += 1

    "Now, I need to go to that computer and enter the password that I calculated."
    "As I understand, in that computer should be the next instruction."



    show bg computer_opened_resize

    show crowd default

    "Oops! I am not the first."
    "I should wait my turn."

    $ time += 2

    hide crowd default

    "Now, I need to unlock the computer"
    
    centered "{size=+24}Do you remember the password?"
    centered "{size=+24}Instruction\nYou need to repreat the pattern.\nSelect the difficulty level\nClick to start"

    jump memory_game_2

    return

label after_the_game_be_first_2:

    "It took some time, but now is my turn to open te file."
    "I need to open it in order to find the next instruction."
    
    "Hmm..., it contains the location of the station, light box."
    system "Second instruction: the light in the building must be turned on!"
    
    "time [time]"

    show bg dark_halls_resize

    "I need to go to that location, but it is in underground?"

    show bg underground_resize
    
    show crowd default

    "In this room are already some students."

    hide crowd default
    
    show bad_student default
    
    "Including that student who offended me!"

    hide bad_student default

    show crowd default

    "Nobody knows from where the problem comes?"

    menu:
        "What to do?"

        "I will wait until somebody has an idea, and stole the opportunity, so be the first (as that student did to me)":
            if luck < 6:
                hide crowd default
                show bg catches_you_cheating_18_resize
                system "Announcement: You have been noticed while cheating, you broke the rule"
                $ social_state = 0
                $ time += 1
                jump acknowledge_meniu
            
        "I will wait until somebody solves the problem":
            jump another_student_solved_the_problem

        "I will try to come up with a solution":
            $ courage += 1
            jump try_to_come_up_with_a_solution

    return


label acknowledge_meniu:

    menu:
        "What to do?"

        "Acknowledge the mistake and ask for forgiveness":
            show bg so_sorry_resize 
            $ lives -= 1
            if luck >= courage:
                teacher "Ok, one more chance"
                $ lives += 1
                jump try_to_come_up_with_a_solution
            else:
                teacher "No, a mistake is a mistake, you don't follow the rules."
                $ lives = 0
                system "You are not allowed to continue the game."

        "Don't acknowledge your mistake":
            show bg i_did_not_cheat_resize
            teacher "You insulted the creator and his game!"
            $ time += 1
            $ lives = 0
            system "You are not allowed to continue the game."

    return

label try_to_come_up_with_a_solution:

    show bg underground_resize
    hide crowd default
    menu:
        "What to do?"

        "Check by yourself":
            $ courage += 1
            jump the


        "Ask somebody to verify":
            show smart_student_better_resize
            "Sorry could you verify the ..."
            $ luck += 1
            jump the

    return

label the:
    show bg panel_resize

    menu:
        "What to verify?"

        "Buttons on the panel":
            $ time += 1
            "Oops! Not right!"
            jump the

        "Cables in panel box":
            $ time += 1
            "One cut cable has been hidden in the others!"
            jump another_cable_must_be_found

        "Cables coming out of the panel box":
            $ time += 1
            "Oops! Not right!"
            jump the

    return

label another_cable_must_be_found:
    "Another cable of the same type must be found, with the same port, thickness, length and maybe color."
    $ time += 1
    hide smart_student_better_resize
    show bg a_lot_of_cables_resize 
    "A substitute must be here"

    "I found cables!"

    

    show bg working_on_panel_rezise

    "Now, it is needed to replace the corresponding cable."
    $ social_state += 1
    $ time += 1
    "Uh! Let's turn on the light"
    jump the_light_is_on
    
    return



label the_light_is_on:

    show bg university_hall_light_resize

    mysterious_person "The light is on."

    show bg mysterious_person_resize
    mysterious_person "Congratulations!"
    mysterious_person "3 instruction!"
    mysterious_person "You must open the door, you have [(15 - time)*4] minutes."
    mysterious_person "You need to find the key."
    
    show bg problem_science_resize

    mysterious_person "You will find a note on the main door."
    mysterious_person "The answer to following problem is the auditorium where the key to the door is located."

    menu:
        "What to do?"

        "Search auditoriums by yourself":
            show bg another_hall_resize
            $ luck += 1
            jump search_auditoriums_meniu

        "Gather a team and search every auditorium":
            show bg team_resize
            $ social_state += 1
            jump gather_a_team

        "Solve the problem":
            $ time += 1
            show bg solve_problem_by_myself_resize
            jump solve_science_problem

    return


label solve_science_problem:
    menu:
        "What to do?"

        "Discuss the problem with others":
            show bg discuss_with_others_resize
            $ time += 1
            "It helped me find the solution"
            show bg problem_solution_resize
            "But I am not the first to find the solution."
            jump run_or_pick

        "Solve by yourself":
            show bg solve_problem_by_myself_resize
            "It will be a little hard."
            "But I am able to do it!"
            show bg problem_solution_resize
            "I succesfully solved the problem"
            show bg keys_resize
            "And found the key"

            if social_state >= 5 and courage <= 3:
                show bg 30_resize
                system "You are named as the best student!"
                system "You receive a prize!" 
                jump score_final
            elif social_state >= 5 and courage > 3:
                show bg 29_resize
                system "You are named as the best student!" 
                system "And the bravest!"
                system "You receive a prize!"
                jump score_final
            else:
                show bg 31_resize
                system "You are just awarded."
                jump score_final

    return

label run_or_pick:
    menu:
        "What to do?"

        "Run towards the auditorium":
            show bg another_hall_resize
            $ time += 1
            "While running I met Mr Dean who was greeting me and asking me to bring him a glass of water."
            show ciorba_25
            ciorba "Hi, dear student!"
            ciorba "Do you have a minute?"
            ciorba "I also got stuck here."
            ciorba "And I need some water."
            ciorba "Could you bring me a glass of water."
            
            menu:
                "What to do?"

                "Accept":
                    $ time += 1
                    $ courage += 1
                    $ luck += 1
                    $ social_state += 1
                    $ lives += 1
                    "Uhh! It took some time, but I think I made the right decision."
                    hide ciorba_25
                    "I need to find the room!"
                    show keys_resize
                    "I entered the room and found the key"
                    jump enter_room

                "Decline":
                    $ lives -= 1
                    "Sorry, but I don't have enough time."
                    hide ciorba_25
                    "I need to find the room!"
                    show keys_resize
                    "I entered the room and found the key"
                    jump enter_room

        "Pick the elevator":

            python:
                import random
                random_nr1 = random.randint(1, 10)
            if random_nr1 >= 7:
                show bg 27_resize
                "The elevator was somehow empty and you managed to be first."
                show keys_resize
                "I found the keys!"
                "You won and was awarded"
                if social_state >= 5 and courage <= 2:
                    show bg 30_resize
                    system "You are named as the best student!"
                    system "You receive a prize!" 
                    jump score_final
                elif social_state >= 5 and courage > 2:
                    show bg 29_resize
                    system "You are named as the best student!" 
                    system "And the bravest!"
                    system "You receive a prize!"
                    jump score_final
                else:
                    show bg 31_resize
                    system "You are just awarded."
                    jump score_final
            else:
                show bg 26_resize
                system "Unfortunately the elevators are too crowded and you fail to use them."
                show bg 31_resize
                system "You are just awarded."
                jump score_final

    return


label enter_room:
    if time == 15:
        "Time is out, you didn't won"
        show bg 31_resize
        system "You are just awarded."
        jump score_final
    else:
        show bg 28_resize
        "While returning the key fell"
        $ time += 1
        "A student wanted to steal the key from me."
        "Mr Ciorba interferes?"
        show ciorba_25
        ciorba "Sorry, what happens here"
        "This student wants to convince you its me who stole the key from him!"
        if lives > 1:
            ciorba "Actually I saw how the key fell from your pocket as I was drinking my water."
            "Thank you!!!"
            hide ciorba_25
            "I succesfuly opened the main door!"
            if social_state >= 7 and courage <= 4:
                show bg 30_resize
                system "You are named as the best student!"
                system "You receive a prize!" 
                jump score_final
            elif social_state >= 7 and courage > 4:
                show bg 29_resize
                system "You are named as the best student!" 
                system "And the bravest!"
                system "You receive a prize!"
                jump score_final
            else:
                show bg 31_resize
                system "You are just awarded."
                jump score_final
        else:
            ciorba "I believe this student, he sounds too convincing and you are disqualified"

    return

label gather_a_team:
    if luck > courage:
        $ time += 1
        show bg another_hall_resize
        "I divided to devide the auditoriums between the team members and everyone needs to searche to its corresponding rooms."
        show bg keys_resize
        "One of my team members found the key!"
        if social_state >= 6 and courage > 2:
            show bg 32_resize
            system "Your team was awarded!" 
            system "You are declared the best team!"
            system "And the bravest!"
            jump score_final
        elif social_state >= 6 and courage <= 2:
            show bg 33_resize
            system "Your team was awarded!" 
            system "You are declared the best team!"
            jump score_final
        else:
            show bg 34_resize
            system "You and your team are just awarded."
            jump score_final
    else:
        show bg 31_resize
        "Another team found the key."
        system "You are one of the students who tried to win."
        jump score_final
    return

label search_auditoriums_meniu:
    "I will try to search auditoriums alone"
    if luck >= courage:
        show bg keys_resize
        "I find the key in the first auditorium I chose and won the contest!"
        if social_state >= 5:
            show bg 30_resize
            system "You are named as the best student" 
            system "You receive a prize!"
            jump score_final
        else:
            show bg 31_resize
            system "You are just awarded."
            jump score_final
    else:
        "Someone else solved the problem while I was searching for the key."
        show bg 30_resize
        system "You are one of the students who tried to win."
        jump score_final
        
    return



label score_final:
    centered "{size=+24}Your score:\nCourage [courage]\nLuck [luck]\nSocial state [social_state]\nSpent time [time]\nLives [lives]"
    return

label think_about_invitation:

    "Think twice, mr. Pumpkin has prepared something special."

    menu:
        "What to do?"

        "HELL YES! Sounds convincing!":
            system "Thanks for joining! The details to the private event will be sent shortly"
            jump start_party
            
        "NO, even this doesn't intrigue me.":
            hide letter 1
            "So, I am staying home."
            # END 
    
    return

transform half_size:
    zoom 0.75
    
screen game_over:
    image "laptop_keyboard_resize.jpg"
    frame:
        background "#06646980"
        xfill True
        yfill True
        frame:
            background None
            xysize (774, 470)
            align (0.5, 0.5)
            text "You got the wrong button...\nTry again?" size 45 color "#45f4f1" outlines[(absolute(2), "#00959d", 0, 0)] align(0.5, 0.10) text_align 0.5
            imagebutton idle "UI/try-again-button.png" action [Hide("game_over"), Show("screen_for_memory_game_menu")], SPlay("click") align(0.5, 0.45) at half_size
            imagebutton idle "UI/quit-button.png" align(0.5, 0.9) action Jump("after_the_game_be_first"), SPlay("click") at half_size


screen screen_for_memory_game_menu:
    modal True 
    image "laptop_keyboard_resize.jpg"
    frame:
        background "#06646980"
        xfill True
        yfill True
        frame:
            xysize(774, 470)
            align (0.5, 0.5)
            text "Difficulty: [current_difficulty]" size 40 color "#45f4f1" outlines[(absolute(2), "#00959d", 0, 0)] align(0.5, 0.30)
            imagebutton idle "UI/arrow-left.png" align(0.1, 0.30) action Function(set_difficulty, button = "left"), SPlay("click") at half_size
            imagebutton idle "UI/arrow-right.png" align(0.9, 0.30) action Function(set_difficulty, button = "right"), SPlay("click") at half_size
            imagebutton idle "UI/play-button.png" align(0.2, 0.8) action [Hide("screen_for_memory_game_menu"), Show("screen_for_memory_game")], SPlay("click") at half_size
            imagebutton idle "UI/quit-button.png" align(0.8, 0.8) action Jump("after_the_game_be_first"), SPlay("click") at half_size
            
screen screen_for_memory_game:
    on "show" action Function(reset_memory_game), SPlay("gamewin")
    image "laptop_keyboard_resize.jpg"
    if red_button_lit:
        imagebutton idle "red-button-lit.png" align(0.35, 0.25) at half_size
    elif not red_button_lit:
        imagebutton auto "red-button-%s.png" align(0.35, 0.25) action [SetVariable("red_button_lit", True), Function(check_user_input, button = "red")] sensitive input_ready at half_size
    if blue_button_lit:
        imagebutton idle "blue-button-lit.png" align(0.65, 0.20) at half_size
    elif not blue_button_lit:
        imagebutton auto "blue-button-%s.png" align(0.65, 0.20) action [SetVariable("blue_button_lit", True), Function(check_user_input, button = "blue")] sensitive input_ready at half_size
    if green_button_lit:
        imagebutton idle "green-button-lit.png" align(0.35, 0.75) at half_size
    elif not green_button_lit:
        imagebutton auto "green-button-%s.png" align(0.35, 0.75) action [SetVariable("green_button_lit", True), Function(check_user_input, button = "green")] sensitive input_ready at half_size
    if yellow_button_lit:
        imagebutton idle "yellow-button-lit.png" align(0.65, 0.75) at half_size
    elif not yellow_button_lit:
        imagebutton auto "yellow-button-%s.png" align(0.65, 0.75) action [SetVariable("yellow_button_lit", True), Function(check_user_input, button = "yellow")] sensitive input_ready at half_size
    
    if not input_ready:
        timer 1.0 action Function(light_buttons) repeat True
    if red_button_lit or blue_button_lit or green_button_lit or yellow_button_lit:
        timer 0.5 action Function(off_buttons) repeat True

label memory_game:
    python:
        def create_button_pattern(type):
            pattern = []
            if type == "easy":
                # easy - just press 4 buttons
                for  i in range(4):
                    pattern.append(renpy.random.randint(0, 3))
            if type == "medium":
                # medium - just press 7 buttons
                for  i in range(7):
                    pattern.append(renpy.random.randint(0, 3))
            if type == "hard":
                # hard - just press 10 buttons
                for  i in range(10):
                    pattern.append(renpy.random.randint(0, 3))
            
            return pattern
        
        def set_difficulty(button):
            global current_difficulty
            if button == "right" and difficulties.index(current_difficulty) < len(difficulties) - 1:
                current_difficulty = difficulties[difficulties.index(current_difficulty) + 1]
            elif button == "left" and difficulties.index(current_difficulty) > 0:
                current_difficulty = difficulties[difficulties.index(current_difficulty) - 1]
            renpy.restart_interaction()

        def light_buttons():                                  
            global input_ready
            global correct_piks
            global current_button_index 
            global red_button_lit
            global blue_button_lit
            global green_button_lit
            global yellow_button_lit

            if current_button_index < len(current_button_pattern):
                button_lit = buttons[current_button_pattern[current_button_index]]
                if button_lit == "red":
                    splay("click")
                    red_button_lit = True
                    blue_button_lit = False
                    green_button_lit = False
                    yellow_button_lit = False
                elif button_lit == "blue":
                    splay("click")
                    red_button_lit = False
                    blue_button_lit = True
                    green_button_lit = False
                    yellow_button_lit = False
                elif button_lit == "green":
                    splay("click")
                    red_button_lit = False
                    blue_button_lit = False
                    green_button_lit = True
                    yellow_button_lit = False
                elif button_lit == "yellow":
                    splay("click")
                    red_button_lit = False
                    blue_button_lit = False
                    green_button_lit = False
                    yellow_button_lit = True

                if correct_piks == current_button_index:
                    input_ready = True
                    correct_piks = 0
                current_button_index += 1
                renpy.restart_interaction()
            else:
                splay("click")
                input_ready = True
                renpy.restart_interaction(screen_for_memory_game_menu)

        def off_buttons():
            global red_button_lit
            global blue_button_lit
            global green_button_lit
            global yellow_button_lit
            red_button_lit = False
            blue_button_lit = False
            green_button_lit = False
            yellow_button_lit = False

        def check_user_input(button):
            global current_button_index
            global input_ready
            global correct_piks
            global user_picks
            global selected_button_index

            if buttons.index(button) == current_button_pattern[selected_button_index]:
                splay("click")
                correct_piks += 1
                user_picks += 1
                if current_button_index == user_picks:
                    selected_button_index = 0
                    current_button_index =0
                    user_picks = 0
                    input_ready = False
                else:
                    selected_button_index += 1
                renpy.restart_interaction()
            else:
                splay("gameover")
                renpy.show_screen("game_over")
                renpy .hide_screen("screen_for_memory_game")
            if correct_piks == len(current_button_pattern):
                renpy.show_screen("screen_for_memory_game_menu")
                renpy.transition(Fade(1, 0, 1))
                renpy.hide_screen("screen_for_memory_game")

        def reset_memory_game():
            splay("gamewin")
            global current_button_index
            global selected_button_index
            global input_ready
            global correct_piks
            global user_piks
            global current_button_pattern
            global red_button_lit
            global blue_button_lit
            global green_button_lit
            global yellow_button_lit

            current_button_index = 0
            selected_button_index = 0
            correct_piks = 0
            user_picks = 0
            input_ready = False

            red_button_lit = False
            blue_button_lit = False
            green_button_lit = False
            yellow_button_lit = False

            current_button_pattern = create_button_pattern(type = current_difficulty)
            renpy.restart_interaction()

 
    
    $ current_button_pattern = []
    $ difficulties = ["easy", "medium", "hard"]
    $ current_difficulty = "easy"
    $ red_button_lit = False
    $ blue_button_lit = False
    $ green_button_lit = False
    $ yellow_button_lit = False
    $ buttons = ("red", "blue", "green", "yellow")
    $ current_button_index = 0
    $ input_ready = False
    $ correct_piks = 0
    $ user_picks = 0
    $ selected_button_index = 0

    call screen screen_for_memory_game_menu


    return





screen game_over_2:
    image "laptop_keyboard_resize.jpg"
    frame:
        background "#06646980"
        xfill True
        yfill True
        frame:
            background None
            xysize (774, 470)
            align (0.5, 0.5)
            text "You got the wrong button...\nTry again?" size 45 color "#45f4f1" outlines[(absolute(2), "#00959d", 0, 0)] align(0.5, 0.10) text_align 0.5
            imagebutton idle "UI/try-again-button.png" action [Hide("game_over_2"), Show("screen_for_memory_game_menu_2")], SPlay("click") align(0.5, 0.45) at half_size
            imagebutton idle "UI/quit-button.png" align(0.5, 0.9) action Jump("after_the_game_be_first_2"), SPlay("click") at half_size


screen screen_for_memory_game_menu_2:
    modal True 
    image "laptop_keyboard_resize.jpg"
    frame:
        background "#06646980"
        xfill True
        yfill True
        frame:
            xysize(774, 470)
            align (0.5, 0.5)
            text "Difficulty: [current_difficulty_2]" size 40 color "#45f4f1" outlines[(absolute(2), "#00959d", 0, 0)] align(0.5, 0.30)
            imagebutton idle "UI/arrow-left.png" align(0.1, 0.30) action Function(set_difficulty_2, button = "left"), SPlay("click") at half_size
            imagebutton idle "UI/arrow-right.png" align(0.9, 0.30) action Function(set_difficulty_2, button = "right"), SPlay("click") at half_size
            imagebutton idle "UI/play-button.png" align(0.2, 0.8) action [Hide("screen_for_memory_game_menu_2"), Show("screen_for_memory_game_2")], SPlay("click") at half_size
            imagebutton idle "UI/quit-button.png" align(0.8, 0.8) action Jump("after_the_game_be_first_2"), SPlay("click") at half_size
            
screen screen_for_memory_game_2:
    on "show" action Function(reset_memory_game_2), SPlay("gamewin")
    image "laptop_keyboard_resize.jpg"
    if red_button_lit_2:
        imagebutton idle "red-button-lit.png" align(0.35, 0.25) at half_size
    elif not red_button_lit_2:
        imagebutton auto "red-button-%s.png" align(0.35, 0.25) action [SetVariable("red_button_lit_2", True), Function(check_user_input_2, button = "red")] sensitive input_ready_2 at half_size
    if blue_button_lit_2:
        imagebutton idle "blue-button-lit.png" align(0.65, 0.20) at half_size
    elif not blue_button_lit_2:
        imagebutton auto "blue-button-%s.png" align(0.65, 0.20) action [SetVariable("blue_button_lit_2", True), Function(check_user_input_2, button = "blue")] sensitive input_ready_2 at half_size
    if green_button_lit_2:
        imagebutton idle "green-button-lit.png" align(0.35, 0.75) at half_size
    elif not green_button_lit_2:
        imagebutton auto "green-button-%s.png" align(0.35, 0.75) action [SetVariable("green_button_lit_2", True), Function(check_user_input_2, button = "green")] sensitive input_ready_2 at half_size
    if yellow_button_lit_2:
        imagebutton idle "yellow-button-lit.png" align(0.65, 0.75) at half_size
    elif not yellow_button_lit_2:
        imagebutton auto "yellow-button-%s.png" align(0.65, 0.75) action [SetVariable("yellow_button_lit_2", True), Function(check_user_input_2, button = "yellow")] sensitive input_ready_2 at half_size
    
    if not input_ready_2:
        timer 1.0 action Function(light_buttons_2) repeat True
    if red_button_lit_2 or blue_button_lit_2 or green_button_lit_2 or yellow_button_lit_2:
        timer 0.5 action Function(off_buttons_2) repeat True

label memory_game_2:
    python:
        def create_button_pattern_2(type):
            pattern_2 = []
            if type == "easy":
                # easy - just press 4 buttons
                for  i in range(4):
                    pattern_2.append(renpy.random.randint(0, 3))
            if type == "medium":
                # medium - just press 7 buttons
                for  i in range(7):
                    pattern_2.append(renpy.random.randint(0, 3))
            if type == "hard":
                # hard - just press 10 buttons
                for  i in range(10):
                    pattern_2.append(renpy.random.randint(0, 3))
            
            return pattern_2
        
        def set_difficulty_2(button):
            global current_difficulty_2
            if button == "right" and difficulties_2.index(current_difficulty_2) < len(difficulties_2) - 1:
                current_difficulty_2 = difficulties_2[difficulties_2.index(current_difficulty_2) + 1]
            elif button == "left" and difficulties_2.index(current_difficulty_2) > 0:
                current_difficulty_2 = difficulties_2[difficulties_2.index(current_difficulty_2) - 1]
            renpy.restart_interaction()

        def light_buttons_2():                                  
            global input_ready_2
            global correct_piks_2
            global current_button_index_2 
            global red_button_lit_2
            global blue_button_lit_2
            global green_button_lit_2
            global yellow_button_lit_2

            if current_button_index_2 < len(current_button_pattern_2):
                button_lit = buttons_2[current_button_pattern_2[current_button_index_2]]
                if button_lit == "red":
                    splay("click")
                    red_button_lit_2 = True
                    blue_button_lit_2 = False
                    green_button_lit_2 = False
                    yellow_button_lit_2 = False
                elif button_lit == "blue":
                    splay("click")
                    red_button_lit_2 = False
                    blue_button_lit_2 = True
                    green_button_lit_2 = False
                    yellow_button_lit_2 = False
                elif button_lit == "green":
                    splay("click")
                    red_button_lit_2 = False
                    blue_button_lit_2 = False
                    green_button_lit_2 = True
                    yellow_button_lit_2 = False
                elif button_lit == "yellow":
                    splay("click")
                    red_button_lit_2 = False
                    blue_button_lit_2 = False
                    green_button_lit_2 = False
                    yellow_button_lit_2 = True

                if correct_piks_2 == current_button_index_2:
                    input_ready_2 = True
                    correct_piks_2 = 0
                current_button_index_2 += 1
                renpy.restart_interaction()
            else:
                splay("click")
                input_ready_2 = True
                renpy.restart_interaction(screen_for_memory_game_menu_2)

        def off_buttons_2():
            global red_button_lit_2
            global blue_button_lit_2
            global green_button_lit_2
            global yellow_button_lit_2
            red_button_lit_2 = False
            blue_button_lit_2 = False
            green_button_lit_2 = False
            yellow_button_lit_2 = False

        def check_user_input_2(button):
            global current_button_index_2
            global input_ready_2
            global correct_piks_2
            global user_picks_2
            global selected_button_index_2

            if buttons_2.index(button) == current_button_pattern_2[selected_button_index_2]:
                splay("click")
                correct_piks_2 += 1
                user_picks_2 += 1
                if current_button_index_2 == user_picks_2:
                    selected_button_index_2 = 0
                    current_button_index_2 = 0
                    user_picks_2 = 0
                    input_ready_2 = False
                else:
                    selected_button_index_2 += 1
                renpy.restart_interaction()
            else:
                splay("gameover")
                renpy.show_screen("game_over_2")
                renpy .hide_screen("screen_for_memory_game_2")
            if correct_piks_2 == len(current_button_pattern_2):
                renpy.show_screen("screen_for_memory_game_menu_2")
                renpy.transition(Fade(1, 0, 1))
                renpy.hide_screen("screen_for_memory_game_2")

        def reset_memory_game_2():
            splay("gamewin")
            global current_button_index_2
            global selected_button_index_2
            global input_ready_2
            global correct_piks_2
            global user_piks
            global current_button_pattern_2
            global red_button_lit_2
            global blue_button_lit_2
            global green_button_lit_2
            global yellow_button_lit_2

            current_button_index_2 = 0
            selected_button_index_2 = 0
            correct_piks_2 = 0
            user_picks_2 = 0
            input_ready_2 = False

            red_button_lit_2 = False
            blue_button_lit_2 = False
            green_button_lit_2 = False
            yellow_button_lit_2 = False

            current_button_pattern_2 = create_button_pattern_2(type = current_difficulty_2)
            renpy.restart_interaction()

 
    
    $ current_button_pattern_2 = []
    $ difficulties_2 = ["easy", "medium", "hard"]
    $ current_difficulty_2 = "easy"
    $ red_button_lit_2 = False
    $ blue_button_lit_2 = False
    $ green_button_lit_2 = False
    $ yellow_button_lit_2 = False
    $ buttons_2 = ("red", "blue", "green", "yellow")
    $ current_button_index_2 = 0
    $ input_ready_2 = False
    $ correct_piks_2 = 0
    $ user_picks_2 = 0
    $ selected_button_index_2 = 0

    call screen screen_for_memory_game_menu_2


    return