# LLM_GPT_Study
>**2025년 1월 24일 (금)**
> - 프롬프트로 Korean-speeking cat을 만들어서 간단히 대화형으로 만들었어요
> - 대화 내용을 txt 파일로 생성하여 기록했어요
```python
# LLM 과제(필수)
1. 과제를 위한 git 레파지토리 생성
2. Transformer 모델에 대해 조사하고 readme에 작성
3. main.py 코드 작성
3.1. .env 파일에 api key를 main.py로 불러와서 사용할 것
3.2. 본인만의 프롬프트 명령어를 작성해볼 것
3.3. exit를 입력받기 전까지 사용자와 대화시킬 것
3.4. 대화를 txt 파일에 기록할 것.
```
---
## 📕 Transformer 모델이란?
>**자연어 처리(NLP)와 기타 머신 러닝 작업에서 사용되는 딥러닝 모델 구조다.**
<br><br>

### 📕 주요 개념과 구조 🤔
1. **Self-Attention Mechanism(자체 주의 메커니즘)**
    - Transformer의 핵심 아이디어는 Self-Attention이다.
    - 예를 들어,
        "I went to the bank to deposit money"에서 "bank"라는 단어는 문맥에 따라 "강둑"이 아닌 "금융기관"을 의미한다는 것을 Self-Attention이 문맥적 정보를 학습한다.
<br><br>

2. **Encoder-Decoder 구조**
    - Encoder와 Decoder로 구성된다.
        - Encoder: 입력 문장의 특징을 학습하고 표현(벡터)을 생성하고, 주로 **문장 이해**에 사용된다.
        - Decoder: Encoder의 출력을 사용해 새로운 문장을 생성하고, 주로 **문장 생성**이나 **번역**에 사용된다.
<br><br>

3. **멀티헤드 어텐션 (Multi-Head Attention)**
    - 여러 Attention 헤드를 ***병렬*** 로 실행해 입력 데이터의 다양한 의미를 동시에 학습한다.
    - 예를 들어,
        한 헤드는 단어의 문법적 관계를, 다른 헤드는 문맥적 의미를 학습할 수 있다.
<br><br>

4. **Position Embedding (위치 임베딩)**
    - Transformer는 순서를 고려하지 않는 모델이기 때문에 입력 데이터의 순서 정보를 보완하기 위해 각 단어에 위치 정보를 추가한다.
<br><br>

### 📕 Transformer 모델의 장점 🤔
1. **병렬 처리 가능**
    - RNN(Recurrent Neural Network)과 달리 입력 데이터를 <u>순차적으로 처리하지 않고</u> 한 번에 병렬로 처리할 수 있어 <u>학습 속도가 빠르다</u>.
<br><br>

2. **긴 문맥 학습 가능**
    - Self-Attention을 통해 긴 문장이나 문서의 모든 단어 관계를 학습할 수 있다.
<br><br>

3. **범용성**
    - 번역, 텍스트 생성, 요약, 질문 답변 등 다양한 NLP 작업에 적합하다.
    - 컴퓨터 비전(예: Vision Transformer)과 음성 처리 등에도 확장되었다.
<br><br>

### 📕 대표적인 Transformer 기반 모델 🤔
1. **GPT (Generative Pre-trained Transformer)**
    - OpenAI에서 개발한 언어 생성 모델이다.
    - 주어진 문맥에서 다음 단어를 예측하는 방식으로 작동한다.
<br><br>

2. **BERT (Bidirectional Encoder Representations from Transformers)**
    - Google에서 개발한 언어 이해 모델이다.
    - 양방향으로 문맥을 이해하여 텍스트의 의미를 학습한다.
<br><br>

3. **T5 (Text-to-Text Transfer Transformer)**
    - Google에서 개발한 모델로, 모든 NLP 작업을 *"텍스트 입력 → 텍스트 출력"* 으로 처리한다.
<br><br>

4. **ViT (Vision Transformer)**
    - Transformer를 컴퓨터 비전에 적용한 모델이다.
