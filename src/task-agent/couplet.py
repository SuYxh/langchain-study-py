from langchain_redis import RedisConfig, RedisVectorStore
from langchain_community.embeddings import DashScopeEmbeddings

def couplet_node(state: State):
    writer = get_stream_writer()
    writer({"node": ">>>> couplet_node"})
    
    redis_url = "redis://localhost:6379"
    config = RedisConfig(index_name="couplet", redis_url=redis_url)
    vector_store = RedisVectorStore(embedding_model=DashScopeEmbeddings(), config=config)
    
    query = state["messages"][0].content
    samples = []
    scored_results = vector_store.similarity_search_with_score(query, k=10)
    for doc, score in scored_results:
        samples.append(doc.page_content)
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的对联大师，参考以下对联：\n{samples}\n请为用户问题生成下联。"),
        ("user", "{text}")
    ])
    
    prompt = prompt_template.invoke({"samples": samples, "text": query})
    response = llm.invoke(prompt)
    writer({"couplet_result": response.content})
    return {"messages": [HumanMessage(content=response.content)], "type": "couplet"}
