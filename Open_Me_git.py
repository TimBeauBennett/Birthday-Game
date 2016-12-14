import time

dict = {
    'bear': False,
    'honey': False,
    'wizard': False,
    'sword': False,
    'key': False,
    'candle': False,
    'gun': False,
    'book': False,
    'chaplin': False,
    'lock': False,
    'bar': False,
    'lover': 'Me',
    'mogget': 'Cat',
}

def speed():
    global x1; global x2; global x3
    (x1, x2, x3) = (1, 2.5, 3)
    start()

def wait(x):
    time.sleep(x)

def start():
    print '.'; wait(x1); print '.'; wait(x1); print '.'; wait(x1)
    print "'Good morning!'"; wait(x2)
    print "You hear a very loud, obnoxious voice in the morning."; wait(x2)
    print "If you weren't in love with them, you'd be annoyed :)"; wait(x2)
    print "You're still a bit groggy though, what is your lover's name again?"
    dict['lover'] = raw_input("> ")
    print "That's right, %s sure is pretty. You wouldn't want anything to happen to them." % dict['lover']; wait(x2)
    print "'Happy birthday by the w...'"
    print '.'; wait(x1); print '.'; wait(x1); print '.'
    print "Crack!"; wait(x2)
    print "%s is being surrounded by a cloud of smoke! %s's gone! Totally gone!" % (dict['lover'], dict['lover'])
    print '.'; wait(x3)
    print "Another cloud of smoke appears at the end of your bed"; wait(x2)
    print "It's swirling into a vortex...rising up from the ground!"; wait(x2)
    print "As the smoke clears, you see the outline of a man, an two piercing eyes in the smoke."; wait(x2)
    print "'Happy birthday indeed...' you hear a sinister voice from the smoke"; wait(x2)
    print "'I'm very sorry, but %s is just...too pretty.'" % dict['lover']; wait(x2)
    print "'I am in need of this prettiness. It is for the greater good, I promise'"; wait(x2)
    print "You hear it speak again, as it starts to fade into nothing"
    print "'I would ask your permission to borrow %s'" % dict['lover']; wait(x2)
    print "'But I have no intention of bringing them back!!!!''"; wait(x1)
    print "HAHAHAHAHAHAHAHA!!!!!"; wait(x2)
    print "\nThe smoke clears, leaving nothing but empty space."; wait(x2)
    print "You look to where %s was a moment ago, hoping it was all a dream" % dict['lover']
    wait(x2)
    print "But there again, all you see is empty space..."; wait(x2)
    choice()

def choice():
    print "What will you do now?"; wait(x1)
    print "\n\t1. Cry a pool of milky tears for you lost love."; wait(x1)
    print "\t2. Resolve to find out who took your lover, and begin the search!"; wait(x1)
    print "\t3. Eat the breakfast %s made you before making a decision." % dict['lover']; wait(x1)
    action = raw_input("> "); wait(x1)
    if action == '1':
        print "\nYou miss %s so much, you can't help but burst into tears!" % dict['lover']; wait(x2)
        print "You hear a voice..."; wait(x2)
        print "'Well that's a fairly useless response the situation isn't it?'"; wait(x2)
        mogget()
    elif action == '2':
        print "\nYou resolve to jump to action and get %s back!" % dict['lover']; wait(x2)
        print "You hear a voice..."; wait(x2)
        print "'I'm impressed! I really thought you'd eat the bacon sandwich."; wait(x2)
        mogget()
    elif action == '3':
        print "\nYou put %s out of your mind, and tuck into a tasty bacon sandwich." % dict['lover']; wait(x2)
        print "You hear a voice..."; wait(x2)
        print "'That's a pretty selfish response the situation isn't it?'"; wait(x2)
        mogget()
    else:
        print "You should learn to type a number. Try again."; wait(x1)
        choice()

def mogget():
    print "You look toward the sound of the voice and see a...white cat."; wait(x3)
    print "\n'Never seen a cat before have you?'"; wait(x2)
    print "\n\t1. Well not one that can speak."; wait(x1)
    print "\t2. It's not that, I just hate cats."; wait(x1)
    print "\t3. I'm allergic to cats, so just stay away from me."; wait(x1)
    cats = raw_input("> "); wait(x1)

    if cats == '1':
        print "\n'You still haven't. I'm not a cat. Don't ask about my true form.'"; wait(x2)
        troo_form()
    elif cats == '2':
        print "'Me too, but they don't scare people. Don't ask about my true form.'"; wait(x2)
        troo_form()
    elif cats == '3':
        print "'It's cool, short fur. Also not a cat. Don't ask about my true form.'"; wait(x2)
        troo_form()
    else:
        print "'If you don't learn to type a number you're gonna have a bad time.'"; wait(x2)
        print "'Anyway, I'm not a real cat. Don't ask about my true form.'"; wait(x2)
        troo_form()

def troo_form():
    print "\n\t1. Ask about true form"; wait(x1)
    print "\t2. Don't ask about true form. Seriously, choose this option..."; wait(x1)
    form = raw_input("\n> "); wait(x1)
    if form == '1':
        print "\n'I told you not to do that...'"; wait(x2)
        print "The cat begins to glow..."; wait(x2)
        print "'BOOM YOU DIED HAHAHAHAHAHAHAHA'"; wait(x2)
        print "'Nah jokes, you're fine. Let's go.'"; wait(x1)
        teleport()
    elif form == '2':
        print "\n'Thanks, I was gonna pretend to kill you if you asked.'"; wait(x2)
        print "'Let's go.''"; wait(x1)
        teleport()
    else:
        print "\n'Look, I'm just gonna assume you meant nuber 2 and not kill you;"; wait(x2)
        print "'Let's go.''"
        teleport()

def teleport():
    print "\nYou wait in anticipation, for a hum, a glow, a fade..."; wait(x2)
    print "Instead, you just hear a..."; wait(x2)
    print "\n\tPOP!\n"; wait(x2)
    print "You look around to totally new surroundings - You're outside!"; wait(x2)
    print "'What?' says the cat, now at your feet. 'Expecting a glow, or a hum?'"; wait(x2)
    print "'Real magic is like science. Boring and useful.'"; wait(x2)
    print "Magic. It makes you think of %s." % dict['lover']; wait(x2)
    print "'Yes, I thought you might like to know what happened.'"; wait(x2)
    print "\n'%s's quite pretty, you might have noticed.'" % dict['lover']; wait(x2)
    print "'Well, in this realm, prettiness is a conduit to magical foces.'"; wait(x2)
    print "'%s was stolen by the evil warlock Zoblochk. The evil eye guy.'" % dict['lover']; wait(x2)
    print "'Zoblochk used his prettiness to extend his life, unnaturally.'"; wait(x2)
    print "'So now he steals pretty people to feed his magical desires.'"; wait(x2)
    print "'That's his tower. Now we go save %s.'" % dict['lover']; wait(x2)
    print "'Before we go, I'll need a name. Any ideas?'"; wait(x1)
    dict['mogget'] = raw_input("\n> "); wait(x1)
    print "%s: 'Well. There's no accounting for taste.'" % dict['mogget']; wait(x2)
    quest()

def quest():
    print "\nYou're in a field, on top of a small mound."; wait(x1)
    print "\tTo the North, a short path leads to a tall tower."; wait(x1)
    print "\tTo the East, there lies a narrow ravine."; wait(x1)
    print "\tTo the West, a rocky outcrop springs from the ground."; wait(x1)
    print "\tTo the South, a boat is docked at a harbour."; wait(x1)
    choose_go()

def choose_go():
    print "\nWill you go East, West, North or South?"; wait(x2)
    go = raw_input("> "); wait(x1)
    if go == 'east':# or 'East':
        east()
    elif go == 'west':# or 'West':
        west()
    elif go == 'north':# or 'North':
        north()
    elif go == 'south':# or 'South':
        south()
    else:
        print "%s: 'You have to pick one. Try again.'" % dict['mogget']; wait(x2)
        choose_go()

def east():
    if dict['bear'] == False and dict['honey'] == False:
        east1()
    elif dict['bear'] == True and dict['honey'] == True:
        print "You find a sticky spot at the end of the ravine. Gross."; wait(x2)
        print "You go back to the hill."; wait(x2)
        quest()
    elif dict['bear'] == True and dict['honey'] == False:
        print "There is a pot of honey on the ground."; wait(x2)
        print "\n\t1. Take the honey and go back to the hill."; wait(x2)
        print "\t2. Go back to the hill."; wait(x2)
        get_honey = raw_input("> "); wait(x1)
        if get_honey == '1':
            print "Got the honey. Great! You go back to the hill."; wait(x2)
            dict['honey'] = True
            quest()
        elif get_honey == '2':
            wait(x2)
            quest()
        else:
            print "%s: 'Just...type a number. Try again.'" % dict['mogget']; wait(x2)
            choose_go()
    else:
        print "east broke"
        choose_go()

#east1 should be split into it's intro and choice functions

def east1():
    print "\nYou walk through narrow ravine."; wait(x2)
    print "You turn the corner at the end and see a huge Bear!"; wait(x2)
    print "The bear is eating a pot of honey."; wait(x2)
    print "What will you do?"; wait(x2)
    print "\n\t1. Fight the bear."; wait(x2)
    print "\t2. Politely ask the Bear for his honey."; wait(x2)
    print "\t3. Joke: 'A pot that big puts you on par with Winnie the Pooh!''"; wait(x2)
    print "\t4. Make like a tree and get outta there!"; wait(x2)
    boo_choice = raw_input("\n> "); wait(x1)
    if boo_choice == '1':
        print "You wind back your fist and smack the bear straight on the nose!"; wait(x2)
        print "Bear: '...'"; wait(x2)
        bear_scare()
    elif boo_choice == '2':
        print "You ask the bear to politely move"; wait(x2)
        print "The bear look at you suspiciously."; wait(x2)
        print "%s: 'He only speaks bear, you dill.'" % dict['mogget']; wait(x2)
        print "You politely growoowl the bear for his honey."; wait(x2)
        print "The bear appears highly amused at your thick accent."; wait(x2)
        print "It grooowoal's to you that you can have what's left."; wait(x2)
        print "Unfortunately, you don't understand bear as well as you speak it."; wait(x2)
        print "So all you hear is..."; wait(x1)
        dict['bear'] = True
        bear_scare()
    elif boo_choice == '3':
        print "You make a hilarious quip about Disney's classic teddy."; wait(x2)
        print "The bear looks at you suspiciously."; wait(x2)
        print "%s: 'Got a follow up?'" % dict['mogget']; wait(x2)
        print "\n\t1. 'Winnie-the-Pooh is so fat that when he stepped on the scales it said To Be Continued.'"; wait(x2)
        print "\t2. 'What does Winnie-the-Pooh and Jabba the Hutt have in common? The same middle name.'"; wait(x2)
        joke = raw_input("> ")
        if joke == '1':
            print "Bear: '...'"; wait(x2)
            bear_scare()
        elif joke == '2':
            print "Bear: '...'"; wait(x2)
            print "\nRABABRABRABRABRABRARARBABABRABRBAR!!!!!"; wait(x2)
            print "\n%s: 'Phew, he likes the reference.'" % dict['mogget']; wait(x2)
            print "The bear, in a fit, wanders off, leaving the honey."; wait(x2)
            print "You pick up the honey, and head back to the hill."; wait(x2)
            dict['bear'] = True; dict['honey'] = True
            quest()
        else:
            print "%s: 'You have to pick one. Try again.'" % dict['mogget']; wait(x2)
            east1()
    elif boo_choice == '4':
        print "You run back to the hill!"; wait(x2)
        quest()
    else:
        print "%s: 'You should learn to type a number.'" % dict['mogget']; wait(x2)
        east1()

def bear_scare():
    print "\nROAAAAAAAAAAARRRRRRRRRR"; wait(x2)
    print "You run for you life out of the ravine!!!"; wait(x2)
    quest()

def south():
    if dict['honey'] == False and dict['wizard'] == False:
        south2()
    elif dict['honey'] == True and dict['wizard'] == False:
        south1()
    elif dict['wizard'] == True:
        print "\nYou see a boat, floating a little way off shore."; wait(x2)
        print "You hear a faint whistling, an out of tune sea shanty."; wait(x2)
        print "Not much else to see here. Cept that stupid boulder. U a baus."; wait(x2)
        print "You give the boulder a nudge and head back to the hill."; wait(x2)
        quest()
    else:
        print 'what'

def south1():
    print "\nYou walk down a worn path to a medium sized boat, docked in a small harbour."; wait(x2)
    print "There is a cloaked lady-hobo sitting on the ground near the water."; wait(x2)
    print "'Can you spare any food? I haven't eaten for days' she says."; wait(x2)
    print "\n\t1. Apologise, telling her you have no food."; wait(x2)
    print "\t2. Offer her what's left of the bear's honey."; wait(x2)
    print "\t3. Ignore her and go back to the hill."; wait(x2)
    foodo1 = raw_input("> "); wait(x1)
    if foodo1 == '1':
        print "You apologise, as you're hungry yourself."; wait(x2)
        print "'I understand' he says, 'let me know if you can spare any later'."; wait(x2)
        print "%s: 'I don't know why, but I feel like we should help him...'"; wait(x2)
        south()
    elif foodo1 == '2':
        print "You offer the lady-hobo what's left of the honey."; wait(x2)
        print "'What a generous soul' she says."; wait(x2)
        wizkid()
    elif foodo1 == '3':
        print "%s: 'Asshole'." % dict['mogget']; wait(x2)
        print "You go back to the hill."; wait(x2)
        quest()
    else:
        print "%s: 'You should learn to type a number.'" % dict['mogget']; wait(x2)
        south()

def south2():
    print "\nYou walk down a worn path to a medium sized boat, docked in a small harbour."; wait(x2)
    print "There is a cloaked lady-hobo sitting on the ground near the water."; wait(x2)
    print "'Can you spare any food? I haven't eaten for days' she says."; wait(x2)
    print "What do you do?"; wait(x2)
    print "\n\t1. Apologise, telling her you have no food."; wait(x2)
    print "\t2. Tell her you'll try and get some, and go back to the hill."; wait(x2)
    print "\t3. Ignore her and go back to the hill."; wait(x2)
    foodo = raw_input("> "); wait(x1)
    if foodo == '1':
        print "You apologise, as you're hungry yourself."; wait(x2)
        print "'I understand' she says, 'let me know if you can spare any later'."; wait(x2)
        print "%s: 'I don't know why, but I feel like we should help her...'"% dict['mogget']; wait(x2)
        print "You go back to the hill."; wait(x2)
        quest()
    elif foodo == '2':
        print "%s: 'I don't know why, but I feel like we should help her...'" % dict['mogget']; wait(x2)
        print "You tell the lady-hobo you'll try and find some food."; wait(x2)
        print "'That's very kind of you' she says, 'I'll just wait here."; wait(x2)
        print "You go back to the hill."; wait(x2)
        quest()
    elif foodo == '3':
        print "%s: 'Asshole'." % dict['mogget']; wait(x2)
        print "You go back to the hill."; wait(x2)
        quest()
    else:
        print "%s: 'You should learn to type a number.'" % dict['mogget']; wait(x2)
        south()

def wizkid():
    print "With no warning or transistion, the lady-hobo becomes a powerful lady-wizard!"; wait(x2)
    print "%s: 'Told you, boring and useful, puffs of smoke are just impractical.'" % dict['mogget']; wait(x2)
    print "You're unimpressed at the lack of spectacle, but you focus on the wizard.'"; wait(x2)
    print "'I am the Wizkid!' she says, although she's clearly at least 30."; wait(x2)
    print "'Shush' she says, reading your mind. 'I'm 576 years old. So there.'"; wait(x2)
    print "'Thank you for your kindness. I wish to assist you in your journey.'"; wait(x2)
    print "'You're after your good for nothing lover? So that was the incredible prettiness I felt...'"; wait(x2)
    print "'I cannot directly help you, as I must go fishing...But you will find this useful.'"; wait(x2)
    print "The Wizkid immediately appears on the boat, rod in hand. 'Good luck!' she shouts, as she leaves.\n"; wait(x2)
    print "%s: '...'" % dict['mogget']; wait(x2)
    print "You shoot %s a sour look before he gets the chance." % dict['mogget']; wait(x2)
    print "%s: 'Fair enough. But it looks like you have super strength now." % dict['mogget']; wait(x2)
    print "%s: 'Try thinking about moving that rock, then push it.'" % dict['mogget']; wait(x2)
    print "You picture yourself rippling with muscles, bursting from your skin!"; wait(x2)
    print "Placing you hands on a great boulder, you push!"; wait(x2)
    print "Yup. It moved. %s was right. You're amazed. Who expected that. Not me. Defs not me." % dict['mogget']; wait(x2)
    print "'See, boring and useful!' says %s, running to the hill before you can smack him." % dict['mogget']; wait(x2)
    print "You go back to the hill."; wait(x2)
    dict['wizard'] = True
    quest()

def west():
    if dict['wizard'] == True:
        win_sword()
    elif dict['wizard'] == False:
        fail_sword()
    else:
        print 'You broke something. Nice. West function.'

def fail_sword():
    print "You navigate a rocky outcrop, down into a valley."; wait(x2)
    print "You feel a strange heat as you enter a clearing."; wait(x2)
    print "There, at the bottom of the clearing, is a sword!"; wait(x2)
    print "IN A STONE!"; wait(x2)
    print "You break the proverbial fourth wall, astounded at the lack of imagination."; wait(x2)
    print "Whatever. How many video games have you written? Anyway, what's next?"; wait(x2)
    print "\n\t1. Pull that sucker out!"; wait(x1)
    print "\t2. Be a cynic and walk away. Go on. See if I care."; wait(x1)
    pullo = raw_input("> ")
    if pullo == '1':
        print "\nYou yank, with ALL YOUR MIGHT!!!"; wait(x2)
        print "YELL WITH ME!!! ARRRRRGGGHHH!!!!!"; wait(x2)
        print "YOU'RE NOT YELLING!!! ACTUALLY DO IT!!! AHHHHH!!!"; wait(x2)
        print "YARARARGARHASGRHASGRHASRGHASGRHASGRHARSGHARSGHARSGH!!!!!"; wait(x2)
        print "Yeah, nah."; wait(x2)
        print "You go back to the hill."; wait(x1)
        quest()
    elif pullo == '2':
        print "\nAs you go back to the hill, the Spirit of Adventure dies."; wait(x2)
        print "Nice."; wait(x2)
        quest()

def win_sword():
    print "You navigate a rocky outcrop, down into a valley."; wait(x2)
    print "You feel a strange heat as you enter a clearing."; wait(x2)
    print "There, at the bottom of the clearing, is a sword!"; wait(x2)
    print "IN A STONE!"; wait(x2)
    print "You don't seem impressed. Whatever, I don't care. What next?"; wait(x2)
    print "\n\t1. Pull that sucker out! WITH MAGIC!"; wait(x1)
    print "\t2. Waste what is a very convinient magical ability and leave."; wait(x1)
    pullo = raw_input("> ")
    if pullo == '1':
        print "\nYou think hard about your super strength."; wait(x2)
        print "You expect to do a lot of screaming, as you grasp the hilt."; wait(x2)
        print "And the thing just slides out, super easy."; wait(x2)
        print "You tuck the sword in you belt, avoiding %s's smug gaze." % dict['mogget']; wait(x2)
        print "You go back to the hill."; wait(x1)
        dict['sword'] = True
        quest()
    elif pullo == '2':
        print "\nAs you go back to the hill, the Spirit of Adventure dies."; wait(x2)
        print "Nice."; wait(x2)
        quest()

def north():
    if dict['sword'] == True:
        wiz_door()
    elif dict['sword'] == False:
        door()
    else:
        print "North broke"
        quest()

def door():
    print "\nYou approach a landing in front of a tall tower."; wait(x2)
    print "%s: 'That's Zoblochk's tower. %s will be in there.'" % (dict['mogget'], dict['lover']); wait(x2)
    print "There is nothing on the tower besides a well tended door."; wait(x2)
    print "There is a nice flower bed, but otherwise, a bit cliche."; wait(x2)
    print "What now?"; wait(x2)
    print "\n\t1. Bash down the door!"; wait(x1)
    print "\t2. Head back to the hill."; wait(x1)
    print "\t3."; wait(x1)
    door_choice = raw_input("> ")
    print "\n"
    if door_choice == '1':
        print "You have a solid crack and knocking down the door, to no avail."; wait(x2)
        print "Brute force won't do it. You head back to the hill."; wait(x2)
        quest()
    elif door_choice == '2':
        print "Not the time for that. You head back to the hill."; wait(x2)
        quest()
    elif door_choice == '3':
        if dict['key'] == False:
            print "You inspect the flowers closer, they smell lovely!"; wait(x2)
            print "You see a small flash from the dirt...a key!"; wait(x2)
            print "Got the key. That might be useful."; wait(x2)
            print "You go back to the hill."; wait(x1)
            dict['key'] = True
            quest()
        elif dict['key'] == True:
            print "You inspect the flowers closer, they smell lovely!"; wait(x2)
            print "You go back to the hill."; wait(x1)
            quest()
        else:
            print "broke"
            quest()
    else:
        print "broke"
        quest()

def wiz_door():
    print "\nYou approach a landing in front of a tall tower."; wait(x2)
    print "%s: 'That's Zoblochk's tower. %s will be in there.'" % (dict['mogget'], dict['lover']); wait(x2)
    print "There is nothing on the tower besides a well tended door."; wait(x2)
    print "There is a nice flower bed, but otherwise, a bit cliche."; wait(x2)
    print "What now?"; wait(x2)
    print "\n\t1. Slice down the door! With the sword!!!"; wait(x1)
    print "\t2. Head back to the hill."; wait(x1)
    door_choice = raw_input("> ")
    print "\n"
    if door_choice == '1':
        print "The door falls before your sword! It lies in splinters."; wait(x2)
        print "You tuck the sword away, and head through the door."; wait(x2)
        tower()
    elif door_choice == '2':
        print "Not the time for that. You head back to the hill."; wait(x2)
        quest()
    else:
        print "broke"
        quest()

def tower():
    print "\nYou enter the a round room at the base of the tower"; wait(x2)
    print "There are three doors, left, right and forward."; wait(x2)
    print "The forward door has a bar across it."; wait(x2)
    print "What now?"; wait(x1)
    print "\n\t1. Inspect the left door."; wait(x1)
    print "\t2. Inspect the right door."; wait(x1)
    print "\t3. Inspect the forward door."; wait(x1)
    door = raw_input("> ")
    if door == '1':
        left_door()
    elif door == '2':
        right_door()
    elif door =='3':
        bar_check()
    else:
        print "%s: 'Why not try a number? You can do it!'" % dict['mogget']
        tower()


def left_door():
    print "\nYou try the left door, and it opens easily."; wait(x2)
    print "Candle chandoliers flick light across a trophy room."; wait(x2)
    print "There are hunting trophies on every wall."; wait(x2)
    print "The centre of the room has a desk, with a long draw."; wait(x2)
    print "What next?"; wait(x2)
    print "\n\t1. Inspect the chandoliers."; wait(x1)
    print "\t2. Inspect the desk."; wait(x1)
    print "\t3. Go back to the round room."; wait(x1)
    left_choice = raw_input("> "); wait(x1)
    if left_choice == '1':
        chandolier()
    elif left_choice == '2':
        desk()
    elif left_choice == '3':
        tower()
    else:
        print "%s: 'Why not try a number? You can do it!'" % dict['mogget']
        left_door()

def chandolier():
    print "\nYou walk up to one of the candle chandoliers on the wall."; wait(x2)
    print "There are too many candles to count!"; wait(x2)
    print "You think it odd they don't look melted down..."; wait(x2)
    print "%s: 'Everlasting candles. Sure are boring and useful.'" % dict['mogget']; wait(x2)
    print "You land a slap on %s's snarkly little nose." % dict['mogget']; wait(x2)
    print "\nHe's right though. You grab an everlasting candle and go back to the room."; wait(x2)
    dict['candle'] = True
    tower()

def desk():
    print "\nYou walk up to the desk, the draw has a big lock on it."; wait(x2)
    if dict['key'] == False:
        print "You can't get into it. Bummer. You head back to the room."; wait(x2)
        tower()
    elif dict['key'] == True:
        print "You try the key you found outside..."; wait(x2)
        print "It works! The top creaks as it opens..."; wait(x2)
        print "Inside is a not-so-antique blunderbuss! It's loaded."; wait(x2)
        print "\nYou swing the strap over your back, it could be useful."; wait(x2)
        print "You go back to the room."; wait(x1)
        dict['gun'] = True
        tower()
    else:
        print "desk broke"

def right_door():
    if dict['candle'] == True:
        right_room()
    elif dict['candle'] == False:
        print "\nYou try the right door, and it creaks open."; wait(x2)
        print "The room is pitch black!"; wait(x2)
        print "There's a musty, faintly nostalgic smell you can't quite pick..."; wait(x2)
        print "It's dangerous to go stumbling around in the dark, you go back to the room."; wait(x2)
        tower()
    else:
        print "right_door broke"
        tower()

def right_room():
    print "\nYou try the right door, and it creaks open."; wait(x2)
    print "The room is pitch black!"; wait(x2)
    print "Luckily, you have a magic candle, that seems to light the entire room."; wait(x2)
    print "The room appears to be a library, with shelves from floor to ceiling on each wall."; wait(x2)
    print "The musky smell of old books tingles with nostalgia."; wait(x2)
    book_choice()

def book_choice():
    print "\nYou count 8 shelves. Which one will you pick?"; wait(x1)
    print "That, or 'exit' to go back to the room."; wait(x1)
    bookies = raw_input("> ")
    if bookies == '1':
        print "\nLots of self-development books here...you open one up."; wait(x2)
        print "'The Power Of Self Affirmation'"; wait(x2)
        print "It's part confidence boosting, part diary. You read a handwritted section."; wait(x2)
        print """\n
        \tI am a strong, confident Warlock.
        \tI am the most attractive Warlock in the Village.
        \tI earn $100,000 a month from Locking Wars.
        \tI will not let Mother continue to hassle me.
        \tWhat she said about my haricut was not true.
        \tMy part does not make me look like Charlie Chaplin.
        \tI. Do. Not. Look. Like. Charlie. Chaplin.
        """; wait(7)
        print "You close it. Partly out of respect, mostly from embarrassment."; wait(x2)
        dict['chaplin'] = True
        book_choice()
    elif bookies == '2':
        print "\nYou pull a book with a nice cover off the second shelf."; wait(x2)
        print "Looks like a fantasy based on Plato's Republic..."; wait(x1)
        print "Nooooooooooooooooope."; wait(x1)
        book_choice()
    elif bookies == '3':
        print "\nIt's crammed full of Pokemon books!"; wait(x2)
        book_choice()
    elif bookies == '4':
        print "\nMostly philosophy here, some pop psychology, 7 habits kind stuff."; wait(x2)
        print "You figure %s might like some of this." % dict['lover']; wait(x2)
        book_choice()
    elif bookies == '5':
        print "\nThere's a whole shelf of old comic books...which is odd for a Warlock..."; wait(x2)
        print "That said, all of them star Adam Warlock...which is a little predictable."; wait(x2)
        book_choice()
    elif bookies == '6':
        print "\nA series of books jumps out at you."; wait(x2)
        print "You flick through...they have a strong female protagonist..."; wait(x2)
        print "Oh, she's a necromancer? Sounds good, you take a note and put it back."; wait(x2)
        print "%s: 'Sounds a bit derivative to me. I should know.'" % dict['mogget']; wait(x2)
        book_choice()
    elif bookies == '7':
        print "\nThe entire seventh shelf is full of different sets of Harry Potter."; wait(x2)
        print "%s: 'Apparently even evil warlocks miss the spectacle of Hogwarts'." % dict['mogget']; wait(x2)
        print "You roll you eyes as he contines to mumble '...it's lev-ee-OH-sah..."; wait(x2)
        book_choice()
    elif bookies == '8':
        magic_book()
    elif bookies == 'exit':
        print "You go back to the room."; wait(x1)
        tower()
    else:
        "%s: 'Really? Number. Between 1 and 8. Don't know why I bother...'" % dict['mogget']; wait(x1)
        book_choice()

def magic_book():
    if dict['book'] == False:
        print "The eighth shelf has the oldest, muskiest books of all."; wait(x2)
        print "You have that sense there should be something humming, but there's nothing."; wait(x2)
        print "So, you correctly assume that these books are magic."; wait(x2)
        print "You open the most boring one, correctly assuming it is the most useful."; wait(x2)
        print "The pages are totally blank...all of them! You close the book, disappointed."; wait(x2)
        print "%s: 'Think about fire.'" % dict['mogget']; wait(x2)
        print "Not that there's any choice now."; wait(x2)
        print "\nTHE BOOK EXPLODES IN A FIREY BALL OF MAGIC POWER!!"; wait(x2)
        print "\nYou're okay though coz you're a fire elemental now. The book's done though."; wait(x2)
        print "You decide whether to read any more books."; wait(x1)
        dict['book'] = True
        book_choice()
    elif dict['book'] == True:
        print "The eighth shelf has the oldest, muskiest books of all."; wait(x2)
        print "But...they're humming now...and glowing..."; wait(x2)
        print "You correctly figure they've lost thir magic. You ignore them."; wait(x2)
        book_choice()

def bar_check():
    if dict['bar'] == False:
        forward_door()
    elif dict['bar'] == True:
        forward_door2()
    else:
        print "bar_check broke"
        tower()

def forward_door():
    print "\nYou approach the door, with a heavy bar across it."; wait(x2)
    print "%s: 'This looks like the door you need to go through.'" % dict['mogget']; wait(x2)
    print "What will you do?"
    if dict['book'] == False and dict['lock'] == False:
        forward_1()
    elif dict['book'] == True and dict['lock'] == False:
        forward_2()
    elif dict['book'] == False and dict['lock'] == True:
        forward_3()
    elif dict['book'] == True and dict['lock'] == True:
        forward_4()
    else:
        print "forward_door broke"
        tower()

def forward_door2():
    print "\nYou approach the door, a pile of ash on the floor."; wait(x2)
    print "%s: 'This looks like the door you need to go through.'" % dict['mogget']; wait(x2)
    print "What will you do?"
    if dict['lock'] == False:
        forward_5()
    elif dict['lock'] == True:
        forward_6()
    else:
        print "forward_door broke"
        tower()

def forward_1():
    print "\n\t1. Try your super strength!"; wait(x2)
    print "\t2. Ask the door nicely to unlock."; wait(x2)
    print "\t3. Go back to the middle of the room."; wait(x1)
    door_attack = raw_input("> ")
    if door_attack == '1':
        print "\nYou think super strong thoughts...and push up the bar!!"; wait(x2)
        print "%s: 'Im sensing an anti-strength charm here.'" % dict['mogget']; wait(x2)
        print "Maybe something else will work."; wait(x2)
        bar_check()
    elif door_attack == '2':
        print "\nYou ask the door if it will please unlock."; wait(x2)
        print "'Sure Sweetie!' it says, as you jump back in surprise!"; wait(x2)
        print "'He's such an awful necromancer. He never talks to me anymore,' she says."; wait(x2)
        print "'Really, if you give somthing life, you have some responsibilities!'"; wait(x2)
        print "\nNow, you're still gonna need something to lift this bar."; wait(x2)
        print "'The Warlock always uses something explosive to remove it. Hope that helps!'"; wait(x2)
        print "You thank the door, a little dumbfounded, and go back to the middle of the room."; wait(x2)
        dict['lock'] = True
        tower()
    elif door_attack == '3':
        print "You go back to the centre of the room."; wait(x2)
        tower()
    else:
        print "%s: 'Seriously? This far along and you can't type a number?" % dict['mogget']; wait(x2)
        bar_check()

def forward_2():
    print "\n\t1. Try your fire powah!"; wait(x2)
    print "\t2. Ask the door nicely to unlock."; wait(x2)
    print "\t3. Go back to the middle of the room."; wait(x1)
    door_attack = raw_input("> ")
    if door_attack == '1':
        print "\nYou think about fire, focussing on the bar..."; wait(x2)
        print "It all burns away, crumbling to ash in seconds!!"; wait(x2)
        print "%s: 'Nice fire elementalising.'" % dict['mogget']; wait(x2)
        print "You try to open the door...It's still locked."; wait(x2)
        dict['bar'] = True
        bar_check()
    elif door_attack == '2':
        print "\nYou ask the door if it will please unlock."; wait(x2)
        print "'Sure Sweetie!' it says, as you jump back in surprise!"; wait(x2)
        print "'He's such an awful necromancer. He never talks to me anymore,' she says."; wait(x2)
        print "'Really, if you give somthing life, you have some responsibilities!'"; wait(x2)
        print "\nNow, you're still gonna need something to lift this bar."; wait(x2)
        print "'The Warlock always uses something explosive to remove it. Hope that helps!'"; wait(x2)
        print "You thank the door, a little dumbfounded, and go back to the middle of the room."; wait(x2)
        dict['lock'] = True
        tower()
    elif door_attack == '3':
        print "You go back to the centre of the room."; wait(x2)
        tower()
    else:
        print "%s: 'Seriously? This far along and you can't type a number?" % dict['mogget']; wait(x2)
        bar_check()

def forward_3():
    print "\n\t1. Try your super strength!"; wait(x2)
    print "\t2. Go back to the middle of the room."; wait(x1)
    door_attack = raw_input("> ")
    if door_attack == '1':
        print "\nYou think super strong thoughts...and push up the bar!!"; wait(x2)
        print "%s: 'Im sensing an anti-strength charm here.'" % dict['mogget']; wait(x2)
        print "Maybe something else will work. You go back to the middle of the room."; wait(x2)
        bar_check()
    elif door_attack == '2':
        print "You go back to the middle of the room."; wait(x2)
        tower()
    else:
        print "%s: 'Seriously? This far along and you can't type a number?" % dict['mogget']; wait(x2)
        bar_check()

def forward_4():
    print "\n\t1. Try your fire powah!"; wait(x2)
    print "\t2. Go back to the middle of the room."; wait(x1)
    door_attack = raw_input("> ")
    if door_attack == '1':
        print "\nYou think about fire, focussing on the bar..."; wait(x2)
        print "It all burns away, crumbling to ash in seconds!!"; wait(x2)
        print "%s: 'Nice fire elementalising.'" % dict['mogget']; wait(x2)
        dict['bar'] = True
        bar_check()
    elif door_attack == '2':
        print "You go back to the middle of the room."; wait(x2)
        tower()
    else:
        print "%s: 'Seriously? This far along and you can't type a number?" % dict['mogget']; wait(x2)
        bar_check()

def forward_5():
    print "\n\t1. Try to jimmy the lock!"; wait(x2)
    print "\t2. Ask the door nicely to unlock."; wait(x2)
    print "\t3. Go back to the middle of the room."; wait(x1)
    door_attack = raw_input("> ")
    if door_attack == '1':
        print "\nYou try to force the lock, but it doesn't come free."; wait(x2)
        print "You haven't got anything small enough to ft to jimmy it."; wait(x2)
        print "%s: 'There must be an easier way.'" % dict['mogget']; wait(x2)
        bar_check()
    elif door_attack == '2':
        print "\nYou ask the door if it will please unlock."; wait(x2)
        print "'Sure Sweetie!' it says, as you jump back in surprise!"; wait(x2)
        print "'He's such an awful necromancer. He never talks to me anymore,' she says."; wait(x2)
        print "'Really, if you give something life, you have some responsibilities!'"; wait(x2)
        print "You thank the door, a little dumbfounded, and go back to the middle of the room"; wait(x2)
        dict['lock'] = True
        tower()
    elif door_attack == '3':
        print "You go back to the centre of the room."; wait(x2)
        tower()
    else:
        print "%s: 'Seriously? This far along and you can't type a number?" % dict['mogget']; wait(x2)
        bar_check()

def forward_6():
    print "\n\t1. Go through the door."; wait(x2)
    print "\t2. Go back to the middle of the room."; wait(x1)
    door_attack = raw_input("> ")
    if door_attack == '1':
        print "\nYou go to turn the knob, ready to open the door."; wait(x2)
        print "%s: 'By my thinking, this is the last chance to go back.'" % dict['mogget']; wait(x2)
        print "Are you sure you're done here?"; wait(x1)
        print "\n\t1. Yep. You're ready."; wait(x1)
        print "\t2. Not yet. Go back to the middle of the room."; wait(x1)
        back = raw_input("> "); wait(x2)
        if back == '1':
            ascend()
        elif back == '2':
            print "You go back to the middle of the room."; wait(x2)
            tower()
        else:
            print "%s: 'Seriously? This far along and you can't type a number?" % dict['mogget']; wait(x2)
            bar_check()
    elif door_attack == '2':
        print "You go back to the middle of the room."; wait(x2)
        tower()
    else:
        print "%s: 'Seriously? This far along and you can't type a number?" % dict['mogget']; wait(x2)
        bar_check()

def ascend():
    print "\nYou pull open the door...it exposes a spiral staircase."; wait(x2)
    print "You take a deep breath before taking the first step."; wait(x2)
    print "But slowly you make your ascent."; wait(x2)
    print "\nYou reach a landing around half way up when you hear a muffled voice."; wait(x2)
    print "'...be long...prettiness...the world...'"; wait(x2)
    print "You tiptoe up several more stairs, and hear a clang of metal above."; wait(x2)
    print "'That was rather rude,' it's the voice from your bedroom, Zoblochk."; wait(x2)
    print "Zoblochk: 'Spitting is terrible bad manners...your lips are sealed for now'"; wait(x2)
    print "You take another step..."; wait(x1)
    print "\n'Oh. It's seems like we have company.'"; wait(x2)
    print "\nYour legs lock together, and you're dragged upwards towards the voice!"; wait(x2)
    print "You emerge from the stairs in a circular room at the top of the tower."; wait(x2)
    print "On the opposite side of the room, %s is trapped in a suspended cage!" % dict['lover']; wait(x2)
    print "In the middle of the room, Zoblochk stares directly at you, mist surrounding him."; wait(x2)
    print "Zoblochk: 'I've been expecting you...'"; wait(x2)
    print "The cloud swells into a whirlwind, the window panes begin to rattle!!"; wait(x2)
    print "\n'Enough of this crap.'"; wait(x2)
    print "\n%s stamps his paw on the floor as the whirlwind diappears, and your muscles are released." % dict['mogget']; wait(x2)
    print "Zoblochk now stands before you, a rather small, boyish creature."; wait(x2)
    print "%s: 'I have no time for spectacle.'" % dict['mogget']; wait(x2)
    print "Zoblochk: 'Well, I have no time to waste! The sun is almost at it's zenith!'"; wait(x2)
    knife_fight()

def knife_fight():
    print "\nZoblochk reaches for a large knife on a table, turning toward %s's cage!" % dict['lover']; wait(x2)
    print "It's time to act!"; wait(x1)
    print "\n\t1. Use your Super Strength!"; wait(x1)
    print "\t2. Use your Fire Powah!"; wait(x1)
    knife_choice = raw_input("> ")
    if knife_choice == '1':
        print "\nYou think fast thoughts, and rush to the table!"; wait(x2)
        print "Thinking strong thoughts, you flip the table, and the knife flys out a window!"; wait(x2)
        hand_knife()
    elif knife_choice == '2':
        print "\nYou think of fire, and focus on the table..."; wait(x2)
        print "The table burns up in a fiery ball of magic! The knife is just ash now!"; wait(x2)
        hand_knife()
    else:
        print "%s: 'No time to be an ass!'" % dict['mogget']; wait(x1)
        knife_fight()

def hand_knife():
    print "\nZoblochk: 'I underestimated you. But I have no need for a knife...'"; wait(x2)
    print "With no spectable, Zoblochk's arm turns into a 2 foot sword!"; wait(x2)
    print "Again, he turns to %s's cage..." % dict['lover']; wait(x2)
    print "Quick! make a choice!"; wait(x1)
    if dict['gun'] == True:
        gun_choice()
    elif dict['gun'] == False:
        print "\n\t1. There is no choice, get your sword and fight!"; wait(x1)
        raw_input("> "); wait(x1)
        sword_fight()
    else:
        print "hand_knife broke"
        hand_knife()

def gun_choice():
    print "\n\t1. Pull out your sword and fight!"; wait(x1)
    print "\t2. Pull out your blunderbuss and fight!"; wait(x1)
    gunnies = raw_input("> "); wait(x1)
    if gunnies == '1':
        sword_fight()
    elif gunnies == '2':
        gun_fight()
    else:
        print "%s: 'No time to be an ass!'" % dict['mogget']; wait(x1)
        gun_fight()

def gun_fight():
    print "You pull the not-so-antique blunderbuss from your shoulder..."; wait(x2)
    print "Feeling no guilt about bringing a gun to a knife fight, you take aim."; wait(x2)
    print "Just to rub in your superiority, you think firey thoughts as you squeeze the trigger."; wait(x2)
    print "A firey blast leaves the end of the gun, pushing you backwards, off your feet!"; wait(x2)
    print "You get to your feet as quickly as you can, the broken rifle in your hand."; wait(x2)
    print "As the smoke clear, you can see a melted stub where Zoblochk's arm used to me."; wait(x2)
    anger_fight()

def sword_fight():
    print "\nThere's no time to waste choosing, you pull the sword from yout belt."; wait(x2)
    print "You think fast thoughts, and run between Zoblochk and %s's cage." % dict['lover']; wait(x2)
    print "You're not practiced, what with the uslessness of swords, but you swing!"; wait(x2)
    print "You and Zoblochk exchange parries, he's not very practiced either!"; wait(x2)
    print "But your sword is heavy, and your arm is getting tired."; wait(x2)
    print "In a desparate attempt to get the upper hand, you think about fire!"; wait(x2)
    print "Your sword, now a flaming demonic blade, connects with Zoblochk's arm..."; wait(x2)
    print "Your swings follows through, and you see a melted stub where his arm used to me."; wait(x2)
    anger_fight()

def anger_fight():
    print "\nZoblochk's eyes fill with rage, as he sees the result of your attack!"; wait(x2)
    print "'AGGHHHHHH!!!!!' he screams! Albeit in a slightly comical boyish voice."; wait(x2)
    print "He then magically forces you back to the wall, pinning your amrs, very uncomically."; wait(x2)
    print "You see %s pinned to the floor as well, Zoblochk's rage fuelling extra power!" % dict['mogget']; wait(x2)
    print "Zoblochk says nothing, but his eyes have gone an evil red colour, as he closes his fist..."; wait(x2)
    print "Your throat begins to close up...you can still breathe, but only just!"; wait(x2)
    print "Quick! Say something!"; wait(x1)
    if dict['chaplin'] == True:
        chaplin_choice()
    elif dict['chaplin'] == False:
        print "\n\t1. Call for help!"; wait(x1)
        raw_input("> "); wait(x1)
        help_bear()
    else:
        print "anger_fight broke"
        anger_fight()

def chaplin_choice():
    print "\n\t1. Call for help!"; wait(x1)
    print "\t2. Call him Charlie Chaplin!"; wait(x1)
    helpee = raw_input("> "); wait(x1)
    if helpee == '1':
        help_bear()
    elif helpee == '2':
        chaplin_call()
    else:
        "%s 'mmmmm, mmmm mm mmm mmmmmm'"; wait(x2)
        chaplin_choice()

def help_bear():
    print "\nThere's nothing you can think of to say! You call for help!"; wait(x2)
    print "You must have picked up a teleport skill at some point..."
    print "\t...because as you call out, the bear appears behind Zoblochk!"; wait(x2)
    print "..."; wait(x2)
    print "Bear: 'GROWWWOOORRRRRRROOOOLLLLL'"; wait(x1)
    print "\nThe bear takes Zoblochk in his giant teeth, and lifts him from the ground!"; wait(x2)
    print "As you are released and fall to the floor, the bear trots to the window..."; wait(x2)
    print "Zoblochk, wailing like a child, can do nothing as the bear tosses him out!"; wait(x2)
    print "You hear Zoblochk's cries fade...until you hear nothing."; wait(x2)
    print "..."; wait(x1)
    print "The Bear looks at you expectantly."; wait(x2)
    print "You apologies, and teleport him to a land of milk and honey."; wait(x3)
    end()

def chaplin_call():
    print "\nYou squeeze out a sentence...you tell Zoblochk how much you like his hair cut."; wait(x2)
    print"'What did you say?!!' he screams, releasing his grip slightly."; wait(x2)
    print "You tell him you're a big fan of classic film, and his part reminds him of someone..."; wait(x2)
    print "Zoblochk: 'Wait, no...you couldn't know that...'"; wait(x2)
    print "You tell him it almost make him look like Charlie Chaplin!"; wait(x2)
    print "Zoblochk: 'Nooooooo! I do not look like him!!!'"; wait(x2)
    print "His release has all but released you from your hold..."; wait(x2)
    print "You tell him his mother must be so proud to have a Chaplin look-a-like."; wait(x2)
    print "Zoblochk continues to scream! It looks like you've finally broken him!"; wait(x2)
    print "Releasing his spell, he runs around in circles repeating 'No mum! Not him!'"; wait(x2)
    print "His screams turn to cries...Zoblochk: 'I can't take it anymore!'"; wait(x2)
    print "He runs to the window and jumps out of it!!"; wait(x2)
    print "You hear Zoblochk's cries fade...until you hear nothing."; wait(x2)
    print "..."; wait(x1)
    print "%s: 'Brutal.'" % dict['mogget']; wait(x3)
    end()

def end():
    print "\nYou rush to %s's cage and super strength the door open." % dict['lover']; wait(x2)
    print "%s: 'Gee Wizz, you cut it close! He was about to cut me up!'" % dict['lover']; wait(x2)
    print "You threaten to seal those pretty lips up again."; wait(x2)
    print "'Sorry, thank you for saving me' %s says, wary of your new powers." % dict['lover']; wait(x2)
    print "You tell %s that %s is really to thank." % (dict['lover'], dict['mogget']); wait(x2)
    print "%s: 'Who's %s?'" % (dict['lover'], dict['mogget']); wait(x2)
    print "You turn to where he...it was, but you can't see anything out of place."; wait(x2)
    print "With that, you're not sure what you meant by...whatever you called it..."; wait(x2)
    print "You hear a hum, and the room starts to glow..."; wait(x2)
    print "You crack a sarcastic smile...for some reason."; wait(x2)
    print "'Only because you insisted' says a faint, disembodied voice..."; wait(x2)
    print "You grab %s's hand as the two of you dissapear through a wormhole!" % dict['lover']; wait(x2)
    print "The spectacular journey takes just a few moments, but it feels like minutes!"; wait(x2)
    print "You and %s find yourselves sitting on your bed." % dict['lover']; wait(x2)
    print "The rest of you breakfast is...still warm."; wait(x2)
    print "This looks like the end...what will you do now?"; wait(x2)
    print "\n\t1. Make love for hours."; wait(x1)
    print "\t2. Eat the rest of your breakfast."; wait(x1)
    breakfast = raw_input("> "); wait(x1)
    if breakfast == '1':
        print "You turn to %s lovingly..." % dict['lover']; wait(x2)
        print "%s freezes, mid-way though wolfing down a rasher of bacon, looking guilty." % dict['lover']; wait(x2)
        print "You figure love-making can wait until after you cook some more."; wait(x2)
        print "As you go in for a cuddle, you swear you see a flash of white fur leaving the room..."; wait(x2)
        print "You fight the urge to give it a smack, and steal the last piece of bacon."; wait(x2)
    elif breakfast == '2':
        print "You turn to you plate, hungrily..."; wait(x2)
        print "%s freezes, mid-way though wolfing down a rasher of bacon, looking guilty." % dict['lover']; wait(x2)
        print "You figure breakfast and love-making can wait."; wait(x2)
        print "As you go in for a cuddle, you swear you see a flash of white fur leaving the room..."; wait(x2)
        print "You fight the urge to give it a smack, and steal the last piece of bacon."; wait(x3)
    else:
        print "A disembodied voice says 'You kidding me? Way to ruin the mood'"; wait(x2)
    print "\n\nThanks for playing Uber-Mega-Birthday-Adventure!"; wait(x2)
    print "\nHere are the credits."; wait(x1)
    print "\n\tEverything: Tim."; wait(x1)

    print "\nThat's the end. You have won some chocolate.\n"; wait(x1)
    print '\n'
    print """
    __________________,.............,
   /_/_/_/_/_/_/_/_/,-',  ,. -,-,--/|
  /_/_/_/_/_/_/_/,-' //  /-| / /--/ /
 /_/_/_/_/_/_/,-' `-''--'  `' '--/ /
/_/_/_/_/_/_,:................../ /
|________,'                     |/
         -----------------------'
"""
    wait(x3)
    print "\n"
    raw_input("Press enter to quit > ")
    quit()

speed()
