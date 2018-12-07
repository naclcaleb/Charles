# Charles Experimental Project
Charles is already a cool project, but he's always getting better. This folder contains the project code for the next-generation Charles.

### New Features and Goals
The biggest part of this project, as of right now, is that Charles will be running on a generative model, rather than a selective one. 
**This means Charles will be making (or generating) his own responses to your requests.**

This project utilizes a Sequence-to-Sequence Neural Network to allow the creating of responses based on a user's query, along with a KnowledgeBase which will provide him with relevant facts - regular and ethical (outlined in the `knowledge.base` file).

This project is modular - one of the biggest reasons I decided to use Python again.

###### Note: This project uses Python 2.7 for compiling purposes - some of the tools used do not work with Python 3.x

Another important upgrade on this project is that Charles now uses a wake word for his activation. Saying "Hey Charles" causes him to light up (with the correct hardware) and begin listening for a request.

## Hardware
As for hardware, this project is the same as that of the original Charles project, but with an optional light connect to GPIO 18 on the Raspberry Pi for a light-up effect.

