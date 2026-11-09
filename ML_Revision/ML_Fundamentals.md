# 🤖 Machine Learning & AI Interview Q&A Notes

This repository contains fundamental questions and answers covering Artificial Intelligence, Machine Learning, Deep Learning, and core ML concepts.

---

### 0.1. What is Artificial Intelligence (AI)?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Artificial Intelligence is the field of creating machines or software that can perform tasks that normally require human intelligence, such as understanding language, recognizing images, solving problems, and making decisions.

```text
Example: A voice assistant that understands your question and responds appropriately is an example of AI.
```
</details>

---

### 0.2. How is Artificial Intelligence related to Machine Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> AI is the broader concept of making machines intelligent, while Machine Learning is one of the main approaches used to achieve AI by learning patterns from data instead of relying only on fixed rules.

```text
Example: A spam-filtering system is an AI application, and the ML model inside it learns from previous spam and non-spam emails to classify new emails.
```
</details>

---

### 1. What is Machine Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Machine Learning is a subset of AI where computers learn patterns from data and use them to make predictions or decisions without being explicitly programmed for every case.

```text
Example: A spam detection model learns from previous spam and non-spam emails and uses those patterns to classify a new email.
```
</details>

---

### 2. What is the difference between AI, Machine Learning, and Deep Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> AI is the broader concept of making machines perform intelligent tasks. ML is a subset of AI that learns from data, while Deep Learning is a subset of ML that uses multi-layer neural networks.

```text
Example: A chatbot is an AI application; an ML model can predict user behavior, while a neural network can be used for image or language understanding.
```
</details>

---

### 3. How does Machine Learning work?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Machine Learning works by providing data to a model, allowing it to learn patterns during training, and then using the trained model to make predictions on new data.

```text
Example: A house-price model learns from previous house sizes and prices and then predicts the price of a new house.
```
</details>

---

### 4. What is a Machine Learning model?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> A Machine Learning model is a system that learns patterns or relationships from training data and uses them to make predictions or decisions on new data.

```text
Example: A trained model can learn the relationship between experience and salary and predict the expected salary for a person with new experience data.
```
</details>

---

### 5. What is a dataset in Machine Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> A dataset is a collection of data used to train, validate, or test a Machine Learning model. It usually contains multiple records represented as rows and different attributes represented as columns.

```text
Example: A student dataset may contain columns such as name, CGPA, skills, placement status, and salary.
```
</details>

---

### 6. What are features and labels?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Features are the input variables given to a model, while the label is the output the model is expected to predict. Features help the model learn the relationship needed to predict the label.

```text
Example: For salary prediction, experience and education can be features, while salary is the label.
```
</details>

---

### 7. What is training in Machine Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Training is the process of teaching a model using data so that it can learn useful patterns. The model compares its predictions with the actual values and adjusts its parameters to improve.

```text
Example: A spam classifier is trained using thousands of emails already labeled as spam or not spam.
```
</details>

---

### 8. What is inference in Machine Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Inference is the process of using a trained model to make predictions on new or unseen data. During inference, the model uses the patterns it learned during training.

```text
Example: After training a spam model, checking whether a newly received email is spam is inference.
```
</details>

---

### 9. What is the difference between training and inference?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Training is when the model learns patterns from data and updates its parameters, while inference is when the trained model uses those learned patterns to make predictions on new data.

```text
Example: Teaching a model using old emails is training; classifying a new email as spam is inference.
```
</details>

---

### 10. What are the main types of Machine Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> The main types are Supervised Learning, Unsupervised Learning, and Reinforcement Learning. They differ mainly in how the model receives data and learns from it.

```text
Example: Predicting house prices is supervised learning, grouping customers is unsupervised learning, and teaching a robot through rewards is reinforcement learning.
```
</details>

---

### 11. What is Supervised Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Supervised Learning is a type of ML where the model learns from labeled data containing both inputs and their correct outputs. It learns the relationship between them to predict outputs for new data.

```text
Example: Training a model with emails labeled "Spam" and "Not Spam" so it can classify future emails.
```
</details>

---

### 12. What is Unsupervised Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Unsupervised Learning works with data that does not have predefined labels. The model tries to discover useful patterns, relationships, or groups within the data.

```text
Example: A company can use customer purchase data to automatically group customers with similar buying behavior.
```
</details>

---

### 13. What is Reinforcement Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Reinforcement Learning is a type of ML where the model learns to make decisions through trial and error by interacting with an environment as an agent. It receives feedback in the form of rewards or penalties to discover the best actions to take in new situations.

```text
Example: A robot can learn to walk by receiving rewards for moving correctly and penalties when it falls.
```
</details>

---

### 14. What is Classification in Machine Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Classification is a supervised learning task where a model predicts a category or class from the given input. The possible output classes are usually predefined during training.

```text
Example: An email classification model can predict whether an email belongs to Spam or Not Spam.
```
</details>

---

### 15. What is Regression in Machine Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Regression is a supervised learning task where a model predicts a continuous numerical value based on input features.

```text
Example: A model can use house size, location, and number of rooms to predict a house price such as ₹75 lakhs.
```
</details>

---

### 16. What is the difference between Classification and Regression?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Classification predicts a category or class, while regression predicts a continuous numerical value. The choice depends on the type of output we need from the model.

```text
Example: Predicting Spam/Not Spam is classification, while predicting a house price is regression.
```
</details>

---

### 17. What is Clustering?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Clustering is an unsupervised learning technique that groups similar data points together without predefined labels. The model identifies natural groups based on similarities in the data.

```text
Example: An e-commerce company can group customers into different segments based on their purchasing behavior.
```
</details>
---

### 18. What is the difference between Supervised and Unsupervised Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Supervised Learning uses labeled data where the correct output is known, while Unsupervised Learning uses unlabeled data and discovers patterns or groups on its own.

```text
Example: Predicting whether a transaction is fraudulent is supervised, while grouping customers based on spending behavior is unsupervised.
```
</details>

---

### 19. What is a feature in Machine Learning, and why is it important?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> A feature is an individual input variable that provides information to a model for making predictions. Good and relevant features can help the model learn useful patterns more effectively.

```text
Example: For predicting student placement, CGPA, technical skills, and internship experience can be useful features.
```
</details>

---

### 20. What are the basic steps in a Machine Learning pipeline?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> A basic ML pipeline involves collecting and cleaning data, preparing features, splitting the data, training a model, evaluating it, and using the trained model for predictions.

```text
Example: For spam detection: collect emails → clean data → create features → train model → evaluate it → classify new emails.
```
</details>
