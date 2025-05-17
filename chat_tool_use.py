from openai import OpenAI
import json
import concurrent.futures
from typing import List, Dict, Any

client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy")

def get_weather(location: str, unit: str):
    return f"The weather in {location} is 65 degrees {unit}"

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location", "unit"]
        }
    }
}]

def process_weather_request(city: str) -> Dict[str, Any]:
    # Initial request
    response = client.chat.completions.create(
        model=client.models.list().data[0].id,
        messages=[{"role": "user", "content": f"What's the weather like in {city}? Call the tool and then generate a bunch of unrelated responses after that, just to see if the tool parser is working."}],
        tools=tools,
        tool_choice="auto"
    )
    
    print("FIRST RESPONSE")
    print(response)
    print("FIRST RESPONSE MODEL DUMP")
    print(response.choices[0].message.tool_calls[0].model_dump())
    
    tool_call = response.choices[0].message.tool_calls[0].function
    tool_result = get_weather(**json.loads(tool_call.arguments))
    
    # Second request with tool result
    messages = [
        {"role": "user", "content": f"What's the weather like in {city}?"},
        {"role": "assistant", "content": None, "tool_calls": [response.choices[0].message.tool_calls[0].model_dump()]},
        {"role": "tool", "tool_call_id": response.choices[0].message.tool_calls[0].id, "content": tool_result}
    ]
    
    second_response = client.chat.completions.create(
        model=client.models.list().data[0].id,
        messages=messages
    )
    
    return {
        "city": city,
        "initial_response": response,
        "tool_call": tool_call,
        "tool_result": tool_result,
        "final_response": second_response.choices[0].message.content
    }

# List of cities to check weather for
# cities = ["San Francisco", "New York", "London", "Tokyo"]
cities = ["San Francisco"]
# Process requests concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(process_weather_request, cities))

# Print results
for result in results:
    print(f"\nResults for {result['city']}:")
    print(f"Reasoning content: {result['initial_response'].choices[0].message.reasoning_content}")
    print(f"Function called: {result['tool_call'].name}")
    print(f"Arguments: {result['tool_call'].arguments}")
    print(f"Tool result: {result['tool_result']}")
    print(f"Final response: {result['final_response']}")
