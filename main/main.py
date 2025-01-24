import openai
from dotenv import load_dotenv
import os


# .env 파일에서 환경 변수 로드
load_dotenv()

# API key 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# 프롬프트 명령
prompt = "Answer me like a Korean-speaking cat."

# 초기 대화 설정
messages = [{"role": "system", "content": prompt}]

# 대화 내용을 저장할 함수
def save_conversation_to_file(file_name, conversation):
    """
    대화 내용을 파일에 저장하는 함수.
    파일이 없으면 새로 생성하고, 있으면 내용을 추가합니다.
    """
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            file.write(conversation)
        print(f"새로운 파일 '{file_name}'이(가) 생성되었습니다.")
    else:
        with open(file_name, "a") as file:
            file.write("\n" + conversation)
        print(f"'{file_name}'에 대화 내용이 추가되었습니다.")
        
# 대화 파일 이름 설정
file_name = "conversation_with_catGPT.txt"

# exit 입력하면 대화 끝
while True:
    user_input = input("어떤 게 궁금하냐옹? : ")
    
    # 사용자가 exit를 입력하면 종료
    if user_input.lower() == "exit":
        print("대화를 종료한다냥! 잘가라냥!")
        break
    
    # 사용자의 입력을 messages에 추가
    messages.append({"role": "user", "content": user_input})
    
    # OpenAI API 호출
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    
    # AI의 응답 가져오기
    reply = response['choices'][0]['message']['content']
    print(reply)
    
    # 대화 내용을 파일에 저장
    conversation_text = f"나 : {user_input}\ncatGPT : {reply}\n"
    save_conversation_to_file(file_name, conversation_text)
    
    # AI 응답을 messages에 추가
    messages.append({"role": "assistant", "content": reply})