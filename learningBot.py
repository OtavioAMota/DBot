from neuralintents import GenericAssistant


def learn_bot(arqName):
    chatbot = GenericAssistant(arqName)
    chatbot.train_model()
    chatbot.save_model()
    print("learn success")
