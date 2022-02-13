Corn and maize are basic ingredients in many regions across the world. The ears can be roasted and eaten as a vegetable right from the cob, or the kernels can be extracted and used to make a range of meals, including cereals and flour. Maize is also a significant source of starch, which can be converted into oils and high-fructose corn syrup. All of this makes maize and cornmeal very important ingredients, therefore it's understandable why one would want to keep them free of illnesses like Common Rust, Ray Leaf Spot, and Blight. These diseases are a major source of concern for maize and corn growers in Asia, Africa, and the Americas. Plant age, pathogen species, and environment all play a role in symptom expression. The diseases are more common in humid, warm climates. As a result, early detection of these diseases is critical in order to mitigate the harm. The main goal of this project is to use Efficientnet to classify various diseases.

# Data exploration
It can be shown that Gray Leaf spot contains less images than the other images, hence it can affect on the results. I'll add class weights in order to address this problem.

![7F4947F7-8D79-477A-AFB2-61ED0CA84FA8_1_201_a](https://user-images.githubusercontent.com/51881832/153748760-d3ec8594-6206-4a1f-812d-81a09c981caf.jpeg)

![83C8B1C0-6308-410C-A0E1-1EAF528F1DF6_1_201_a](https://user-images.githubusercontent.com/51881832/153748783-ccdde862-8546-4ae1-8a02-0359b4ed2d13.jpeg)

Using Efficientnet the validation achieved ~95%.
![E16FA221-BA4F-4356-94D8-D09077131881_1_105_c](https://user-images.githubusercontent.com/51881832/153748911-5c318f22-3372-488f-924e-6f2c320d0dab.jpeg)

The confusion matrix show very good results for the different classes:

![86C99271-4375-46FD-8DAD-F179373F2F76_1_201_a](https://user-images.githubusercontent.com/51881832/153748973-4ef39650-97b8-4029-84a0-0b323d3380a6.jpeg)

# Conclusions
From the confusion matrix it can be shown that the results are pretty good with ~95% average accuracy. It can be used to detect diseases as early as possible.
