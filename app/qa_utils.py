from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# loading model globally
tokenizer = AutoTokenizer.from_pretrained('t5-small')
model = AutoModelForSeq2SeqLM.from_pretrained('t5-small')

# creating answer to the user question
def create_ans(context, question):
    # combining context and question
    input_text = f'Context: {context}\nQuestion: {question}'
    # tokenizing the input
    inputs = tokenizer(input_text, return_tensors='pt', truncation=True)
    try:
        outputs = model.generate(**inputs)
    except Exception as e:
        print('Error generating answer:', e)
        return 'Unable to generate answer'
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer