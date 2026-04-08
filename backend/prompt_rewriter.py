def detect_type(prompt):
    prompt = prompt.lower()
    technical_keywords = [
        "code", "build", "api", "program", "app", "website",
        "backend", "frontend", "server", "database",
        "react", "node", "python", "java", "fix", "bug",
        "debug", "deploy", "implementation"
    ]

    writing_keywords = [
        "write", "essay", "story", "email", "blog",
        "article", "script", "caption", "post",
        "paragraph", "content", "draft"
    ]

    general_keywords = [
        "explain", "what", "why", "how",
        "define", "meaning", "concept",
        "introduction", "overview"
    ]
    if any(word in prompt for word in technical_keywords):
        return "technical"
    elif any(word in prompt for word in writing_keywords):
        return "writing"
    elif any(word in prompt for word in general_keywords):
        return "general"
    else:
        return "general"

def clean_input(prompt):
    return prompt.strip()

def rewrite_prompt(user_input):
    prompt_type = detect_type(user_input)

    if prompt_type == "technical":
        role = "Senior Software Developer"
        context = "User has basic programming knowledge"
        output = "Step-by-step explanation with code examples"

    elif prompt_type == "writing":
        role = "Professional Writer"
        context = "Focus on clarity, tone, and structure"
        output = "Well-structured paragraphs"

    else:
        role = "Subject Matter Expert"
        context = "Explain in simple terms for a beginner"
        output = "Clear bullet points"

    return {
        "role": role,
        "task": user_input,
        "context": context,
        "constraints": "Keep it concise and easy to understand",
        "output_format": output
    }

if __name__ == "__main__":
    while True:
        user_input = input("Enter your prompt (or type 'exit'): ")
        if user_input.lower() == "exit":
            break
        user_input = clean_input(user_input)
        improved = rewrite_prompt(user_input)
        print("Improved prompt: \n")
        print(improved)        