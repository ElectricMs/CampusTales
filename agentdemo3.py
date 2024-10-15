
import os
import json
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatZhipuAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 设置环境变量（确保通过环境变量或安全方式管理）
os.environ["ZHIPUAI_API_KEY"] = "798c6766d89022735623c294ee28216c.stDi9j8OcRNp9f5L"  # 替换为新的智谱 AI API 密钥

# 初始化 ChatZhipuAI
zhipuai_chat_model = ChatZhipuAI(model="glm-4", temperature=0.2)

# 初始化 VADER 分析器
analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment_with_vader(text):
    """
    使用 VADER 进行情感分析，返回情感类别。

    参数：
        text (str): 要分析的文本。

    返回：
        str: 情感类别（正面、中性、负面）。
    """
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        return "正面"
    elif compound <= -0.05:
        return "负面"
    else:
        return "中性"


class Agent:
    def __init__(self, name, personality_traits, chat_model, initial_emotion=0, trust_level=50, interest_level=50):
        self.name = name
        self.personality_traits = personality_traits
        self.emotion_level = initial_emotion  # 范围: -100 到 +100
        self.trust_level = trust_level  # 范围: 0 到 100
        self.interest_level = interest_level  # 范围: 0 到 100
        self.chat_model = chat_model

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
        # 构建消息列表
        messages = [
            SystemMessage(content=f"你是{self.name}，一个{self.personality_traits}。"),
            HumanMessage(
                content=f"情绪等级: {self.emotion_level}, 信任度: {self.trust_level}, 兴趣度: {self.interest_level}"),
            HumanMessage(content=context)
        ]
        response = self.chat_model.invoke(messages)  # 使用 invoke 方法
        return response.content.strip()  # 提取 content 并调用 strip()

    def update_state(self, emotion_change=0, trust_change=0, interest_change=0): 
        self.emotion_level = max(-100, min(100, self.emotion_level + emotion_change))
        self.trust_level = max(0, min(100, self.trust_level + trust_change))
        self.interest_level = max(0, min(100, self.interest_level + interest_change))


def interact(agent_a, agent_b, context):
    # Agent A 生成回应
    response_a = agent_a.generate_response(context)
    print(f"{agent_a.name} 对 {agent_b.name} 说: {response_a}\n")

    # 使用情感分析（VADER）
    sentiment_a = analyze_sentiment_with_vader(response_a)
    print(f"情感分析 - {agent_a.name} 的回应: {sentiment_a}")
    if sentiment_a == "正面":
        agent_b.update_state(emotion_change=5, trust_change=5, interest_change=3)
    elif sentiment_a == "负面":
        agent_b.update_state(emotion_change=-5, trust_change=-5, interest_change=-3)

    # Agent B 生成回应
    response_b = agent_b.generate_response(response_a)
    print(f"{agent_b.name} 对 {agent_a.name} 说: {response_b}\n")

    # 使用情感分析（VADER）
    sentiment_b = analyze_sentiment_with_vader(response_b)
    print(f"情感分析 - {agent_b.name} 的回应: {sentiment_b}")
    if sentiment_b == "正面":
        agent_a.update_state(emotion_change=5, trust_change=5, interest_change=3)
    elif sentiment_b == "负面":
        agent_a.update_state(emotion_change=-5, trust_change=-5, interest_change=-3)


def user_interact_with_agent(user_input, agent):
    """
    允许用户输入文字与指定的代理进行对话，并返回包含代理状态和回应内容的 JSON 对象。

    参数：
        user_input (str): 用户输入的文字。
        agent (Agent): 要与之对话的代理实例。

    返回：
        dict: 包含代理的当前状态和回应内容的 JSON 对象。
    """
    # 将用户输入作为上下文发送给代理
    context = f"用户对你说: {user_input}"
    response = agent.generate_response(context)

    # 使用情感分析（VADER）
    sentiment = analyze_sentiment_with_vader(response)

    # 根据情感结果更新代理的状态
    if sentiment == "正面":
        agent.update_state(emotion_change=5, trust_change=5, interest_change=3)
    elif sentiment == "负面":
        agent.update_state(emotion_change=-5, trust_change=-5, interest_change=-3)
    # 中性则不做改变

    # 构建 JSON 响应
    json_response = {
        "agent_name": agent.name,
        "emotion_level": agent.emotion_level,
        "trust_level": agent.trust_level,
        "interest_level": agent.interest_level,
        "response": response,
        "sentiment": sentiment
    }

    return json_response


def game_loop():
    # 初始化代理
    alice = Agent(name="Alice", personality_traits="开朗、善解人意", chat_model=zhipuai_chat_model)
    bob = Agent(name="Bob", personality_traits="谨慎、理性", chat_model=zhipuai_chat_model)

    # 初始交互场景
    initial_context = "Alice 和 Bob 正在咖啡店讨论即将到来的项目截止日期。Alice 对项目的进展感到满意，而 Bob 有些担忧。"

    # 模拟代理之间的对话
    for round_num in range(1, 4):
        print(f"--- 对话轮次 {round_num} ---")
        interact(alice, bob, initial_context)
        # 更新上下文描述（可根据具体需求进行调整）
        initial_context = f"Alice 和 Bob 在上一次讨论后，继续讨论项目的进展。Alice 依然乐观，而 Bob 依旧有些担心。"

    # 用户与代理的对话
    while True:
        user_input = input("你想对 Alice 说什么？（输入 'quit' 退出）: ")
        if user_input.lower() == "quit":
            print("游戏结束。")
            break

        # 用户与 Alice 对话
        alice_response = user_interact_with_agent(user_input, alice)

        # 打印 JSON 响应
        print(json.dumps(alice_response, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    game_loop()
