import gradio as gr
import aitextgen


def ai_text(inp):
  generated_text = ai.generate_one(max_length = 2500, prompt = inp, no_repeat_ngram_size = 3)
  return generated_text

# here it will download all the datasets needed, this is painfully slow its why i recommend using as commandline

print("downloading dataset if your internet bad this will take... yes minutes?!?!?")

ai = aitextgen(model="EleutherAI/gpt-neo-125M",to_gpu=True)

print("All Downloaded Finially...")

# ai_text("hard coded input for CLI not using web") 
# print(type(generated_text) # uncomment this for cli output

print(" ") # spacing because I hate walls of text
print("Bellow should be the link to your tempoary Gradio")
print(" ")

output_text = gr.outputs.Textbox()
gr.Interface(ai_text,"textbox", output_text, title="Viking couldnt be arsed",
             description="bot for when sample writting is needed and your lazy").launch()
# this should output link to the Gradio tempoary website url... if it dosnt meh
