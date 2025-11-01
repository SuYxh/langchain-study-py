def joke_node(state: State):
    writer = get_stream_writer()
    writer({"node": ">>>> joke_node"})

    system_prompt = "你是一个笑话大师，根据用户的问题，写一个不超过100字的笑话。"
    prompts = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": state["messages"][0].content},
    ]

    response = llm.invoke(prompts)
    writer({"joke_result": response.content})
    return {"messages": [HumanMessage(content=response.content)], "type": "joke"}
