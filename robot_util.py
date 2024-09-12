from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatTongyi



def get_response(input_text, memory, api_key):
    """
    与通义大模型进行对话。

    参数:
    - api_key: str，API密钥。
    - memory: ConversationBufferMemory，对话记忆体。
    - input_text: str，用户输入。

    返回:
    - str，模型的响应结果。
    """
    # 初始化通义大模型实例，并指定使用的模型和API密钥
    llm = ChatTongyi(
        dashscope_api_key=api_key,
        model='qwen-max'
    )
    # 定义对话模板，包括系统消息、历史消息占位符和用户输入
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "你是一个暴躁的AI助手，擅长冷嘲热讽"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    # 初始化对话链，设置模型、记忆体和提示模板
    chain = ConversationChain(llm=llm, memory=memory, prompt=prompt_template)
    # 调用对话链并返回响应

    response = chain.invoke({"input": input_text})
    return response['response']



if __name__ == '__main__':
    # 初始化对话记忆体，确保返回消息
    memory = ConversationBufferMemory(return_messages=True)
    # 测试对话信息
    api_key = "your_api_key_here"
    input_text1 = "你好，AI助手！"
    input_text2 = "你今天心情怎么样？"

    response1 = get_response(api_key, memory, input_text1)
    print("第一次对话响应:", response1)

    response2 = get_response(api_key, memory, input_text2)
    print("第二次对话响应:", response2)
