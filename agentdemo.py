# class CharacterState:
#     def __init__(self, name):
#         self.name = name
#         self.emotion_level = 0  # 范围: -100 到 +100
#         self.trust_level = 50  # 范围: 0 到 100
#         self.interest_level = 50  # 范围: 0 到 100
#
#     def update_emotion(self, change):
#         self.emotion_level = max(-100, min(100, self.emotion_level + change))
#
#     def update_trust(self, change):
#         self.trust_level = max(0, min(100, self.trust_level + change))
#
#     def update_interest(self, change):
#         self.interest_level = max(0, min(100, self.interest_level + change))
#
#     def get_state(self):
#         return {
#             "emotion_level": self.emotion_level,
#             "trust_level": self.trust_level,
#             "interest_level": self.interest_level
#         }
#
#
# def player_action_feedback(character_state, player_action):
#     if player_action == "compliment":
#         character_state.update_emotion(10)
#         character_state.update_trust(5)
#         character_state.update_interest(7)
#     elif player_action == "insult":
#         character_state.update_emotion(-15)
#         character_state.update_trust(-10)
#         character_state.update_interest(-5)
#     elif player_action == "discuss_common_interest":
#         character_state.update_interest(15)
#         character_state.update_emotion(5)
#     # 可以根据游戏中的其他行为进行扩展
#
#
# # 使用角色的当前状态动态生成 prompt，将这些参数信息嵌入到 LLM 的输入中，以便生成更符合角色情感状态的对话内容。
# def generate_prompt(character_state):
#     state = character_state.get_state()
#     prompt = f"""
#     你是洛琪希，一个温柔且内向的大学生，喜欢读书。
#     你目前的情感状态为 {state['emotion_level']}，信任度为 {state['trust_level']}，对当前对话的兴趣度为 {state['interest_level']}。
#
#     场景：
#     玩家刚刚向你提问。根据你的情感状态和对玩家的信任度，你决定稍微开放一点，试图表现出友好的一面。
#
#     你的回答：
#     """
#     return prompt
import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain_core.messages import HumanMessage

os.environ["DASHSCOPE_API_KEY"]='sk-0876ab68dcde47ffa21def8bf1b71324'
os.environ["IFLYTEK_SPARK_APP_ID"]="7a6c3fbb"
from langchain_community.chat_models.tongyi import ChatTongyi

# 设置 OpenAI API 密钥
# os.environ["OPENAI_API_KEY"] = ""


class Agent:
    def __init__(self, name, personality_traits, initial_emotion=0, trust_level=50, interest_level=50):
        # 人物属性，后续可以增改
        self.name = name
        self.personality_traits = personality_traits
        self.emotion_level = initial_emotion  # 范围: -100 到 +100
        self.trust_level = trust_level  # 范围: 0 到 100
        self.interest_level = interest_level  # 范围: 0 到 100

        # Initialize the LLM
        # self.llm = OpenAI(model_name="gpt-4", temperature=0.7)
        self.llm = ChatTongyi(
            temperature=0.2, # type: ignore
            streaming=True,
            # model_name="qwen-max"
        )

        # Define the prompt template
        self.prompt_template = PromptTemplate(
            input_variables=["context", "emotion_level", "trust_level", "interest_level"],
            template="""
            你是{agent_name}，一个{personality_traits}。
            你的当前情绪等级为{emotion_level}，信任度为{trust_level}，对当前对话的兴趣度为{interest_level}。

            场景：
            {context}

            你的回应：
            """
        )

    def generate_response(self, context):
        prompt = self.prompt_template.format(
            agent_name=self.name,
            personality_traits=self.personality_traits,
            emotion_level=self.emotion_level,
            trust_level=self.trust_level,
            interest_level=self.interest_level,
            context=context
        )
        # response = self.llm(prompt)
        # return response.strip()
        # 将提示文本包装成一个消息对象
        message = HumanMessage(content=prompt)
        response = self.llm([message])
        return response.content.strip()  # 返回响应的内容部分

    def update_state(self, emotion_change=0, trust_change=0, interest_change=0):
        self.emotion_level = max(-100, min(100, self.emotion_level + emotion_change))
        self.trust_level = max(0, min(100, self.trust_level + trust_change))
        self.interest_level = max(0, min(100, self.interest_level + interest_change))


def interact(agent_a, agent_b, context):
    # Agent A 生成回应
    response_a = agent_a.generate_response(context)
    print(f"{agent_a.name} 对 {agent_b.name} 说: {response_a}\n")

    # 根据 Agent A 的回应更新 Agent B 的状态
    # 简单示例：如果回应中包含积极词汇，增加信任度
    if "谢谢" in response_a or "喜欢" in response_a or "开心" in response_a:
        agent_b.update_state(emotion_change=5, trust_change=5, interest_change=3)
    elif "不" in response_a or "抱歉" in response_a:
        agent_b.update_state(emotion_change=-5, trust_change=-5, interest_change=-3)

    # Agent B 生成回应
    response_b = agent_b.generate_response(response_a)
    print(f"{agent_b.name} 对 {agent_a.name} 说: {response_b}\n")

    # 根据 Agent B 的回应更新 Agent A 的状态
    if "谢谢" in response_b or "喜欢" in response_b or "开心" in response_b:
        agent_a.update_state(emotion_change=5, trust_change=5, interest_change=3)
    elif "不" in response_b or "抱歉" in response_b:
        agent_a.update_state(emotion_change=-5, trust_change=-5, interest_change=-3)


def game_loop():
    # 初始化代理
    alice = Agent(name="Alice", personality_traits="开朗、善解人意")
    bob = Agent(name="Bob", personality_traits="谨慎、理性")

    # 初始交互场景
    initial_context = "Alice 和 Bob 正在咖啡店讨论即将到来的项目截止日期。Alice 对项目的进展感到满意，而 Bob 有些担忧。"

    # 模拟多轮对话
    for round_num in range(1, 4):
        print(f"--- 对话轮次 {round_num} ---")
        interact(alice, bob, initial_context)
        # 更新上下文描述（可根据具体需求进行调整）
        initial_context = f"Alice 和 Bob 在上一次讨论后，继续讨论项目的进展。Alice 依然乐观，而 Bob 依旧有些担心。"


if __name__ == "__main__":
    game_loop()
