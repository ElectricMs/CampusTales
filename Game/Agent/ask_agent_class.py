import os
import json
import re
import sqlite3  # 引入SQLite

from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatZhipuAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import StringPromptTemplate

import ssl
print(ssl)
# 设置环境变量（确保通过环境变量或安全方式管理）
os.environ["ZHIPUAI_API_KEY"] = "798c6766d89022735623c294ee28216c.stDi9j8OcRNp9f5L"  # 替换为你的智谱 AI API 密钥

# 初始化 ChatZhipuAI
zhipuai_chat_model = ChatZhipuAI(model="glm-4-plus")


# SQLite数据库初始化
def init_db():
    conn = sqlite3.connect('conversation_history.db')
    cursor = conn.cursor()
    # 创建用于存储对话的表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent_name VARCHAR(255),
            emotion_level INT,          
            user_input TEXT,
            ai_response TEXT
        )
    ''')
    conn.commit()
    conn.close()


class Agent:
    def __init__(self, name, personality_traits, relationship, context, chat_model, initial_emotion=30):
        self.name = name
        self.personality_traits = personality_traits
        self.emotion_level = initial_emotion  # 范围: -100 到 +100
        self.relationship = relationship
        self.chat_model = chat_model
        self.context = context
        # Define the prompt template
        self.prompt_template = PromptTemplate(
            input_variables=["context", "emotion_level", "relationship"],
            template="""
            你的当前好感度为{emotion_level}，当前关系为：{relationship}。

            {context}
            
            """
        )

    def generate_response(self, context):
        # 结合历史会话
        history = self.get_conversation_history()
        chat_prompt = self.prompt_template.format(
            emotion_level=self.emotion_level,
            relationship=self.relationship,
            context=self.context + "\n" + history
        )
        messages = [
            SystemMessage(content=chat_prompt),
            HumanMessage(content=context)
        ]
        # chat_prompt = self.prompt_template.format(
        #     emotion_level=self.emotion_level,
        #     context=self.context,
        #     relationship=self.relationship,
        # )
        # messages = []
        # messages.append(SystemMessage(content=chat_prompt))
        # messages.extend(new_his_message)
        # messages.append(HumanMessage(content=context))
        # print(messages)
        response = self.chat_model.invoke(messages)  # 使用 invoke 方法
        return response.content.strip()  # 提取 content 并调用 strip()

    def get_conversation_history(self, limit=4):
        conn = sqlite3.connect('conversation_history.db')
        cursor = conn.cursor()
        # 查询历史会话
        cursor.execute('SELECT agent_name, emotion_level, user_input, ai_response FROM conversation WHERE agent_name = ? ORDER BY id DESC LIMIT ?', (self.name, limit))
        rows = cursor.fetchall()
        print(rows)
        if(len(rows) != 0):
            self.emotion_level = rows[0][1]
        conn.close()
        # new_message = []        
        # for row in rows:
        #     new_message.append(HumanMessage(content=row[1]))
        #     new_message.append(AIMessage(content=row[2]))
        # print(new_message)
        # return new_message
        # 将历史会话整合为字符串
        history = "\n".join([f"用户: {row[2]}\nAI: {row[3]}" for row in rows])
        return history


    def user_interact_with_agent(self, user_input):
        context = f"{user_input}"
        response = self.generate_response(context)
        
        # 提取AI的回复
        greeting_start = 0
        greeting_end = response.find("\n\n")
        greeting = response[greeting_start:greeting_end].strip()

        goodness_match = re.search(r'当前好感度：(\d+)', response)
        if goodness_match:
            goodness = int(goodness_match.group(1))
        else:
            goodness = None

        json_response = {
            "agent_name": self.name,
            "emotion_level": goodness,
            "response": greeting,
            "relationship": self.relationship
        }
        print(json_response)

        # 更新好感度
        if goodness==None or goodness - self.emotion_level > 10 or goodness - self.emotion_level< -10 : # type: ignore
            self.emotion_level = self.emotion_level + 1 # type: ignore
        else:
            self.emotion_level = goodness
      
        if self.emotion_level >= 400:
            self.relationship = "God"
        elif self.emotion_level >= 200:
            self.relationship = "Great"
        elif self.emotion_level >= 100:
            self.relationship = "好友"
        elif self.emotion_level >= 50:
            self.relationship = "普通朋友"
        else: 
            self.relationship = "陌生人"
        
            
        # 构建 JSON 响应
        json_response = {
            "agent_name": self.name,
            "emotion_level": self.emotion_level,
            "response": greeting,
            "relationship": self.relationship
        }

        # 保存到数据库
        self.save_conversation_to_db(user_input, greeting)

        return json_response


    def save_conversation_to_db(self, user_input, ai_response):
        conn = sqlite3.connect('conversation_history.db')
        cursor = conn.cursor()
        # 插入对话到数据库
        cursor.execute('INSERT INTO conversation (agent_name, emotion_level ,user_input, ai_response) VALUES (?, ?, ?, ?)', (self.name, self.emotion_level ,user_input, ai_response))
        conn.commit()
        conn.close()


