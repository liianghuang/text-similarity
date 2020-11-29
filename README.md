## Introduction
This is an algorithm to compute similiarity of two documents, the score should be 0 to 1, where 0 means there are no similiarity and 1 means they are identical. 

## Requirements
* **Pretrained embedding for word2vec**  
    Can be found [here](https://wikipedia2vec.github.io/wikipedia2vec/pretrained/) for your use case. Here I used `enwiki_20180420` with 100 dimesional vector for demonstration.
* **Stopwords from spacy**  
    Get it using the following code
    ```
    pip install spacy
    python3 -m spacy download en_core_web_sm
    ```

## How to run web app
```
cd web
export FLASK_APP=run.py
flask run
```

## API Documentation
**Get Similiarity**
----
  Returns json data of similiarity of two texts, with key `similiarity`.

* **URL**

  /get_sim/option

* **Method:**

  `POST`
  
*  **URL Params**

    `option: string`  
    There are two options to calculate similiarity of documents, `cosine_similiarity` or `word2vec` 

* **Data Params**  
  **Required:**

  `{"first": "some text","second":"another text"}`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "similiarity" : 0.867965}`

* **Sample Call:**

  ```
  curl -i -H "Content-Type: application/json" -X POST -d '{"first":"The easiest way .","second":"The easiest way to earn points."}' http://localhost:5000/get_sim/cosine_similiarity
  ```

## Questions to consider

* Do you count punctuation or only words?  
* Which words should matter in the similarity comparison?  
* Do you care about the ordering of words?  
* What metric do you use to assign a numerical value to the similarity?  
* What type of data structures should be used? (Hint: Dictionaries and lists are particularly helpful data structures that can be leveraged to calculate the similarity of two pieces of text.) 