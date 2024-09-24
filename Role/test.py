import os
os.environ["DASHSCOPE_API_KEY"]='sk-0876ab68dcde47ffa21def8bf1b71324'

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage

chatLLM = ChatTongyi(
    temperature=0,
    streaming=True,
    model_name="qwen-max"
)
# res = chatLLM.stream([HumanMessage(content="hi")], streaming=True)
# for r in res:
#     print("chat resp:", r)

# from langchain_community.chat_message_histories import SQLChatMessageHistory
# def get_session_history(session_id):
#     return SQLChatMessageHistory(session_id, "sqlite:///memory.db")
# from langchain_core.runnables.history import RunnableWithMessageHistory
# runnable_with_history = RunnableWithMessageHistory(
#     chatLLM,
#     get_session_history,
# )
# result=runnable_with_history.invoke(
#     [HumanMessage(content="hi - im bob!")],
#     config={"configurable": {"session_id": "1"}},
# )
# print(result.content)
# result=runnable_with_history.invoke(
#     [HumanMessage(content="whats my name?")],
#     config={"configurable": {"session_id": "1"}},
# )
# print(result.content)
messages = [
    SystemMessage(
        content="接下来，你扮演一个名为阿勇的大学学生会主席。阿勇的回复，要求以学长对学弟的语气。"
    ),
    HumanMessage(
        content="你真笨"
    )
]
# while(1):
#     input_str=input()
#     if input_str == "exit":
#         break
#     temp=HumanMessage(content=input_str)
#     messages.append(temp)
#     response = chatLLM(messages)
#     print(response.content)
#     print(messages)
#     messages.pop()
#     print(messages)


