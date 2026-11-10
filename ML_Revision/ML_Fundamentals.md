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

### 21. What is Data Preprocessing in Machine Learning?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Data preprocessing is the process of preparing raw data before giving it to a Machine Learning model. It includes handling missing values, duplicates, incorrect data, categorical values, and converting data into a suitable format.

```text
Example: If a dataset contains missing ages and text values like "Male" and "Female", we may fill the missing ages and encode the categories before training the model.
```
</details>

---

### 22. How do you handle missing values in a dataset?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Missing values can be handled by removing affected rows or columns, or by replacing the missing values with suitable values such as mean, median, or mode. The method depends on the data and the reason for the missing values.

```text
Example: If a few students have missing CGPA values, we could replace them with the median CGPA if removing those records would lose useful data.
```
</details>

---

### 23. What is an outlier?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> An outlier is a data point that is significantly different from the other values in a dataset. Outliers can sometimes represent errors, but they can also be genuine unusual observations.

```text
Example: If most employee salaries are between ₹3–10 LPA and one value is ₹500 LPA, it may be an outlier that needs investigation.
```
</details>

---

### 24. What is feature engineering?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Feature engineering is the process of creating or transforming input features to provide more useful information to a Machine Learning model. Good features can help a model identify patterns more effectively.

```text
Example: Instead of using only date of birth, we can create an Age feature because age may be more useful for predicting customer behavior.
```
</details>

---

### 25. What is feature selection?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Feature selection is the process of choosing the most relevant features for a Machine Learning model and removing unnecessary or irrelevant ones. This can reduce complexity and sometimes improve model performance.

```text
Example: For predicting house prices, house size and location may be useful, while a randomly generated customer ID is not useful.
```
</details>

---

### 26. What is categorical data, and how is it handled in ML?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Categorical data represents values belonging to specific categories rather than continuous numbers. Since many ML algorithms require numerical input, categorical values are usually converted into numbers using techniques such as one-hot encoding or label encoding.

```text
Example: Values like "Red", "Blue", and "Green" can be converted into numerical representations before training a model.
```
</details>

---

### 27. What is feature scaling?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Feature scaling is the process of bringing numerical features into comparable ranges so that features with larger values do not unnecessarily dominate the model. It is particularly important for algorithms that depend on distance or gradients.

```text
Example: If age ranges from 18–60 but salary ranges from 3,00,000–20,00,000, scaling can bring these features to comparable ranges.
```
</details>

---

### 28. What is the difference between normalization and standardization?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Normalization usually scales values to a fixed range, commonly 0 to 1. Standardization transforms values based on their mean and standard deviation so that the resulting data has approximately mean 0 and standard deviation 1.

```text
Example: If a model uses features like age and income with very different scales, normalization or standardization can make them more comparable.
```
</details>

---

### 29. What is Linear Regression?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Linear Regression is a supervised learning algorithm used to predict a continuous numerical value by learning the relationship between input features and the target. It tries to find a line that best represents the relationship between the variables.

```text
Example: A model can learn the relationship between house size and price and predict the price of a 2,000 sq.ft house.
```
</details>

---

### 30. What is Logistic Regression?
<details>
<summary><b>👁️ Click to reveal Answer & Example</b></summary>

> **Answer:**
> Logistic Regression is a supervised learning algorithm mainly used for classification problems. It calculates a probability for an input and uses that probability to determine the appropriate class.

```text
Example: A model can calculate the probability that an email is spam and classify it as Spam if the probability crosses a chosen threshold.
```
</details>
