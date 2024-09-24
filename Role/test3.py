import os

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory

os.environ["DASHSCOPE_API_KEY"]='sk-0876ab68dcde47ffa21def8bf1b71324'
os.environ["IFLYTEK_SPARK_APP_ID"]="7a6c3fbb"
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_community.document_loaders import TextLoader


chatLLM = ChatTongyi(
    temperature=0.2,
    streaming=True,
    model_name="qwen-max"
)
file_path = "Role/ayong.txt"  # Your local file path"
loader = TextLoader(file_path, encoding="utf-8")
Txt = loader.load()
print(Txt)
#导包
from langchain_huggingface import HuggingFaceEmbeddings
EMBEDDING_DEVICE="cpu"

embeddings=HuggingFaceEmbeddings(model_name=r"m3e-base-huggingface",
                                 model_kwargs={'device':EMBEDDING_DEVICE})
print(embeddings)
#向量数据库FAISS
#导包，生成词向量，存储到FAISS中
from langchain_text_splitters import RecursiveCharacterTextSplitter
#生成分词器
text_splitter=RecursiveCharacterTextSplitter()
documents=text_splitter.split_documents(documents=Txt)
print(documents)

from langchain_community.vectorstores import FAISS


#建立索引：将词向量存储向量数据库
vector=FAISS.from_documents(documents=documents,embedding=embeddings)
print(vector)
#生成链：带有历史记录的检索链

#生成一个基于向量存储的检索器
retriever=vector.as_retriever()



prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Now you are playing a role, and here is an introduction to your role.Answer user's question based only on the introduction:{context}"
            "If you are asked if there is no information in the introduction, answer '这个问题我不知道'",
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)
qa_chain = create_stuff_documents_chain(chatLLM, prompt)
retrieval_chain = create_retrieval_chain(retriever, qa_chain)
def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, "sqlite:///memory.db")
history=SQLChatMessageHistory(session_id="2f", connection_string="sqlite:///memory.db")
chain_with_history = RunnableWithMessageHistory(
    retrieval_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)
while True:
    human_message = input("请输入问题（输入 'end' 结束）：")
    if human_message == "end":
        break
    result=chain_with_history.invoke({"input":human_message},
                                     config={"configurable": {"session_id": "2f"}})
    print(result)
    history.add_user_message(HumanMessage(content=human_message))
    ai_message:str=result["answer"]
    print(ai_message)
    history.add_ai_message(AIMessage(content=ai_message))

print("拜拜下次见了")
#以下是实现有历史对话记录的部分

