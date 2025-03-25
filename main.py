import streamlit as st
import requests

# 外部APIのエンドポイント
API_URL = "https://np9i6wu5q3.execute-api.ap-northeast-1.amazonaws.com/PROD/hanson-20250327"

def get_bot_response(user_message):
    """
    外部APIを呼び出してチャットボットの応答を取得する関数
    """
    try:
        # APIにリクエストを送信
        response = requests.post(API_URL, json={"message": user_message})
        
        # ステータスコードを確認
        if response.status_code == 200:
            # レスポンスをJSON形式で取得
            response_data = response.json()
            
            # "body" -> "content" -> [0] -> "text" を取得
            return response_data.get("body", {}).get("content", [{}])[0].get("text", "エラー: 応答がありません")
        else:
            return f"エラー: ステータスコード {response.status_code}"
    except Exception as e:
        return f"エラー: {str(e)}"

# Streamlitアプリのタイトル
st.title("🤖 フレンドリーチャットボット")

# セッション状態の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# チャット履歴の表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ユーザー入力
user_input = st.text_input("メッセージを入力してください：", key="user_input")

# 送信ボタン
if st.button("送信", key="send") and user_input:
    # ユーザーの入力を表示
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 外部APIからボットの応答を取得
    with st.chat_message("assistant"):
        response = get_bot_response(user_input)
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
