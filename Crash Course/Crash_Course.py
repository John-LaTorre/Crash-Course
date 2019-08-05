
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
def practice4_3():
    for value in range (1, 21):
        print(value);
def practice4_4():
    million = list(range(1, 1000001));
    print(million);
def practice4_5():
    million = list(range(1, 1000001));
    print(min(million));
    print(max(million));
    print(sum(million));
def practice4_6():
    odd_numbers = list(range(1, 21, 2));
    print(odd_numbers);
def practice4_7():
    triples = list(range(3, 30, 3));
    print(triples);
def practice4_8():
    for value in range(1,11):
        cube = value**3;
        print(cube);
def practice4_9():
    cubes = [value**3 for value in range(1,11)];
    print(cubes);
def practice4_10():
    animals = ['dog', 'cat', 'rabbit', 'fox', 'horse', 'raccoon', 'beaver', 'badger', 'wolf'];
    print("The first three items in the list are:");
    print(animals[:3]);
    print("Three items from the middle of the list are:");
    print(animals[3:6]);
    print("The last three items in the list are:");
    print(animals[-3:]);
def practice4_11():
     pizzas = ['pepperoni', 'extra cheese', 'meat lovers'];
     friends_pizzas = pizzas[:];
     pizzas.append('NY White');
     friends_pizzas.append('Hawaiian');
     print("My favorite pizzas are: ")
     for pizza in pizzas:
         print(pizza.title());
     print("\nMy friend's favorite pizzas are: ")
     for pizza in friends_pizzas:
         print(pizza.title());
def practice4_12():
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]
    my_foods.append('cannoli');
    friend_foods.append('ice cream');
    print("My favorite foods are: ");
    for food in my_foods:
        print(food);
    print("\nMy friend's favorite foods are: ");
    for food in friend_foods:
        print(food);
def practice4_13():
    buffet = ('pizza', 'fried chicken', 'steamed veggies', 'spaghetti', 'chocolate cake');
    for food in buffet:
        print(food);
    buffet = ('pizza', 'grilled chicken', 'steamed veggies', 'lasagna', 'chocolate cake');
    for food in buffet:
        print(food);

def practice5_1():
    game = 'Red Dead Redemption 2';
    print("Is RDR2 the best game ever? I predict True");
    print(game == 'Red Dead Redemption 2');

    print("Is Fortnite the best game ever? I predict False");
    print(game == 'Fortnite');

    food = 'Ice cream'
    print("I don't think ice cream is the best");
    print(food != 'Ice cream');
    answer = 42;
    print("The answer to life the universe and everything is 42");
    print(answer == 42);

def practice5_3():
    alien_color = 'green';
    if alien_color == 'green':
        print("You have earned 5 points!");
    if alien_color == 'yellow':
        print("You earn nothing.");
 
def practice5_4():
    color = 'green';
    if color == 'green':
        print("You got 5 points.");
    else: 
        print("You got 10 points.");

def practice5_5():
    color = 'yellow';
    if color == 'green':
        print("You got 5 points.");
    elif color == 'yellow': 
        print("You got 10 points.");
    else:
        print("You got 15 points");

def practice5_6():
    age = 16;
    if age <= 2:
        print("You are a baby");
    elif age < 4:
        print("You are a toddler");
    elif age < 13:
        print("You are a kid");
    elif age < 20:
        print("You are a teenager");
    elif age < 65:
        print("You are an adult");
    else:
        print("You are an elder");

def practice5_7():
    fruits = ['strawberries', 'raspberries', 'grapes'];
    if 'bananas' in fruits:
        print("You really like bananas!");
    if 'grapes' in fruits:
        print("You really like grapes!");
    if 'blueberries' in fruits:
        print("You really like blueberries.");
    if 'strawberries' in fruits:
        print("You really love strawberries!");
    if 'oranges' in fruits:
        print("You really like oranges!");

def practice5_8():
    usernames = ['elite_haxor420', 'susan095678', 'BigBillyBass1956', 'admin', 'jimmysmith123'];
    for user in usernames:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a status report?");
        else:
            print("Hello " + user + ", thank you for logging in again.");

def practice5_9():
    usernames = [];
    if usernames:
        for user in usernames:
            if user == 'admin':
                print("Hello " + user + ", would you like to see a status report?");
            else:
                print("Hello " + user + ", thank you for logging in again.");
    else:
        print("We need to find some users!");

def practice5_10():
    current_users = ['elite_haxor420', 'susan095678', 'BigBillyBass1956', 'admin', 'jimmysmith123'];
    new_users = ['SUSAN095678', 'Jimmysmith123', 'xxx_ArCaDiA317_xxx', 'BigSloppyTetons69', 'frankburman1975'];

    for user in new_users:
        if user.lower() in current_users:
            print("That name is taken. Please choose a different user name.");
        else:
            print("That name is available. Welcome aboard " + user + ".");

def practice5_11():
    numbers = list(range(1, 10));
    for number in numbers:
        if number == 1:
            print(str(number) + "st");
        elif number == 2:
            print(str(number) + "nd");
        elif number == 3:
            print(str(number) + "rd");
        else:
            print(str(number) + "th");

def practice6_1():
    governor = {'first': 'Roy', 'last': 'Cooper', 'age': 62, 'residence': 'Raleigh'};
    print("The Governor of North Carolina is " + governor['first'] + " " + governor['last'] + ". He is "
          + str(governor['age']) + " years old and lives in " + governor['residence'] + ".");
 
def practice6_2():
    favorite_numbers = {
        'John': 42,
        'Shannon': 20,
        'Ben': 420,
        'Leslie': 51,
        'Jeff': 2,
        }
    print(favorite_numbers);

def practice6_3():
    python_gloss = {
        'list': "Basically the python version of an array.",
        'dictionary': "Like an array but functions similar to a hash table.",
        'elif': "Stands for else-if, otherwise identical to Java.",
        'loop': "Instead of using an increment variable, Python skips that and says it in plain English -> for x in y.",
        'slice': "Python lets you take pieces of an array/list and work with them separately with this command.",
        }
    print("List: " + python_gloss['list']);
    print("Dictionary: " + python_gloss['dictionary']);
    print("Elif: " + python_gloss['elif']);
    print("Loop: " + python_gloss['loop']);
    print("Slice: " + python_gloss['slice']);

practice6_1();
practice6_2();
practice6_3();


    
