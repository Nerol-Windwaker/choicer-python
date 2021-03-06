# Choicer - helps you choose what to do if you can't choose yourself.

It often happens that there is a list of activities, but you cannot choose what to do! And you spend hours thinking about what to do and what you will lose if you do something else. And so you start to get frustrated, and instead of finally making a choice, you suffer from this uncertainty for weeks. If you do this, then you and I are alike. And because of this, I created **Сhoicer**! **Сhoicer** makes a random selection from your choices. Now you don't have to spend hours to choose what you want to do!

The **Сhoicer** is supposed to be flexible so that you can easily change it for yourself.

### Installation and using

**Сhoicer** uses ```reprint``` and ```colorama``` to play animations in the console(if you don't need animation, just don't install).
```
pip install colorama
pip install reprint
```
To run **Сhoicer** use 
```
choicer.py
```

### If you want change something:

#### Console animation

To made own console animation, you need:
* In ```ui_console/animations``` create directory with your animation name
* In this directory create empty ```__init__.py```
* Also in this direcotry create ```start.py```. That your animation script
* In ```start.py``` write 
    ```def anim(all_lines,chosen_line):```
    ```all_lines``` - These are all choices.
    ```chosen_line``` - This is the choice that your animation will eventually show.
* And now you can write your own animation in this function
* To play animation in **Сhoicer**, open ```config.py```, and write in line
 ```anim_name = 'your animation name'```

#### Other
The functionality to easily add other elements will appear later. If you want to add something, write the code in the appropriate files. For example, if you want to change the function for calculating the random choice, modify ```random_choice.py```
Don't hold back, show your creativity!
