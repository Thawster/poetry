from random import randint

poem_1 = '''Once there was a tree….;
and she loved a little boy.;
And everyday the boy would come;
and he would gather her leaves;
and make them into crowns;
and play king of the forest.;
He would climb up her trunk;
and swing from her branches;
and eat apples.;
And they would play hide-and-go-seek.;
And when he was tired,;
he would sleep in her shade.;
And the boy loved the tree….;
very much.;
And the tree was happy.;
But time went by.;
And the boy grew older.;
And the tree was often alone.;
Then one day the boy came to the tree;
and the tree said, “Come, Boy, come and;
climb up my trunk and swing from my;
branches and eat apples and play in my;
shade and be happy.”;
“I am too big to climb and play” said the boy.;
“I want to buy things and have fun.;
I want some money?”;
“I’m sorry,” said the tree, “but I have no money.;
I have only leaves and apples.;
Take my apples, Boy, and sell them in the city.;
Then you will have money and you will be happy.”;
And so the boy climbed up the;
tree and gathered her apples;
and carried them away.;
And the tree was happy.;
But the boy stayed away for a long time….;
and the tree was sad.;
And then one day the boy came back;
and the tree shook with joy;
and she said, “Come, Boy, climb up my trunk;
and swing from my branches and be happy.”;
“I am too busy to climb trees,” said the boy.;
“I want a house to keep me warm,” he said.;
“I want a wife and I want children,;
and so I need a house.;
Can you give me a house?”;
” I have no house,” said the tree.;
“The forest is my house,;
but you may cut off;
my branches and build a;
house. Then you will be happy.”;
And so the boy cut off her branches;
and carried them away;
to build his house.;
And the tree was happy.;
But the boy stayed away for a long time.;
And when he came back,;
the tree was so happy;
she could hardly speak.;
“Come, Boy,” she whispered,;
“come and play.”;
“I am too old and sad to play,”;
said the boy.;
“I want a boat that will;
take me far away from here.;
Can you give me a boat?”;
“Cut down my trunk;
and make a boat,” said the tree.;
“Then you can sail away…;
and be happy.”;
And so the boy cut down her trunk;
and made a boat and sailed away.;
And the tree was happy;
… but not really.;
And after a long time;
the boy came back again.;
“I am sorry, Boy,”;
said the tree,” but I have nothing;
left to give you –;
My apples are gone.”;
“My teeth are too weak;
for apples,” said the boy.;
“My branches are gone,”;
said the tree. ” You;
cannot swing on them – ”;
“I am too old to swing;
on branches,” said the boy.;
“My trunk is gone, ” said the tree.;
“You cannot climb – ”;
“I am too tired to climb” said the boy.;
“I am sorry,” sighed the tree.;
“I wish that I could give you something….;
but I have nothing left.;
I am just an old stump.;
I am sorry….”;
“I don’t need very much now,” said the boy.;
“just a quiet place to sit and rest.;
I am very tired.”;
“Well,” said the tree, straightening;
herself up as much as she could,;
“well, an old stump is good for sitting and resting;
Come, Boy, sit down. Sit down and rest.”;
And the boy did.;
And the tree was happy.'''

poem_2 = '''There is a place where the sidewalk ends;
And before the street begins,;
And there the grass grows soft and white,;
And there the sun burns crimson bright,;
And there the moon-bird rests from his flight;
To cool in the peppermint wind.'''

poem_list_1 = poem_1.split(";")
poem_list_2 = poem_2.split(";")
#for line in poem_list:
  #print(line)
#poem_list.remove(poem_list[2])

def lines_printed_backwards(poem):
    num = 0
    while num < len(poem):
        print(poem[len(poem)-num-1])
        num += 1

def lines_printed_random(poem):
    random_lines=[]
    num_rand = []    
    
    count = 1
    while count <= len(poem):
        need = 1
        rand = randint(0, len(poem)-1)
        for num in num_rand:
            if rand == num:
                need += 0
            else:
                need += 1
        if need > len(num_rand):
            random_lines.append(poem[rand])
            count += 1
            num_rand.append(rand)
            #print(need)
            
    for line in random_lines:  
        print(line)
                


def combine_poems(poem1, poem2):
    both_poems = []
    for line in poem1:
        both_poems.append(line)
    for line in poem2:
        both_poems.append(line)
    lines_printed_random(both_poems)
    

def user_poem():
    poem_u = input("Type in your poem, end each line with a ';'. Leave blank for set poem")
    if poem_u == "":
        poem_list_u = poem_1
    else:
        poem_list_u = poem_u.split(";")

    correct = False
    while correct != True:
        choice = input('''Would you like to:
        1 - repeat it backwards
        2 - Randomize it
        3 - repeat it the same''')
        if choice == 1:
            lines_printed_backwards(poem_list_u)
            correct = True
        if choice == 2:
            lines_printed_random(poem_list_u)
            correct = True
        if choice == 3:
            for line in poem_list_u:
                print(line)
            correct = True


if __name__ == '__main__':
    #lines_printed_backwards(poem_list_2)
    #lines_printed_random(poem_list_1)
    #combine_poems(poem_list_1, poem_list_2)
    user_poem()