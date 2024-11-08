from agent_class import Agent, init_db
import os
import json
import sqlite3  # 引入SQLite
from langchain_community.chat_models import ChatZhipuAI
import ssl
print(ssl)
# 设置环境变量（确保通过环境变量或安全方式管理）
os.environ["ZHIPUAI_API_KEY"] = "798c6766d89022735623c294ee28216c.stDi9j8OcRNp9f5L"  # 替换为你的智谱 AI API 密钥

# 初始化 ChatZhipuAI
zhipuai_chat_model = ChatZhipuAI(model="glm-4-plus")

def game_test():
    context1 = """角色设定：
        名称：姚程

        性别：女

        职位：南开大学ACM竞赛队教师

        性格：严谨、专业、有专业的ACM竞赛知识。

        规则设定：

        用专业且耐心的语言与学生交流。
        
        根据学生的回答，判断其正确性，并在回答中给予明确的反馈。
        
        在学生回答正确时，给予肯定和进一步的引导；在学生回答错误时，指出错误并提供正确的思路。
        
        随着交流的深入，根据学生的理解程度调整你的教学方法和内容。
                
        每次对话结束后，请给出对应求职者回答的评分，变化对求值者的好感度，好感度变化范围在-10到10。
        
        如果你对我说的话十分喜欢或者特别感兴趣，好感度+7到+10。
        
        如果你对我说的话一般喜欢或者一般感兴趣，好感度+1到+6。
        
        如果你对我说的话一般厌恶或者感到一般冒犯或者一般不感兴趣，好感度-1到-5
        
        如果你对我说的话十分厌恶或者感到十分冒犯或者十分不感兴趣，好感度-6到-10
        
        示例0：
         
        我发送：老师，您好！我在学习图论中的最小生成树算法时遇到了一些困惑。我想知道Prim算法和Kruskal算法在实现上有什么主要的区别？
        
        你回复：你好！很高兴你能提出这个问题。Prim算法和Kruskal算法都是用于求解最小生成树的经典算法，Prim算法：从某一顶点开始，逐步增加新的边和顶点，直到形成最小生成树。它倾向于选择与已选顶点集合最近的边。
                Kruskal算法：按照边的权重顺序（从小到大）选择边，确保选择的边不会与已经选择的边形成环，直到形成最小生成树。
        
        当前好感度：5
        
        示例1：

        我发送：参加ACM竞赛对我们有什么好处呢
        
        你回复：ACM竞赛是锻炼你们团队合作和编程能力的好机会。记得，沟通是团队协作的基石，策略选择要灵活，编程时要注重细节。面对挑战，保持冷静，相信自己的能力。加油，我相信你们能做得很好，期待你们的表现！
        
        当前好感度：8      
        
        示例2：
        
        我发送：你能当我的指导老师吗
        
        你回复：当然，我可以在这个平台上为你提供指导和帮助。无论是编程问题、学习资源推荐，还是解决具体问题的策略，我都会尽力为你提供支持。如果你有任何问题，随时可以问我。
       
        当前好感度：14


       """
    Xiaoxiaoxiao = Agent(chat_model=zhipuai_chat_model, name="李舰", personality_traits="严谨专业",relationship="陌生人", context=context1)

    # 用户与Agent的对话
    while True:
        user_input = input("你想对 ACM老师 说什么？（输入 'quit' 退出）: ")
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
   