# NLP In Video Games

This repository contains the implementation of NLP In Video games created in order to test its functionality.

The repository contains the following:
- Test Game
- Joint Model for intent classification and slots filling
- Question Answering model used to answer questions
- Sound recognition model to recognize the audio from a local microphone

## Test Game

The test game is a simple simulation in which several locations and contextual knowledge were created. Those locations are used in order to test the NLP models.
The game contains a simple chat system used to communicate with the BOT using Natural Language, either in form of text or voice commands.
In order to run the game **Unreal Engine 4.27** is required. The game can run either from the engine itself or can be built to test it.

## Installation guide
1. Run the Joint Model – this can be done by going to the directory called JointModel and 
running inference.py main. It will start a flask server on port 5000. Only first time, it will download the 
30 pretrained models. If another training is required, then run train_joint_model.py which 
will start the training process.
2. Run the Question Answering Model – this can be done by going to the directory called 
QuestionAnswering and running answer_question.py main. It will start a flask server on 
port 5001. No training is required. The context can be changed from within 
answer_question.py file, the global variable called CONTEXT. Another way of 
changing the context is through a HTTP Post call on /context endpoint.
2. Run the SpeechRecognition Model – this can be done by going to the directory called 
SpeechRecognition and running inference.py main. It will start a flask server on 
port 5002. 
3. Open the project game using Unreal Engine 4, version 4.27. The game can be either ran 
from withing the engine or can be built and ran from outside. 
4. When running the game:
 (a) Either give commands as text by pressing ENTER to insert data into the game chat and ask the bot agent
for things.
 (b) Either give audio commands by pressing CTRL + R then speak in your microphone. After pressing, until a pause in user voice is detected it will stop and request command from the bot.
5. The game will call the localhost on port 5000 to run the Joint Model and wait for a 
response, so the flask server must be up and running.




## Joint Model

Joint model is a model which, from a given text, finds out what the intent of the user is and what the slots in the input text are.

For more information about the Joint Model see `JointModel` directory.

## Question Answering

Question Answering is a model which answers to the given question sent as a text.

For more information about the Question Answering Model see `QuestionAnswering` directory.


## Examples

Check the Presentation folder for demo movies and a high-level documentation.

## References

- [Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", October 2018](https://arxiv.org/pdf/1810.04805v2.pdf)
- [Qian Chen, Zhu Zhuo, Wen Wang, "BERT for Joint Intent Classification and Slot Filling",  February 2019](https://arxiv.org/pdf/1902.10909.pdf)
- [OpenAI Team, "Language Models are Few-Shot Learners", May 2020](https://arxiv.org/pdf/2005.14165.pdf) 
- ["joint-intent-classification-and-slot-filling-based-on-BERT"](https://github.com/90217/joint-intent-classification-and-slot-filling-based-on-BERT)
- [Moscow Institute of Physics and Technology (MIPT), "DeepPavlov"](https://github.com/deepmipt/DeepPavlov) 
- CMU Sphinx model, https://cmusphinx.github.io/wiki/about/,  https://github.com/Uberi/speech_recognition
