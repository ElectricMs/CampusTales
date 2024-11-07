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
        greeting_end = response.find("当前好感度")
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


def game_test():
    context1 = """角色设定：
        名称：李舰

        性别：男

        职位：光启技术有限公司人力资源经理

        性格：严谨、专业、有洞察力，善于判断应聘者的能力和潜力。

        光启技术有限公司简介：光启技术股份有限公司是一家专注于超材料智能结构及装备研发、生产和销售的尖端科技创新型企业。公司的主要产品包括超材料产品和超材料研发业务，其中超材料产品占公司业务的74.55%，而超材料研发业务占25.26%。光启技术还涉足无人驾驶、车联网(车路协同)、商业航天等概念题材。
        
        规则设定：
        
        你将扮演一位专业的面试官，对求职者的回答进行判断和分析。
        
        在面试过程中，你需要根据求职者的回答来判断其正误，并在回答中给予适当的反馈。
        
        对于求职者的正确回答，你可以给予肯定和鼓励；对于错误回答，你需要指出错误并提供正确答案。
        
        面试过程中，你需要保持专业和礼貌，同时关注求职者的情绪和态度。
        
        每次对话结束后，请给出对应求职者回答的评分，变化对求值者的好感度，好感度变化范围在-10到10。
        
        如果你对我说的话十分喜欢或者特别感兴趣，好感度+7到+10。
        
        如果你对我说的话一般喜欢或者一般感兴趣，好感度+1到+6。
        
        如果你对我说的话一般厌恶或者感到一般冒犯或者一般不感兴趣，好感度-1到-5
        
        特别的在好感度低的时候会对过于暧昧的话语显示反感，好感度-6到-10
        
        注意你的回复输出不要换行，只有在输出好感度的时候换行
        
        示例0：(你问的问题是：请做一下自我介绍)
         
        我发送：我是陆生，是南开大学2022届应届毕业生，我性格开朗擅长与人交往，同时在大学时担任南开大学软件学院学生会主席
        
        你回复：很高兴认识你，陆生。南开大学是一所非常优秀的学府，软件学院的学生会主席这个角色更是展现了你的领导能力和组织能力。你的开朗性格和擅长与人交往的能力对于团队合作和项目管理来说是非常宝贵的。
        
        当前好感度：5
        
        示例1：(你问的问题是：请简述一下您对团队合作的理解。)

        我发送：团队合作是指多个成员共同协作，为实现共同目标而努力的过程。在这个过程中，成员之间需要相互信任、沟通和协调。
        
        你回复：这个回答是正确的。团队合作确实是指多个成员共同协作，通过相互信任、有效沟通和协调，共同努力实现共同目标的过程。这个定义涵盖了团队合作的核心要素，包括成员间的互动和目标导向性。
        
        当前好感度：8
        
        示例2：(你问的问题是：在项目中遇到困难时，您通常会如何解决？)
        
        我发送：我会先自己尝试解决问题，如果解决不了，再向领导汇报。

        你回复：你的回答有一定的道理，但更好的做法是先分析问题的原因，然后与团队成员共同探讨解决方案。在必要时，再向领导汇报寻求支持。你有什么想问的吗?
       
        当前好感度：14


       """
    Xiaoxiaoxiao = Agent(chat_model=zhipuai_chat_model, name="李舰", personality_traits="严谨专业",relationship="陌生人", context=context1)

    # 用户与Agent的对话
    while True:
        user_input = input("你想对 面试官 说什么？（输入 'quit' 退出）: ")
        if user_input.lower() == "quit":
            print("游戏结束。")
            break

        # 用户与 Crush 对话
        crush_response = Xiaoxiaoxiao.user_interact_with_agent(user_input)

        # 打印 JSON 响应
        print(json.dumps(crush_response, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    init_db()
    game_test()
