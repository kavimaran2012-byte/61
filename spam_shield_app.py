"""
Spam Shield web page (Gradio). Step 8 of the activity.
Leep this file in the same folder as spam_shield.py.
Run: python spam_shield_app.py then open http://127.0.0.1:7860
Do not use launch(share =True): it makes a public link to your computor.
"""
import  gradio as gr
from spam_shield import THRESHOLD, classify, explain, spam_score



def check(messages):

    flagged = ", ".join(explain(messages))
    return classify(messages), spam_score(message), flagged


demo = gr.Interface(
    fn=check,
    inputs=gr.Textbox(lines=3, label="Paste a message"),
    outputs=[
        gr.Textbox(label="Verdict"),
        gr.Number(label="Spam score"),
        gr.Textbox(label="Words that raised the score"),
    ],
    title="Spam Shield",
    description="Every spam word adds points. A score of %d or more means SPAM" % THRESHOLD,
    examples=[
        ["Congratulations! You WON a FREE IPHONE. Click now to claim"],
        ["Hey, are we still meeting at 5?"],
        ["Click the link in the class group to join the free quiz now"],
    ],
)

if __name__ == "__main__":
    demo.launch()