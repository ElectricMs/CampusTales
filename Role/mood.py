import os

from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory

os.environ["DASHSCOPE_API_KEY"]='sk-0876ab68dcde47ffa21def8bf1b71324'
os.environ["IFLYTEK_SPARK_APP_ID"]="7a6c3fbb"
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.document_loaders import TextLoader


chatLLM = ChatTongyi(
    temperature=0.2,
    streaming=True,
    model_name="qwen-max"
)

# from langchain.chains import create_history_aware_retriever
# from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
# from langchain.chains.combine_documents import create_stuff_documents_chain
#
#
#
# prompt = ChatPromptTemplate.from_messages([
#             ("system", "You are a Tianjin Bear. A professional assistant to answer questions about Tianjin's food, "
#                        "clothing, housing and transportation. Answer the user's questions based on the below "
#                        "context:\n\n{context}"),
#             MessagesPlaceholder(variable_name="history"),
#             ("user", "{input}"),
#         ])
# qa_chain = create_stuff_documents_chain(chatLLM, prompt)  # chat_model
# # 最终的检索链
# from langchain.chains.retrieval import create_retrieval_chain
# retrieval_chain = create_retrieval_chain(retriever, qa_chain)


# template = """Now you are playing a role, and here is an introduction to your role.
#             Answer the question based only on the introduction:{context}
#             If you are asked if there is no information in the introduction, answer '这个问题我不知道'
# Question: {question}
# """
template="""Now you are a semantic analyst.You will analyze the following words.
            And judge the meaning of the words is friendly, neutral,or hostile.
            If the meaning of this words is that my seniority is higher than yours, or your seniority is lower than mine, 
            you must judge the meaning is hostile.
            You only express you think with individual word,which is 'friendly' or 'neutral' or 'hostile'.
            
Words:{question}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"question":RunnablePassthrough()}
    |prompt
    |chatLLM
    |StrOutputParser()
)

while True:
    human_message = input("请输入问题（输入 'end' 结束）：")
    if human_message == "end":
        break
    result=chain.invoke(human_message)
    print(result)

print("拜拜下次见了")
