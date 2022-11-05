## I'ts Lunch Time!

Have you ever looked over at someone's pizza and discovered that they put **pineapple** on it? Pineaple never has, and never will, belong on pizza. Pineapple is **only a fruit**. Nevertheless, people continue to put pineapple on pizza. This game was created to tell people that pineapple should never come within 10m of a pizza.

## Running the Game

This game was created in PyCharm, so if you use PyCharm as well, it should work perfectly. Make sure to download ALL THE FILES (except this README, that's optional) and run the game as you normally would a script in PyCharm.

If you don't have PyCharm, get PyCharm. It is a great IDE with so many inbuilt features like code snippets, intuitive error handling, and if you want to download a package, just search it up within PyCharm and download it with just one click. If you do not want to download PyCharm, download all files except the venv (virtual environment) and make sure you have at least Python 3.6 (which you can download [here](https://www.python.org/downloads/)) along with PyGame 2.0.0 installed, which you can do using

```zsh
pip install pygame
```

at the command line.

## Gameplay

### Playing the Game

After pressing play, your character will appear in the middle of the screen. The default controls are below:

 ```
 W: Move Up
 S: Move Down
 A: Move Left
 D: Move Right
 
 O: Increase Player Size + Speed
 P: Decrease Player Size + Speed
 ```
 
 There are 3 categories of obstacles, and 5 individual obstacles.
 
  - Good
    - Cheese
    - Chilli
  - Bad
    - Pineapple
    - Chocolate 
  - Power-Up
    - x2 Score Booster
    
Obstacles will enter from the right hand side and exit from the left. But be aware, after a certain score, obstacles come in from both directions! Hitting a good obstacle will increase your score by 1, while hitting a bad obstacle will end the game. However, if you hit a power-up (which has a 1/100 chance of appearing in place of a good/bad obstacle), you will get a boost for a small period of time- make the most of it!

So far, there is only 1 power-up: the x2 Score Booster. When you hit it, all the points you get while the boost is active will be multiplied by 2. You can see the duration left on the boost in the bottom left-hand corner of the screen.

### Shop

In the shop, you can buy three things: backgrounds, skins, and shields. Skins are what your player looks like while you are playing the game. Backgrounds are, well, backgrounds, but you can only upgrade them. If you choose to buy the next background, you cannot go back to your previous background. Shields are another power-up, but shields cannot be obtained in normal gameplay. You can buy a shield, and if you hit an obstacle while you have 1 or more shields, the game will not end, and you will instead lose a shield.

## Designs

I am not a graphic designer, so I apologize if the game does not look that great. All of the images for obstacles have been downloaded from Google Images. This game is not going to be used for any commercial purposes.

## Thank you!

This game was the first medium-sized project that I made in Python, and I would appreciate it if you gave me some advice! Thank you so much if you decided to try my game out!
