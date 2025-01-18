from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Загрузка слов из файла
def load_words():
    try:
        with open("word_dict.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Сохранение слов в файл
def save_words():
    with open("word_dict.json", "w", encoding="utf-8") as file:
        json.dump(word_dict, file, ensure_ascii=False, indent=4)

# Загрузка данных из файла
word_dict = load_words()

@app.route('/api/words', methods=['GET'])
def get_words():
    """Получение всех слов из словаря"""
    return jsonify(word_dict), 200

@app.route('/api/words', methods=['POST'])
def add_word():
    """Добавление нового слова в словарь"""
    word = request.json.get("word")
    definition = request.json.get("definition")
    if word and definition:
        word_dict[word] = definition
        save_words()
        return jsonify({"message": f"Word '{word}' added successfully!"}), 201
    return jsonify({"error": "Word or definition is missing!"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
