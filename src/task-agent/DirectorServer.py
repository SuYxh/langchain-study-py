import random
from Director import graph
import gradio as gr

def process_input(query):
    config = {"configurable": {"thread_id": str(random.randint(1, 10000))}}
    res = graph.invoke({"messages": [query]}, config, stream_mode="values")
    return res["messages"][-1].content

with gr.Blocks() as demo:
    gr.Markdown("# LangGraph Multi-Agent")
    with gr.Row():
        with gr.Column():
            inputs_text = gr.Textbox(label="问题", placeholder="请输入你的问题", value="讲一个郭德纲的笑话")
            btn_start = gr.Button("Start", variant="primary")
        with gr.Column():
            output_text = gr.Textbox(label="Output")
    
    btn_start.click(process_input, inputs=[inputs_text], outputs=[output_text])

demo.launch()
