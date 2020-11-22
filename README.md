## Introduction
This is an algorithm to compute similiarity of two documents, the score should be 0 to 1, where 0 means there are no similiarity and 1 means they are identical.

## Questions
You will have to make a number of decisions as you develop this solution:

* Do you count punctuation or only words?  
* Which words should matter in the similarity comparison?  
* Do you care about the ordering of words?  
* What metric do you use to assign a numerical value to the similarity?  
* What type of data structures should be used? (Hint: Dictionaries and lists are particularly helpful data structures that can be leveraged to calculate the similarity of two pieces of text.)  

## Requirements
1. Use the 3 sample texts provided below to develop your app. Samples 1 and 2 should be more similar than samples 1 and 3.
2. Only standard libraries may be used
3. Package this application as a web service that performs the comparison in response to a POST request containing the two texts in the body of the payload. You may use external libraries (i.e., Flask).
4. Package the web service in a Docker container that can be built and run locally or pulled down and run via Docker Hub.

## How to run web app
```
cd web
export FLASK_APP=run.py
flask run
```

## API Documentation
**Show User**
----
  Returns json data of similiarity of two texts, with key `similiarity`.

* **URL**

  /get_sim

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
  None

* **Data Params**

  `{"first": "some text","second":"another text"}`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "similiarity" : 0.867965}`

* **Sample Call:**

  ```
  curl -i -H "Content-Type: application/json" -X POST -d '{"first":"The easiest way .","second":"The easiest way to earn points."}' http://localhost:5000/get_sim
  ```