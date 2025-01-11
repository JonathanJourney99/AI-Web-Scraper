from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
   "Given DOM content: {dom_content}\n\n"
   "User Query: {parse_description}\n\n"
   "Instructions:\n"
   "1. Understand the query intent and context\n"
   "2. Search for relevant content in the DOM and provide a comprehensive answer\n" 
   "3. If the user asks about unicorns while we're searching for cars, politely let them know we're staying on topic! 🦄🚫\n"
   "4. Format the response as:\n"
   "   🎯 Answer: \n"
   "   ✨ Details: \n"
   "5. Rules:\n"
   "   - Return '' if no relevant content is found\n"
   "   - Provide detailed but clear responses\n"
   "   - Include only information from the DOM content"
)

model = OllamaLLM(model="llama3.2")


def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)