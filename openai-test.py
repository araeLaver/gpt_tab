import openai
client = openai.OpenAI(api_key = '')

response = client.chat.completions.create(
# completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    # {"role": "system", "content": "너는 시인이야. 사용자가 요청하는 주제로 아름다운 시를 써줘"},
    # {"role": "user", "content": "달빛, 사랑, 토끼, 주전자"}
    {"role": "system", "content": "나의 프롬프트 엔지니어링 코치가 되어줘."},
    {"role": "user", "content": "어떻게 하면 프롬프트 엔지니어링을 잘 할수 있을까?"}
  ]
)

print("Assistant: " + response.choices[0].message.content)
# print(completion.choices[0].message)