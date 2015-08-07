# munui
Simple python instant console dialog ui system (single line usage). No dependencies. Works on Windows and Linux.

## Motivation

I was trying to write simple scripts that need some simple bits of UI.
Although the simple bits of UI are possible in the console, a GUI form feels more usable and easier to hack.
In the past I've ended up mashing out a simple WinForms ui in C#, with all the weight that comes with it.
This just felt wrong, simple scripts should not be leaving the console. 
Most of my C# apps had console windows too because I needed the console feedback.

This project is creating those tiny bits of UI as simple console dialogues. Easy to code and pleasing to use.

## Features

 * Boxed message box [complete]
  - Basic boxes of text with word wrapping.
  - Th basic components to make the dialogues look nice.
  - Box art is also a strong visual indicator that the UI is not just spamming trace.
  - All dialogues will use this basic box art.
 * Multi select list [complete]
  - Supports single and multi select.
  - Take a list of strings as input.
  - Show the user the list and prompts them type the nubers to select items.
  - Returns an index or list of indexes for multiselect.
  - Optional confirm dialogue.
 
## Planned Featues

 * Colours
  - I'm hoping this will be easy, jsut add some codes.
  - Will be optional.

 * File selection
  - File selection might be more tolerable with a text interface.
  - Most GUI file selectors are an irritating waste of time.
  - Will be list menu + number based.
 * Yes-No Dialogue
  - This may be trivial to do manually but it will look nicer with box art.
  - Also this will deal with the tedium of invalid responses.
 
## License
GPL3
 
 
