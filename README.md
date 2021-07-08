# DFA-validator
This project is a DFA validator built with Python using Tkinter module to create its graphical user interface (GUI) for school project purposes.

The given regular expressions that this DFA validator will solve are the follwing: 
1. ( aa + bb ) ( a + b )* ( a + b + ab + ba ) ( a + b + ab + ba )* ( aa + bab )* ( a + b + aa ) ( a + b + bb +
aa )*
2. ( ( 101 + ( 111 )* + 100 ) + ( 1 + 0 + 11 )* ) ( 1 + 0 + 01 )* ( 111 + 000 + 101 ) ( 1 + 0 )*




**Tkinter Module** 

Tkinter is a standard library in Python which is used for GUI application. Tkinter actually comes along when we install Python. To import: 

```
import tkinter
```
or
```
from tkinter import *
```
   Read [here](https://docs.python.org/3/library/tkinter.html) for the tkinter documentation.


## What is Automata Theory
Automata Theory is a branch of computer science and math. It is the study of abstract machines and the computation problems that can be solved using these machines. Automata is the kind of machine which takes some string as input and this input goes through a finite number of states and may enter in the final state.

Regular Experssions are the language accepted by finite automata-- used to recognize patterns. It takes the string of symbol as input and changes its state accordingly. When the desired symbol is found, then the transition occurs. If the machine reads an input string one symbol at a time then it is a Deterministic Finite Automata (DFA). 

Read more [here.](https://www.javatpoint.com/automata-tutorial)



