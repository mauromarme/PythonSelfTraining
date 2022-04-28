print('''

            .---------------------------------------------------------------------------.
           ( I AM A LITTLE LOST IN THE JUNGLE, PLEASE HELP ME GOING BACK TO THE SAVANNA  )
          //'---------------------------------------------------------------------------'
         /      , _.-~~-.__            __.,----.
      (';    __( )         ~~~'--..--~~         '.
(    . \"..-'  ')|                     .       \  '.
 \\. |\.'                    ;       .  ;       ;   ;
  \ \'"   /9)                 '       .  ;           ;
   ; )           )    (        '       .  ;     '    .
    )    _  __.-'-._   ;       '       . ,     /\    ;
    '-'"'--'      ; "-. '.    '            _.-(  ".  (
                  ;    \,)    )--,..----';'    >  ;   .
                   \   ( |   /           (    /   .   ;
     ,   ,          )  | ; .(      .    , )  /     \  ;
,;'-PjP;.';.-.;._,;/;,;)/;.;.);.;,,;,;,,;/;;,),;.,/,;.).,;,
''')
print("Welcome to 'Rescuing a Rhino'.")
print("Your mission is to help the Rhino going back to the Savanna") 

firstinput=input("The Rhino is in the middle of a unknown jungle, where do you like him to go? Left or Right? ")
firstinput=firstinput.lower()

if firstinput != "left":
  print("The Rhino has been attacked by a tiger. Game Over.") 
else:
  secondinput=input("There is an storm coming and you have reached a river, what would you like the Rhino does? Wait or Swim? ")
  secondinput=secondinput.lower()

if secondinput != "wait":
  print("The Rhino has been eaten by a monster coming from nowherer. You are a Looooser.")
else:
  thirdinput=input("The storm, made some trees fall into the river and the Rhino was able to use one of them to cross the river and now, he have reached a jail with three doors, a door with blue bars, a door with red bars and a door with yellow bars . Which door do you want the Rhino come into? Blue, Yellow or Red?")
  thirdinput=thirdinput.lower()

if thirdinput == "blue":
  print("The Rhino fall into a hole. You are an assasin. GAME OVER! (TRAGICALLY)")
elif thirdinput == "red":
  print("The Rhino get triped by a poisoning trap. GAME OVER! (TRAGICALLY)")
else:
  print("You Won!! The Rhino have reached the Savanna and is happy.")
  print('''
        ,       ,
      /|    |\./'.
     | |  ,  \|| ,|
     \  \_(\.-""\//.  _
   .-'`""``"` _   ` `-.`"""--.._      _..----. __
   | '~`      o\                `"---"        `. `"-.==,
    \,.-;    `"`                                |`""`===`
      (`            /                           |
       `-----.____.;          \     |           ;
                   \__         |    \          /
                  .'         .'      \        ' `,
                 /          /         '._        |
                 |    '.---;`-.____.-'`\ `""`;   |
                 |     _\   \    '.     )   /    \
                 \-,--( /   /    _/   .'   |_ _ .-)
              jgs '----;)__;    (`.-. ;    `-:.;-'
                                 `""""`

****************************************************************''')