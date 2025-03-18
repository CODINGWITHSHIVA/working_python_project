from time import *
import random as r



def mistake(paratest,usertest):
    error=0
    for i in range(min(len(paratest),len(usertest))):  # change
        # try:
        if paratest[i] != usertest[i]:
            error=error+1
        # except:
    error += abs(len(paratest)-len(usertest))
    return error

def speed_time(time_start,time_end,userinput):
    time_taken=round(time_end - time_start,2)
    word_count =len(userinput.split()) # count word instead of the caracter
    speed= round(word_count/time_taken,2) if time_taken > 0 else 0
    return speed


test=[" a self-contained unit of writing that develops a single idea or topic through a series of related sentences, often indicated by an indent at the beginning.",
      "A paragraph typically consists of a topic sentence (introducing the main idea), supporting sentences (providing details and evidence), and a concluding sentence (summarizing the main point). ",
     "A good paragraph maintains unity by focusing on a single topic and coherence by ensuring that the sentences flow logically and relate to the main idea."]

test_text=r.choice(test)
print("\n\t******** typing speed *********\n")
print(test_text,"\n")
input("Press Enter when ready.....")

time_start=time()
user_input=input(" Enter : ")
time_end=time()


print("\nResults:")
print(f'Typing Speed : {speed_time(time_start,time_end,user_input)} W/Sec')
print(f"Typing Errors :{mistake(test_text,user_input)}")
print(f"Time Taken : {round(time_end - time_start,2)} sec")































