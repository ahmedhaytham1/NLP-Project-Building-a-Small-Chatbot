import re

def clean_text(text):
    """
    Clean and normalize text
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text


def preprocess_dataset(dataset):
    """
    Apply preprocessing to dataset
    """
    dataset = dataset.map(lambda x: {
        "clean_context": clean_text(x["context"]),
        "clean_question": clean_text(x["question"])
    })
    return dataset


if __name__ == "__main__":
    from data.dataset_loader import load_data

    data = load_data()
    processed_data = preprocess_dataset(data)

    print("Preprocessing completed!")
    print(processed_data[0])
