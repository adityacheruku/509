import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestRegressor

# Load the training data
data = pd.read_csv('train.csv')

# Change the column names to upper case
data.columns = data.columns.str.upper()

# Select the relevant columns
X = data[['TITLE', 'DESCRIPTION', 'BULLET_POINTS', 'PRODUCT_TYPE_ID']]
y = data['PRODUCT_LENGTH']

# Fill missing values with the median
X = X.fillna(X.mode().iloc[0])

# Feature engineering
X['TITLE_LENGTH'] = X['TITLE'].apply(len)
X['DESCRIPTION_LENGTH'] = X['DESCRIPTION'].apply(len)
X['BULLET_POINTS_LENGTH'] = X['BULLET_POINTS'].apply(len)

# Vectorize the text data
vectorizer = CountVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(X['TITLE'] + ' ' + X['DESCRIPTION'] + ' ' + X['BULLET_POINTS'])

# Train a random forest regressor
model = RandomForestRegressor(n_estimators=100, max_depth=50, random_state=42)
model.fit(X_vectorized, y)

# Load the test data
test = pd.read_csv('test.csv')

# Change the column names to upper case
test.columns = test.columns.str.upper()

# Select the relevant columns
test_X = test[['TITLE', 'DESCRIPTION', 'BULLET_POINTS', 'PRODUCT_TYPE_ID']]
test_X = test_X.fillna(X.mode().iloc[0])

# Feature engineering
test_X['TITLE_LENGTH'] = test_X['TITLE'].apply(len)
test_X['DESCRIPTION_LENGTH'] = test_X['DESCRIPTION'].apply(len)
test_X['BULLET_POINTS_LENGTH'] = test_X['BULLET_POINTS'].apply(len)

# Vectorize the text data
test_X_vectorized = vectorizer.transform(test_X['TITLE'] + ' ' + test_X['DESCRIPTION'] + ' ' + test_X['BULLET_POINTS'])

# Make predictions on the test data
y_pred = model.predict(test_X_vectorized)

# Save the predictions to a CSV file
submission_df = pd.DataFrame({'PRODUCT_ID': test['PRODUCT_ID'], 'PRODUCT_LENGTH': y_pred})
submission_df.to_csv('submission.csv', index=False)
