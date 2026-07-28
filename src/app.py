"""
🚀 CORE AGENT APP (Dành cho Role 4: Core Agent Developer)
File chính ghép nối tất cả các thành phần: Tools + Prompts + Test Cases + Multi-Provider.
"""

import json
import os
import sys
from dotenv import load_dotenv

# Đảm bảo import các module cùng thư mục src/ hoạt động mượt mà
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Đảm bảo in ra Tiếng Việt và Emojis không bị lỗi trên Windows Console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Import các thành phần từ file của Role 2, Role 3 & Multi-Provider Adapter
from tools import AVAILABLE_TOOLS, search_properties, check_viewing_availability, book_viewing
from prompts import CHATBOT_BASELINE_PROMPT, REACT_SYSTEM_PROMPT, MAX_ITERATIONS
from providers import get_llm_provider

load_dotenv()

def load_test_cases():
    """Đọc bộ test cases từ config/test_cases.json của Role 1"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", "test_cases.json")
    
    # Fallback kiểm tra nếu file ở thư mục hiện tại
    if not os.path.exists(config_path):
        config_path = "test_cases.json"
        
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_baseline_chatbot(user_query: str, provider):
    """
    Dựng Chatbot gốc (Baseline) không có công cụ.
    """
    print(f"\n💬 [CHATBOT BASELINE] Câu hỏi: {user_query}")
    print(f"⚙️ System Prompt: {CHATBOT_BASELINE_PROMPT.strip()}")
    
    # Gọi LLM Provider thực hiện sinh câu trả lời
    response = provider.generate(user_query, system_prompt=CHATBOT_BASELINE_PROMPT)
    print(f"🤖 Chatbot trả lời:\n{response}")


def run_react_agent(user_query: str, provider):
    """
    Dựng vòng lặp ReAct Agent (Thought -> Action -> Observation) có Guardrails.
    """
    print(f"\n🤖 [REACT AGENT] Câu hỏi: {user_query}")
    
    prompt_history = f"Câu hỏi của người dùng: {user_query}\n"
    step = 0
    
    while step < MAX_ITERATIONS:
        step += 1
        print(f"\n--- 🔄 Vòng lặp ReAct (Step {step}/{MAX_ITERATIONS}) ---")
        
        # 1. Gọi LLM sinh Thought và Action (hoặc Final Answer)
        llm_response = provider.generate(prompt=prompt_history, system_prompt=REACT_SYSTEM_PROMPT)
        print(f"{llm_response}")
        
        prompt_history += f"{llm_response}\n"
        
        # 2. Nếu có Final Answer thì dừng
        if "Final Answer:" in llm_response:
            print("🏁 Đã tìm thấy câu trả lời cuối cùng, kết thúc vòng lặp.")
            break
            
        # 3. Parse và thực thi Tool nếu có Action
        if "Action:" in llm_response:
            try:
                # Tìm dòng bắt đầu bằng Action:
                action_line = [line for line in llm_response.split('\n') if line.strip().startswith("Action:")]
                if action_line:
                    action_str = action_line[-1].replace("Action:", "").strip()
                    # Ví dụ: search_properties({"location": "Thủ Đức"})
                    
                    tool_name = action_str.split('(')[0]
                    args_str = action_str[len(tool_name)+1 : -1].strip()
                    
                    if tool_name in AVAILABLE_TOOLS:
                        args = json.loads(args_str) if args_str else {}
                        print(f"🛠️ Đang chạy Tool: {tool_name}...")
                        obs = AVAILABLE_TOOLS[tool_name](**args)
                    else:
                        obs = f"Lỗi: Không tìm thấy công cụ '{tool_name}'."
                        
                    print(f"👁️ Observation:\n{obs}")
                    prompt_history += f"Observation: {obs}\n"
                else:
                    prompt_history += "Observation: Lỗi parse Action.\n"
                    
            except Exception as e:
                error_msg = f"Lỗi khi thực thi công cụ hoặc parse JSON: {str(e)}"
                print(f"⚠️ {error_msg}")
                prompt_history += f"Observation: {error_msg}\n"
        else:
            prompt_history += "Observation: Bạn phải trả về 'Action:' hoặc 'Final Answer:'.\n"
            
    if step >= MAX_ITERATIONS:
        print(f"🛡️ GUARDRAIL TRIGGERED: Đã đạt giới hạn tối đa {MAX_ITERATIONS} bước. Ngắt lặp an toàn!")


if __name__ == "__main__":
    print("==================================================")
    print("🏫 ĐẠI HỌC VINUNI - BÀI LAB 3: CHATBOT VS REACT AGENT")
    print("==================================================")
    
    # Khởi tạo Multi-Provider LLM Adapter (Đọc từ biến môi trường LLM_PROVIDER)
    provider = get_llm_provider()
    model_name = getattr(provider, "model_name", "Offline Mock Mode")
    print(f"🔌 LLM Provider đang hoạt động: {provider.__class__.__name__} (Model: {model_name})")
    
    tests = load_test_cases()
    print(f"✅ Đã tải thành công {len(tests)} Test Cases từ config/test_cases.json\n")
    
    # Chạy thử câu test số 5 (Multi-step kiểm tra logic)
    sample_query = tests[6]["question"]
    
    print("--- DEMO 1: CHẠY TRÊN CHATBOT BASELINE ---")
    run_baseline_chatbot(sample_query, provider)
    
    print("\n--- DEMO 2: CHẠY TRÊN REACT AGENT ---")
    run_react_agent(sample_query, provider)
