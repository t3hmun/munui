# munui
Simple python instant console ui system (single line usage). No dependencies. Works on Windows and Linux.

I was trying to write simple scripts that need some very simple bits of UI. 
In the past I've ended up mashing out a simple WinForms ui in C#, with all the weight that comes with it.
This just felt wrong, simple scripts should not be leaving the console. 
Most of my C# apps had console windows too because I needed the console feedback.

## Features

 * Boxed message box [complete]
  - A little bit of bax art makes it so much more enjyable to use.
  - Box art is also a strong visual indicator that the UI is not just spamming trace.
 * Multi select list [started]
  - I suppose I should start with a single select menu.
  - Take a list as input.
  - Get an index (list of indexes for multiselect) as output.
 
## Planned Featues

 * File selection
  - File selection would actually be much simple with a text interface.
  - Most file selectors are an irritating wate of time slowdown.
  - Arrow keys slow you down.
  - Will be list menu + number based.
 
 
 ## License
 GPL3
 
 
