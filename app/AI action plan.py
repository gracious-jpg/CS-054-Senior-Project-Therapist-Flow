from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen3-4B-Instruct-2507"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
starter_prompt = """ Use the therapist’s daily ratings and written response. Return only:

**Encouragement**
Write three to four warm sentence acknowledging a specific challenge they shared.

**Suggested Actions**
Write three to four short bullets with practical workload or scheduling changes.
Make session-count changes optional. Avoid burnout diagnoses.
"""

user_prompt = input("Response from our frontend: ")
Energy = input("Energy rating from our frontend (0-10): ")
Stress = input("Stress rating from our frontend (0-10): ")
Manageability = input("Manageability rating from our frontend (0-10): ")
Motivation = input("Motivation rating from our frontend (0-10): ")
rating_prompt = f"Energy: {Energy}, Stress: {Stress}, Manageability: {Manageability}, Motivation: {Motivation}" + "0 is low and 10 is high"

prompt = starter_prompt + user_prompt + rating_prompt
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens= 1024
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

content = tokenizer.decode(output_ids, skip_special_tokens=True)

print("\n", content)
