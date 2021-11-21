# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model is trained using sklearn[==0.24.1] Random Forest Classifier with randomized grid

## Intended Use
This model is used to predict the salary [<=50K | >50K] based on different variables, one record represents one ppl in the census

## Training Data
The data was obtained from the UCI ML repo https://archive.ics.uci.edu/ml/datasets/census+income. The target variable is the salary column, some cleaning processes have been taken to remove all the spaces in the data. During the training, we used one hot encoder for categorial features and label binarizer on the target label

## Evaluation Data
The evaluation data is used with the same pipeline in the training data, we select the required columns and apply the learned transformers to the columns

## Metrics
The model was evaluated using mean accuracy [0.855766053806917]

## Ethical Considerations
The data doesn't contains PII data and open to public, it shouldn't be a big concern
Although it contains the detailed personal info such as age and race
