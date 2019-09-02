
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

def practice6_4():
    python_gloss = {
        'list': "Basically the python version of an array.",
        'dictionary': "Like an array but functions similar to a hash table.",
        'elif': "Stands for else-if, otherwise identical to Java.",
        'loop': "Instead of using an increment variable, Python skips that and says it in plain English -> for x in y.",
        'slice': "Python lets you take pieces of an array/list and work with them separately with this command.",
        }
    for word, definition in python_gloss.items():
        print(word.title() + ": " + definition);

def practice6_5():
    rivers = {
        'nile': 'egypt',
        'amazon': 'brazil',
        'yellow': 'china'
        }
    for river, country in rivers.items():
        print("The " + river.title() + " River runs through " + country.title() + ".");
    for river in rivers.keys():
        print(river.title());
    for country in rivers.values():
        print(country.title());

def practice6_6():
    favorite_numbers = {
        'John': 42,
        'Shannon': 20,
        'Ben': 420,
        'Leslie': 51,
        'Jeff': 2,
        }
    poll_takers = ['Ben', 'John', 'Shannon', 'Leslie', 'Jeff', 'Susanne', 'Marissa', 'Aymeric'];
    poll_takers.sort();
    for name in poll_takers:
        if name in favorite_numbers.keys():
            print("Thanks for taking the poll, " + name.title() + "!");
        else:
            print("Hey, " + name.title() + "!" + " Please take the poll!");

def practice6_a():
    favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
        }
    for name, languages in favorite_languages.items():
        print("\n" + name.title() + "'s favorite languages are:");
        for language in languages:
            print("\t" + language.title());

def practice6_b():
    users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
            }
        }
    for username, user_info in users.items():
        print("\nUsername: " + username);
        full_name = user_info['first'] + " " + user_info['last'];
        location = user_info['location'];

        print("\tFull name: " + full_name.title());
        print("\tLocation: " + location.title());

def practice6_7():
    governor = {'first': 'Roy', 'last': 'Cooper', 'age': 62, 'residence': 'Raleigh'};
    senator = {'first': 'Thom', 'last': 'Tillis', 'age': 58, 'residence': 'Washington D.C'};
    president = {'first': 'Barack', 'last': 'Obama', 'age': 58, 'residence': 'Our Hearts'};

    politicians = [governor, senator, president];
    for politician in politicians:
        full_name = politician['first'] + " " + politician['last'];
        print("Name: " + full_name.title());
        print("Age: " + str(politician['age']));
        print("Residence: " + politician['residence'] + "\n");

def practice6_8():
    fluffy = {'owner': 'sarah', 'animal': 'bunny', 'name': 'fluffy'};
    tim = {'owner': 'frank', 'animal': 'cat', 'name': 'tim'};
    sir_barkington = {'owner': 'john', 'animal': 'dog', 'name': 'sir barkington'};

    pets = [fluffy, tim, sir_barkington];
    print("Pet Registry");
    for pet in pets:
        print("\nName: " + pet['name'].title());
        print("\tType: " + pet['animal'].title());
        print("\tOwner: " + pet['owner'].title());

def practice6_9():
    favorite_places = {
        'john': ['tokyo', 'raleigh', 'italy'],
        'shannon': ['wilmington', 'berlin', 'apex'],
        'leslie': ['atlanta', 'jamaica', 'wilmington'],
        }
    for person, places in favorite_places.items():
        print(person.title() + "'s favorite places:");
        for place in places:
            print('\t' + place.title());

def practice6_10():
    favorite_numbers = {
        'John': [42, 23, 90, 14],
        'Shannon': [20, 34, 75, 12],
        'Ben': [420, 4, 20, 24],
        'Leslie': [51, 65, 87, 25],
        'Jeff': [2, 6, 1, 9],
        }
    for person, numbers in favorite_numbers.items():
        print(person.title() + "'s favorite numbers:");
        for number in numbers:
            print('\t' + str(number));

def practice6_11():
    cities = {
        'tokyo': {'country': 'japan', 'population': 12000000, 'fact': 'the best city in the world.'},
        'raleigh': {'country': 'america', 'population': 350000, 'fact': 'the state capital of NC.'},
        'saigon': {'country': 'vietnam', 'population': 8400000, 'fact': 'officially named Ho Chi Min but no one calls it that.'}
        }
    print("John's Travel Notebook");
    for city, information in cities.items():
        where = information['country'];
        pop = information['population'];
        factoid = information['fact'];
        print(city.title() + " is a city in " + where.title() + " with a general population of " + str(pop));
        print("It is a fact that " + city.title() + " is " + factoid + "\n");

def practice7_a():
    height = input("How tall are you, in inches? ");
    height = int(height);

    if height >= 36:
        print("\nYou're tall enough to ride!");
    else:
        print("\nYou'll be able to ride when you're a little older.");

def practice7_b():
    number = input("Enter a number, and I'll tell you if it's even or odd: ");
    number = int(number);

    if number % 2 == 0:
        print("\nThe number " + str(number) + " is even.");
    else:
        print("\nThe number " + str(number) + " is odd.");

def practice7_1():
    car = input("What kind of car would you like to rent? ");
    print("Let me see if I can find you a " + car.title());

def practice7_2():
    party = input("How many people are in your party? ");
    party = int(party);

    if party > 8:
        print("I'm sorry you'll have to wait a bit for a table to be available.");
    else:
        print("Let me show you to your table.");

def practice7_3():
    number = input("Please provide a number: ");
    number = int(number);

    if number % 10 == 0:
        print(str(number) + " is a multiple of ten.");
    else:
        print(str(number) + " is not a multiple of ten.");

def practice7_c():
    prompt = "\nTell me something and I'll repeat it back to you: ";
    prompt += "\nEnter 'quit' to end the program. ";

    message = " ";
    active = True;

    while active:
        message = input(prompt);

        if message == 'quit':
            active = False;
        else:
            print(message);

def practice7_d():
    prompt = "\nPlease enter the name of a city that you have visited: ";
    prompt += "\n(Enter 'quit' when you are finished.) ";

    while True:
        city = input(prompt);

        if city == 'quit':
            break;
        else:
            print("I'd love to go to " + city.title() + "!");

def practice7_4():
    prompt = "Enter the pizza toppings you want: ";
    prompt += "\n(Enter 'quit' to finish) ";

    topping = " ";

    while topping != 'quit':
        topping = input(prompt);
        if topping != 'quit':
            print("We'll add " + topping + " to your pizza.");

def practice7_5():
    prompt1 = "How many tickets do you want? ";
    party = input(prompt1);
    party = int(party);

    asks = 1;
    prompt2 = "How old are you? ";

    while asks <= party:
        age = input(prompt2);
        age = int(age);
        asks += 1;

        if age < 3:
            print("Your ticket is free.");
        elif age <= 12:
            print("Your ticket is $10.");
        else:
            print("Your ticket is $15");

def practice7_e():
    unconfirmed_users = ['alice', 'brian', 'candace'];
    confirmed_users = [];

    while unconfirmed_users:
        current_user = unconfirmed_users.pop();
        print("Verifying user: " + current_user.title());
        confirmed_users.append(current_user);

    print("\nThe following users have been confirmed: ");
    for user in confirmed_users:
        print(user.title());

def practice7_f():
    responses = {};
    # Set flag to indicate polling active
    polling_active = True;

    while polling_active:
        #Ask for user's name and response
        name = input("\nWhat is your name? ");
        response = input("Which mountain would you like to climb someday? ");

        # Store response in dictionary
        responses[name] = response;

        # Find out if anyone else wants to take the poll
        repeat = input("Would you like to let someone else respond? (yes/no) ");
        if repeat == 'no':
            polling_active = False;
    # Polling complete. Show the results
    print("\n--- Poll Results ---");
    for name, response in responses.items():
        print(name + " would like to climb " + response + "."); 

def practice7_8():
    sandwich_orders = ['blt', 'ham and cheese', 'turkey club', 'grilled cheese'];
    made_sandwiches = [];

    while sandwich_orders:
        current_order = sandwich_orders.pop();
        print("One " + current_order + " sandwich ready. Order up!");
        made_sandwiches.append(current_order);
    print("\n--- Sandwiches made ---");
    for sandwich in made_sandwiches:
        print(sandwich.upper());

def practice7_9():
    sandwich_orders = ['pastrami', 'ham and cheese', 'pastrami', 'grilled cheese', 'turkey club', 'pastrami'];
    made_sandwiches = [];

    print("We apologize but the deli has run out of pastrami.");
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami');

    while sandwich_orders:
        current_order = sandwich_orders.pop();
        print("One " + current_order + " sandwich ready. Order up!");
        made_sandwiches.append(current_order);
    print("\n--- Sandwiches made ---");
    for sandwich in made_sandwiches:
        print(sandwich.upper());

def practice7_10():
    vacations = {};

    poll_active = True;

    while poll_active:
        name = input("\nWhat is your name? ");
        location = input("If you could visit one place in the world, where would you go? ");

        vacations[name] = location;
        repeat = input("Is there someone else waiting to take the poll? (yes/no) ");

        if repeat == 'no':
            poll_active = False;

    print("\n--- Poll Results ---");
    for name, location in vacations.items():
        print(name + " wants to visit " + location.title() + " more than anywhere else in the world.");

def practice8_1():
    print("This chapter deals with functions which is something I figured out awhile ago.");
    print("This bit is just to practice the absolute simplest form of a function.")

def practice8_2(title):
    print("Our first function that takes a parameter!");
    print("One of my favorite books is " + title.title() + ".");

# practice8_3
def make_shirt(size, message):
    print("Ok, we'll make you a " + size + " sized shirt with '" + message + "' printed on it.");

# practice8_4
# Change previous function to have default values
def make_shirt(message = 'I love Python', size = 'large'):
    print("Ok, we'll make you a " + size + " sized shirt with '" + message + "' printed on it.");

#practice8_5
def cities(city, country = 'The United States'):
    print(city.title() + " is in " + country.title());

# practice8_a
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name;
    else:
        full_name = first_name + ' ' + last_name;
    return full_name.title();

# practice8_b
def build_person(first_name, last_name, age = ''):
    person = {'first': first_name, 'last': last_name};
    if age:
        person['age'] = age;
    return person;

def practice8_c():
    while True:
        print("\nPlease tell me your name: ");
        print("(enter 'q' at any time to quit) ");

        f_name = input("First name: ");
        if f_name == 'q':
            break;
        l_name = input("Last name: ");
        if l_name == 'q':
            break;

        formatted_name = get_formatted_name(f_name, l_name);
        print("\nHello, " + formatted_name + "!");

# practice8_6
def city_country(city, country):
    the_city = city.title();
    the_country = country.title();
    result = the_city + ", " + the_country;
    return result;

def practice8_6():
    print(city_country('tokyo', 'japan'));
    print(city_country('raleigh', 'north carolina'));
    print(city_country('bangkok', 'thailand'));

# practice8_7
def make_album(artist, title, tracks = ''):
    album = {'band': artist, 'release': title};
    if tracks:
        album['songs'] = tracks;
    return album;

def practice8_7():
    kpop = make_album('twice', 'what is love?');
    rap = make_album('childish gambino', 'camp');
    electro = make_album('sia', 'this is acting');
    alternative = make_album('nirvana', 'unplugged in new york', 14);
    print(kpop);
    print(rap);
    print(electro);
    print(alternative);

def practice8_8():
    while True:
        print("\nPlease tell me your favorite album: ");
        print("(enter 'q' at any time to quit) ");

        artist_name = input("Artist name: ");
        if artist_name == 'q':
            break;
        album_name = input("Album title: ");
        if album_name == 'q':
            break;
        the_album = make_album(artist_name, album_name);
        print(the_album);

# practice8_c
#def print_models(unprinted_designs, complete_models):
#    while unprinted_designs:
#        current_design = unprinted_designs.pop();
#        print("Printing model: " + current_design);
#        completed_models.append(current_design);

#def show_completed_models(completed_models):
#    print("\nThe following models have been printed: ");
#    for completed_model in completed_models:
#        print(completed_model);
#unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'];
#completed_models = [];
#print_models(unprinted_designs[:], completed_models);
#show_completed_models(completed_models);
#print(unprinted_designs);

#practice8_9
magicians = ['frank', 'mysterio', 'balthazar'];
def show_magicians(magi):
    for mage in magi:
        print(mage.title());
#show_magicians(magicians);

#practice8_10&11
def make_great(magicians):
    new = [];
    while magicians:
        new_magician = magicians.pop();
        new_magician += ' the Great';
        new.append(new_magician);
    return new;
great_magicians = make_great(magicians[:]);
#show_magicians(great_magicians);
#show_magicians(magicians);

# practice8_12
def make_sandwich(*ingredients):
    print("\nMaking a sandwhich with the following ingredients: ");
    for ingredient in ingredients:
        print("- " + ingredient);
#make_sandwich('peanut butter', 'grape jelly');
#make_sandwich('bacon', 'lettuce', 'tomato');
#make_sandwich('steak', 'cheese', 'onions', 'peppers');

#practice8_13
def build_profile(first, last, **user_info):
    profile = {};
    profile['first_name'] = first;
    profile['last_name'] = last;
    for key, value in user_info.items():
        profile[key] = value;
    return profile;

me = build_profile('John', 'LaTorre', location='North Carolina', marital_status='Single', employed=False);
#print(me);
#practice8_14
def make_car(maker, model, **info):
    car = {};
    car['manufacturer'] = maker;
    car['model'] = model;
    for key, value in info.items():
        car[key] = value;
    return car;
my_car = make_car('mazda', '3', color = 'red', doors = 4);
#print(my_car);
#practice 8_d
from pizza import make_pizza as mp
#mp(16, 'pepperoni');
#mp(12, 'mushrooms', 'green peppers', 'extra cheese');

#practice8_15
import printing_functions as pf
#unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'];
#completed_models = [];
#pf.print_models(unprinted_designs[:], completed_models);
#pf.show_completed_models(completed_models);
#print(unprinted_designs);

#practice8_16
import practice_8_16
#print("import module name")
#practice_8_16.purpose();
#from practice_8_16 import purpose
#print("from module name import function")
#purpose();
from practice_8_16 import purpose as p
#print("from module name import function as fn")
#p();
import practice_8_16 as p816
#print("import module name as mn")
#p816.purpose();
from practice_8_16 import *
#print("from module name import *")
#purpose();

#practice9_a
class Dog():
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
    def sit(self):
        print(self.name.title() + " is now sitting.");
    def roll_over(self):
        print(self.name.title() + " rolled over!");

my_dog = Dog('annabelle', 12);
your_dog = Dog('fido', 5);
#print("My dog's name is " + my_dog.name.title() + ".");
#print("My dog is " + str(my_dog.age) + ".");
#print("Your dog's name is " + your_dog.name.title() + ".");
#print("Your dog is " + str(your_dog.age) + ".");
#my_dog.sit();
#my_dog.roll_over();
#your_dog.sit();
#your_dog.roll_over();

#practice9_1
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name;
        self.cuisine = cuisine;
        self.number_served = 0;
    def describe_restaurant(self):
        print(self.name.title() + " is a " + self.cuisine.title() + " restaurant.");
    def open_restaurant(self):
        print(self.name.title() + " is now open for business!");
    def served(self):
        print(self.name.title() + " has served " + str(self.number_served) + " customers.");
    def set_number_served(self, customers):
        self.number_served = customers;
    def increment_number_served(self, customers):
        self.number_served += customers;


restaurant1 = Restaurant("cuchinos", 'italian');
#print(restaurant1.name.title());
#print(restaurant1.cuisine.title());
#restaurant1.describe_restaurant();
#restaurant1.open_restaurant();

#practice9_2
french = Restaurant("chez pierre", 'french');
chinese = Restaurant("double happiness", 'chinese');
fast_food = Restaurant("bojangles", 'chicken');
#french.describe_restaurant();
#chinese.describe_restaurant();
#fast_food.describe_restaurant();

#practice9_3
class User():
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name;
        self.last_name = last_name;
        self.age = age;
        self.hobby = hobby;
        self.login_attempts = 0;

    def user_description(self):
        print("User: " + self.first_name.title() + " " + self.last_name.title());
        print("Age: " + str(self.age));
        print("Hobby: " + self.hobby.title());

    def greet_user(self):
        print("Hello " + self.first_name.title() + "!");
        print("Have you had time for " + self.hobby + " lately?\n");

    def increment_login_attempts(self):
        self.login_attempts += 1;
        
    def reset_login_attempts(self):
        self.login_attempts = 0;

john = User('john', 'latorre', 36, 'video games');
#john.user_description();
#john.greet_user();

shannon = User('shannon', 'schaible', 25, 'politics');
#shannon.user_description();
#shannon.greet_user();

leslie = User('leslie', 'cohen', 56, 'painting');
#leslie.user_description();
#leslie.greet_user();

#practice9_b
class Car():
    def __init__(self, make, model, year):
        self.make = make;
        self.model = model;
        self.year = year;
        self.odometer_reading = 0;

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model;
        return long_name.title();

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.");

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage;
        else:
            print("You can't roll back an odometer!");

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles;
        else:
            print("You can't roll back an odometer!");

my_new_car = Car('mazda', '3', '2015');
#print(my_new_car.get_descriptive_name());
#my_new_car.update_odometer(23);
#my_new_car.read_odometer();
#my_new_car.update_odometer(15);

my_used_car = Car('subaru', 'outback', 2013);
#print(my_used_car.get_descriptive_name());
#my_used_car.update_odometer(23500);
#my_used_car.read_odometer();
#my_used_car.increment_odometer(100);
#my_used_car.read_odometer();

#practice9_4 (see 9_1)
burgers = Restaurant('mcdonalds', 'hamburger');
#burgers.served();
#burgers.number_served = 500;
#burgers.served();
#burgers.set_number_served(1000);
#burgers.served();
#burgers.increment_number_served(2500);
#burgers.served();

#practice9_5 (see 9_3)
hacker = User('hacker', 'mchackerton', 14, 'haxor');
#login = 0;
#while login < 5:
#    hacker.increment_login_attempts();
#    login += 1;
#print(str(hacker.login_attempts));
#hacker.reset_login_attempts();
#print(str(hacker.login_attempts));

#practice9_c
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size;
     
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.");

    def get_range(self):
        if self.battery_size == 70:
            range = 240;
        elif self.battery_size == 85:
            range = 270;
        message = "This car can go approximately " + str(range);
        message += " miles on a full charge.";
        print(message);

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85;

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year);
        self.battery = Battery();

my_tesla = ElectricCar('tesla', 'model s', 2016);
#print(my_tesla.get_descriptive_name());
#my_tesla.battery.describe_battery();
#my_tesla.battery.get_range();

#practice9_6
class IceCreamStand(Restaurant):
    def __init__(self, name, *flavors, cuisine= 'ice cream'):
        super().__init__(name, cuisine);
        self.flavors = flavors;
    def give_flavors(self):
        print("Available Flavors:");
        for flavor in self.flavors:
            print("- " + flavor);

#simple_shop = IceCreamStand("simple shop", 'chocolate', 'vanilla', 'strawberry');
#simple_shop.describe_restaurant();
#simple_shop.give_flavors();

#practice9_8

class Privileges():
    def __init__(self, *privileges):
        self.privileges = privileges;
    def show_privileges(self):
        for privilege in self.privileges:
            print("- " + privilege);

#practice9_7

class Admin(User):
    def __init__(self, first_name, last_name, age, hobby):
        super().__init__(first_name, last_name, age, hobby);
        self.privileges = Privileges("can add post", "can delete post", "can ban user");
        
admin1 = Admin("john", "latorre", 36, "video games");
#admin1.privileges.show_privileges();

#practice9_9

my_2nd_car = ElectricCar("nissan", "leaf", 2006);
my_2nd_car.battery.get_range();
my_2nd_car.battery.upgrade_battery();
my_2nd_car.battery.get_range();
