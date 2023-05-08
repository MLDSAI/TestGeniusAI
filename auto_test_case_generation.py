import sys
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Function to load a pre-trained GPT model and tokenizer from HuggingFace Transformers library
def load_gpt_model(model_name: str):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    return tokenizer, model

# Function to generate test cases based on the input feature description
def generate_test_cases(tokenizer, model, feature_description: str, num_test_cases: int):
    # Tokenize the feature description
    input_ids = tokenizer.encode(feature_description, return_tensors='pt')

    # Generate test cases using GPT-2 model
    outputs = model.generate(
        input_ids,
        max_length=50,
        do_sample=True,
        top_k=10,
        num_return_sequences=num_test_cases,
        repetition_penalty=1.2
    )

    # Decode the generated outputs
    test_cases = []
    for output in outputs:
        test_case = tokenizer.decode(output, skip_special_tokens=True)
        if test_case not in test_cases:
            test_cases.append(test_case)

    return test_cases

# Command-line interface to input the feature description and the number of test cases to generate
if __name__ == "__main__":
    model_name = "gpt2"
    tokenizer, model = load_gpt_model(model_name)

    feature_description = input("Please enter the feature description: ")
    num_test_cases = int(input("Please enter the number of test cases to generate: "))

    test_cases = generate_test_cases(tokenizer, model, feature_description, num_test_cases)
    print("Generated test cases:")
    for i, test_case in enumerate(test_cases):
        print(f"{i + 1}. {test_case}")
