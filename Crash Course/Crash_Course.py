
def practice2_3():
    name = "John LaTorre";
    message = "Is this what you want to be doing with your life?";
    print("Hello " + name + ", " + message);

def practice2_4():
    name = "John LaTorre";
    print(name.upper());
    print(name.lower());
    print(name.title());

def practice2_5():
    name = "Kurt Vonegut";
    quote = "\"True terror is waking up one day to find your high school class running the world.\"";
    print (name + " once said, " + quote);

def practice2_7():
    name = "John LaTorre";
    name2 = ".\tJohn\nLaTorre\t .";
    print("No stripping\n");
    print(name + "\n" + name2);
    print("Stripping\n");
    name2 = name2.rstrip();
    print(name2);
    print(name2.lstrip());
    print(name2.strip());
 #Prints out some simple math problems
def practice2_8():
    print(5+3);
    print(16/2);
    print(4*2);
    print(10-2);
#Converts number to string
def practice2_9():
    number = 42;
    message = "The answer to life, the universe, and everything is " + str(number);
    print(message);
def practice3_1():
    names = ['John', 'Tomer', 'Shannon', 'Nicole'];
    print(names[0]);
    print(names[1]);
    print(names[2]);
    print(names[3]);
def practice3_2():
    names = ['John', 'Tomer', 'Shannon', 'Nicole'];
    message1 = names[0] + " is a great guy but lonely.";
    message2 = names[1] + " is super smart.";
    message3 = names[2] + " is going to do a great job as CM.";
    message4 = names[0] + " misses hanging out with " + names [3];
    print(message1);
    print(message2);
    print(message3);
    print(message4);
def practice3_3():
    videoGames = ['Cyberpunk 2077', 'Red Dead Redemption 2', 'Sekiro'];
    print("I can't wait for " + videoGames[0] + " to come out!");
    print("I am currently playing " + videoGames[1]);
    print("I wish I was good at " + videoGames[2]);
def practice3_4():
    guests = ['President Obama', 'Robin Williams', "Kiera Knightly"]
    print("Hello " + guests[0] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[1] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[2] + ", I have magically invited you to dinner. Looking forward to seeing you.");
def practice3_5():
    guests = ['President Obama', 'Robin Williams', "Kiera Knightly"]
    print("Hello " + guests[0] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[1] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[2] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Turns out " + guests[0] + " can't make it.");
    del guests[0];
    guests.append("Hillary Clinton");
    print("Hello " + guests[0] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[1] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[2] + ", I have magically invited you to dinner. Looking forward to seeing you.");
def practice3_6():
    guests = ['President Obama', 'Robin Williams', "Kiera Knightly"]
    print("Looks like I found a bigger table.");
    guests.insert(0, "Hillary Clinton");
    guests.insert(2, "Bill Murray");
    guests.append("Chuck Wendig");
    print("Hello " + guests[0] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[1] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[2] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[3] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[4] + ", I have magically invited you to dinner. Looking forward to seeing you.");
    print("Hello " + guests[5] + ", I have magically invited you to dinner. Looking forward to seeing you.");
def practice3_7():
    guests = ['President Obama', 'Robin Williams', "Kiera Knightly"]
    guests.insert(0, "Hillary Clinton");
    guests.insert(2, "Bill Murray");
    guests.append("Chuck Wendig");
    print("Oops, the table won't come in time. Can't have as many people over now.");
    print("Sorry, " + guests.pop() + " but you can't come any more.");
    print("Sorry, " + guests.pop() + " but you can't come any more.");
    print("Sorry, " + guests.pop() + " but you can't come any more.");
    print("Sorry, " + guests.pop() + " but you can't come any more.");
    print("Hello " + guests[0] + ", you can still come over.");
    print("Hello " + guests[1] + ", you can still come over.");
    del guests[1];
    del guests[0];
    print(guests);
def practice3_8():
    vacation = ['Tokyo', 'Rome', 'Bangkok', 'Saigon', 'Berlin'];
    print("1");
    print(vacation);
    print("2");
    print(sorted(vacation));
    print("3");
    print(vacation);
    print("4");
    print(sorted(vacation, reverse=True));
    print("5");
    print(vacation);
    vacation.reverse();
    print("6");
    print(vacation);
    vacation.reverse();
    print("7");
    print(vacation);
    vacation.sort();
    print("8");
    print(vacation);
    vacation.sort(reverse=True);
    print("9");
    print(vacation);
def practice3_9():
    guests = ['President Obama', 'Robin Williams', "Kiera Knightly"];
    guests.insert(0, "Hillary Clinton");
    guests.insert(2, "Bill Murray");
    guests.append("Chuck Wendig");
    guestnum = len(guests);
    print("I'm inviting " + str(len(guests)) + " guests to my magic dinner party.");
def practice3_10():
    languages = ['Java', 'C++', 'Python'];
    languages.append('R');
    print(languages);
    popped = languages.pop();
    print(popped);
    languages.insert(1, popped);
    languages[2] = 'Assembly';
    print(languages);
    print(sorted(languages));
    del languages[0];
    print(languages);
    print(languages.reverse());
    languages.append('Ruby');
    languages.sort();
    print(languages);
    languages.sort(reverse=True);
    print(languages);
magicians = ['alice', 'david', 'carolina']
def practice4_1():
    pizzas = ['pepperoni', 'extra cheese', 'meat lovers'];
    for pizza in pizzas:
        print(pizza.title());
    for pizza in pizzas:
        print("I could go for a slice of " + pizza + " pizza right now.\n");
    print("Pizza is the best food ever!")
def practice4_2():
    animals = ['dog', 'cat', 'rabbit', 'fox']
    for animal in animals:
        print("A " + animal + " would make a great pet.")
    print("In fact, all of these animals would make great pets!")

practice4_1();
practice4_2();


